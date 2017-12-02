#######################################
#                                     #
#    Author : Gabriel Grimberg        #
#    Module : Cloud Computing         #
#    Year   : Third Year              #
#    Type   : Assignment              #
#    About  : DockerCMS RESTFUL API   #
#                                     #
#######################################

#
# Imports needed for this Restful API.
#
from flask import Flask, Response, render_template, request
import json
from subprocess import Popen, PIPE
import os
from tempfile import mkdtemp
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return """
Available API endpoints:

GET /containers                     List all containers                          - Yes.
GET /containers?state=running       List running containers (only)               - Not Done.
GET /containers/<id>                Inspect a specific container                 - Yes.
GET /containers/<id>/logs           Dump specific container logs                 - Yes.
GET /services                       List all service                             - Not Done.
GET /nodes                          List all nodes in the swarm                  - Not Done.
GET /images                         List all images                              - Yes.

POST /images                        Create a new image                           - Yes.
POST /containers                    Create a new container                       - Yes.

PATCH /containers/<id>              Change a container's state                   - Yes.
PATCH /images/<id>                  Change a specific image's attributes         - Yes.

DELETE /containers/<id>             Delete a specific container                  - Not Done.
DELETE /containers                  Delete all containers (including running)    - Not Done.
DELETE /images/<id>                 Delete a specific image                      - Done.
DELETE /images                      Delete all images                            - Done.

"""

#############################
#          GET              #
#############################

#
# List all containers.
#
@app.route('/containers', methods=['GET'])
def containers_index():
    """
    List all containers
 
    curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers | python -mjson.tool
    curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers?state=running | python -mjson.tool

    """
    if request.args.get('state') == 'running': 
        output = docker('ps')
        resp = json.dumps(docker_ps_to_array(output))
         
    else:
        output = docker('ps', '-a')
        resp = json.dumps(docker_ps_to_array(output))

    #resp = ''
    return Response(response=resp, mimetype="application/json")


#
# Inspect a specific container.
#
@app.route('/containers/<id>', methods=['GET'])
def containers_show(id):
    """
    Inspect specific container

    """

    resp = ''

    return Response(response=resp, mimetype="application/json")


#
# Dump specific container logs.
#
@app.route('/containers/<id>/logs', methods=['GET'])
def containers_log(id):
    """
    Dump specific container logs

    """
    resp = ''
    return Response(response=resp, mimetype="application/json")


#
# List all images.
#
@app.route('/images', methods=['GET'])
def images_index():
    """
    List all images 
    
    Complete the code below generating a valid response. 
    """
    
    resp = ''
    return Response(response=resp, mimetype="application/json")
    

#############################
#          POST             #
#############################

#
# Create a new image.
#
@app.route('/images', methods=['POST'])
def images_create():
    """
    Create image (from uploaded Dockerfile)

    curl -H 'Accept: application/json' -F file=@Dockerfile http://localhost:8080/images

    """
    dockerfile = request.files['file']
    
    resp = ''
    return Response(response=resp, mimetype="application/json")
  
  
#
# Create a new container
#
@app.route('/containers', methods=['POST'])
def containers_create():
    """
    Create container (from existing image using id or name)

    curl -X POST -H 'Content-Type: application/json' http://localhost:8080/containers -d '{"image": "my-app"}'
    curl -X POST -H 'Content-Type: application/json' http://localhost:8080/containers -d '{"image": "b14752a6590e"}'
    curl -X POST -H 'Content-Type: application/json' http://localhost:8080/containers -d '{"image": "b14752a6590e","publish":"8081:22"}'

    """
    body = request.get_json(force=True)
    image = body['image']
    args = ('run', '-d')
    id = docker(*(args + (image,)))[0:12]
    return Response(response='{"id": "%s"}' % id, mimetype="application/json")


#############################
#          PATCH            #
#############################

#
# Change a container's state.
#
@app.route('/containers/<id>', methods=['PATCH'])
def containers_update(id):
    """
    Update container attributes (support: state=running|stopped)

    curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/b6cd8ea512c8 -d '{"state": "running"}'
    curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/b6cd8ea512c8 -d '{"state": "stopped"}'

    """
    body = request.get_json(force=True)
    try:
        state = body['state']
        if state == 'running':
            docker('restart', id)
    except:
        pass

    resp = '{"id": "%s"}' % id
    return Response(response=resp, mimetype="application/json")


#
# Change a specific image's attributes.
#
@app.route('/images/<id>', methods=['PATCH'])
def images_update(id):
    """
    Update image attributes (support: name[:tag])  tag name should be lowercase only

    curl -s -X PATCH -H 'Content-Type: application/json' http://localhost:8080/images/7f2619ed1768 -d '{"tag": "test:1.0"}'

    """
    resp = ''
    return Response(response=resp, mimetype="application/json")
    
    
#############################
#          DELETE           #
#############################

#
# Delete a specific container.
#
@app.route('/containers/<id>', methods=['DELETE'])
def containers_remove(id):
    """
    Delete a specific container - must be already stopped/killed

    """
    docker ('rm', id)
    
    resp = '{"id": "%s"}' % id
    return Response(response=resp, mimetype="application/json")

    
#
# Delete all containers (including running).
#
@app.route('/containers', methods=['DELETE'])
def containers_remove_all():
    """
    
    Force remove all containers - dangrous!

    """
    
    for containerschk in docker('ps', '-a', '-q').split('\n'):
        if containerschk:
            docker('stop', containerschk)
            docker('rm', containerschk)
        
    resp = 'The containers have all been deleted.'
    return Response(response=resp, mimetype="application/json")

 
#
# Delete a specific image.
#       
@app.route('/images/<id>', methods=['DELETE'])
def images_remove(id):
    """
    
    Delete a specific image
    
    """
    
    docker ('rmi', id)
    resp = '{"id": "%s"}' % id
    return Response(response=resp, mimetype="application/json")


#
# Delete all images.
#
@app.route('/images', methods=['DELETE'])
def images_remove_all():
    """
    
    Force remove all images - dangrous!

    """
    
    imgcheck = docker('images', '-q').split('\n')
    
    for id in imgcheck:
        if id:
            docker('rmi', '-f', id)
 
    resp = 'The images have all been deleted.'
    return Response(response=resp, mimetype="application/json")


##############################
#    End of API Endpoints    #
##############################


def docker(*args):
    cmd = ['docker']
    for sub in args:
        cmd.append(sub)
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr.startswith('Error'):
        print 'Error: {0} -> {1}'.format(' '.join(cmd), stderr)
    return stderr + stdout


# ###############################
# Docker output parsing helpers #
#################################

#
# Parses the output of a Docker PS command to a python List
# 
def docker_ps_to_array(output):
    all = []
    for c in [line.split() for line in output.splitlines()[1:]]:
        each = {}
        each['id'] = c[0]
        each['image'] = c[1]
        each['name'] = c[-1]
        each['ports'] = c[-2]
        all.append(each)
    return all


#
# Parses the output of a Docker logs command to a python Dictionary
# (Key Value Pair object)
#
def docker_logs_to_object(id, output):
    logs = {}
    logs['id'] = id
    all = []
    for line in output.splitlines():
        all.append(line)
    logs['logs'] = all
    return logs


#
# Parses the output of a Docker image command to a python List
# 
def docker_images_to_array(output):
    all = []
    for c in [line.split() for line in output.splitlines()[1:]]:
        each = {}
        each['id'] = c[2]
        each['tag'] = c[1]
        each['name'] = c[0]
        all.append(each)
    return all


#
# Main
#
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)