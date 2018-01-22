#######################################
#                                     #
#    Author : Gabriel Grimberg        #
#    Module : Cloud Computing         #
#    Year   : Third Year              #
#    Type   : Testing			      #
#                                     #
#######################################

import requests
import json

#############################
#          Index            #
#############################
#
### 1. View Index
#
def index(ip):
	url = 'http://'+ip+':8080/'
	response = requests.get(url).text
	print(response)


#############################
#          GET              #
#############################
#
### 2 View Containers
#
def list_containers(ip):
	url = 'http://'+ip+':8080/containers'
	response = requests.get(url).json()
	print(response)


#
### 3 View Running Containers
#
def list_containers_running(ip):
	url = 'http://'+ip+':8080/containers'
	response = requests.get(url, params='state=running').json()
	print(response)


#
### 4 View all images.
#
def list_images(ip):
	url = 'http://'+ip+':8080/images'
	response = requests.get(url).json()
	print(response)


#
### 5 Inspect a specific container
#
def view_container(ip, id):
	url = 'http://'+ip+':8080/containers/'+id
	response = requests.get(url).json()
	print(response)


#
### 6 Dump specific container logs.
#
def container_logs(ip, id):
	url = 'http://'+ip+':8080/containers/'+id+'/logs'
	response = requests.get(url).json()
	print(response)


#
### 7 List all services
#
def list_all_services(ip):
	url = 'http://'+ip+':8080/services'
	response = requests.get(url).json()
	print(response)

#
### 8 List all nodes in the swarm
#
def list_all_nodes(ip):
	url = 'http://'+ip+':8080/nodes'
	response = requests.get(url).json()
	print(response)
	

#############################
#          POST             #
#############################
#
### 9 Create a new Image
#
def image_create(ip, tag, path):
	url = 'http://'+ip+':8080/images/'+tag+"/"+path
	response = requests.post(url)
	print(response.text)


#
### 10 Create a new container
#
def container_create(ip, id):
	url = 'http://'+ip+':8080/containers'
	data = {"image": id}
	header = {"Content-Type": "application/json"}
	response = requests.post(url, data=json.dumps(data), headers=header)
	print(response.json())


#############################
#          PATCH            #
#############################
#
### 11 Change a container's state
#
def container_update(ip, id, state):
	url = 'http://'+ip+':8080/containers/'+id
	data ={"state": state}
	header = {"Content-Type": "application/json"}
	response = requests.patch(url, data=json.dumps(data), headers=header).json()
	print(response)

#
### 12 Change a specific image's attributes
#
def image_update(ip, id, tag):
	url = 'http://'+ip+':8080/images/'+id
	data ={"tag": tag}
	header = {"Content-Type": "application/json"}
	response = requests.patch(url, data=json.dumps(data), headers=header).json()
	print(response)
	
	
#############################
#          DELETE           #
#############################
#
### 13 Delete a specific container
#
def container_delete(ip, id):
	url = 'http://'+ip+':8080/containers/'+id
	response = requests.delete(url).json()
	print(response)


#
### 14 Delete all containers including running ones
#
def container_delete_all(ip):
	url = 'http://'+ip+':8080/containers'
	response = requests.delete(url).json()
	print(response)


#
### 15 Delete a specific image
#
def image_delete(ip, id):
	url = 'http://'+ip+':8080/images/'+id
	response = requests.delete(url).json()
	print(response)


#
### 16 Delete all images
#
def image_delete_all(ip):
	url = 'http://'+ip+':8080/images'
	response = requests.delete(url).json()
	print(response)


#
### Main
#
if __name__ == "__main__":
	ip = 'FILL IP HERE'
	
	## Index.
	index(ip)
	
	## - Example -
	## Call whichever function you want here.
	
	## View containers.
	list_containers(ip)