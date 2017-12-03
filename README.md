# DockerCMS-Restful-API
A container management system (DockerCMS) using a restful API that manages containers, images, services and stacks by defining several routes for each task.

### Docker Swarm

- Created with one mananger and two workers.
- Tested with NGINX as a service.


### DockerCMS Using a Restful API.

- In the **my_application** folder and named **container-server.py**.


### Running the NGINX as a service in Docker swarm. (Uses Manager and Two Workers)

- ```sudo docker swarm init```
- Get the code and copy and paste that code into the workers.
- To check they have joined: ```docker node ls```
- Creating: NGINX Web Server ```docker service create --replicas 5 -p 80:80 --name web nginx```
- To check: docker service ps web


### Testing the DockerCMS

- **Tests the API using Python Code**

<<<<<<< HEAD
- In the Testing folder.

- **Tests the API using Bash**

#### Test 1: Main Page
curl http://35.195.116.183:8080
=======
### Test 1: Main Page
```curl http://35.195.116.183:8080```
>>>>>>> 23f7c8f05a9f4bdf4e6fb61de094f30704b0590d


**GET**

#### Test 2: View Containers
```curl http://35.195.116.183:8080/containers```

#### Test 3: View Running Containers
```curl http://35.195.116.183:8080/containers?state=running```

#### Test 4: Inspect a specific container
```curl http://35.195.116.183:8080/containers/<ID>```

#### Test 5: Dump specific container logs.
```curl http://35.195.116.183:8080/containers/<ID>/logs```

#### Test 6: List all service
```curl http://35.195.116.183:8080/services```

#### Test 7: List all nodes in the swarm
```curl http://35.195.116.183:8080/nodes```

#### Test 8: List all images
```curl http://35.195.116.183:8080/images```


**POST**

#### Test 9: Create a new image
```curl -H 'Accept: application/json' -F file=@Dockerfile http://35.195.116.183:8080/images```

#### Test 10: Create a new container
```curl -X POST -H 'Content-Type: application/json' http://35.195.116.183:8080/containers -d '{"image": "my-app"}'```


**PATCH**

#### Test 11: Change a container’s state.
```curl -X PATCH -H 'Content-Type: application/json' http://35.195.116.183:8080/containers/b6cd8ea512c8 -d '{"state": "running"}'```

```curl -X PATCH -H 'Content-Type: application/json' http://35.195.116.183:8080/containers/b6cd8ea512c8 -d '{"state": "stopped"}'```

#### Test 12: Change a specific image’s attributes.
```curl -s -X PATCH -H 'Content-Type: application/json' http://35.195.116.183:8080/images/7f2619ed1768 -d '{"tag": "test:1.0"}'```


**DELETE**

#### Test 13: Delete a specific container
```curl -s -X DELETE -H ‘Content-Type: application/json’ http://35.195.116.183:8080/containers/b6cd8ea512c8```

#### Test 14: Delete all containers including running ones
```curl -s -X DELETE -H ‘Content-Type: application/json’ http://35.195.116.183:8080/containers```

#### Test 15: Delete a specific image
```curl -s -X DELETE -H ‘Content-Type: application/json’ http://35.195.116.183:8080/images/7f2619ed1768```

#### Test 16: Delete all images
```curl -s -X DELETE -H ‘Content-Type: application/json’ http://35.195.116.183:8080/images```