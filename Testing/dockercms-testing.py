#######################################
#                                     #
#    Author : Gabriel Grimberg        #
#    Module : Cloud Computing         #
#    Year   : Third Year              #
#    Type   : Testing			      #
#                                     #
#######################################


#############################
#          Index            #
#############################
#
### 1. View Index
#
import requests
import json

response = requests.get("http://35.205.198.91:8080").text
print(response)


#############################
#          GET              #
#############################
#
### 2 View Containers
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/containers").json()
print(response)


#
### 3 View Running Containers
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/containers", params='state=running').json()
print(response)


#
### 4 Inspect a specific container
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/containers/b80236ab245f").json()
print(response)


#
### 5 Dump specific container logs.
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/containers/b80236ab245f/logs").json()
print(response)


#
### 6 List all services
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/services").json()
print(response)


#
### 7 List all nodes in the swarm
#
import requests
import json
	
response = requests.get("35.205.198.91:8080/nodes").json()
print(response)


#
### 8 List all images
#
import requests
import json

response = requests.get("http://35.205.198.91:8080/images").json()
print(response)


#############################
#          POST             #
#############################
#
### 10 Create a new container
#
import requests
import json
data = {"image": "9ec4d80e0be6"}
header = {"Content-Type": "application/json"}
response = requests.post("http://35.205.198.91:8080/containers", data=json.dumps(data), headers=header)
print(response.json())


#############################
#          PATCH            #
#############################
#
### 11 Change a container's state
#
import requests
import json

data = {"state": "running"}
header = {"Content-Type": "application/json"}
response = requests.patch("http://35.205.198.91:8080/containers/45174b3ce50e", data=json.dumps(data), headers=header).json()
print(response)


#
### 12 Change a specific image's attributes
#
import requests
import json

data ={"tag": "test:1.0"}
header = {"Content-Type": "application/json"}
response = requests.patch("http://35.205.198.91:8080/images/9e7424e5dbae", data=json.dumps(data), headers=header).json()
print(response)


#############################
#          DELETE           #
#############################
#
### 13 Delete a specific container
#
import requests
import json

response = requests.delete("http://35.205.198.91:8080/containers/45174b3ce50e").json()
print(response)


#
### 14 Delete all containers including running ones
#
import requests
import json

response = requests.delete("http://35.205.198.91:8080/containers").json()
print(response)


#
### 15 Delete a specific image
#
import requests
import json

response = requests.delete("http://35.205.198.91:8080/images/9e7424e5dbae").json()
print(response)


#
### 16 Delete all images
#
import requests
import json

response = requests.delete("http://35.205.198.91:8080/images").json()
print(response)

