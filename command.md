# command to copy all the libraries of the application
pip freeze >> requirements.txt
# command to build docker images
docker build -t test_image .
# command to list out images on your machine
docker images
# command to delete images
docker rmi image test_file
# command to create container
docker run -d -p 5009:5009 diamond:latest
# to bring up the running containers
docker ps
# to show all running and stop a running container
docker ps -a
# to rename container name
# command to build a container
docker run --name champion -dp 5008:5008 timothyimage:latest
# to stop running container using container ID
docker stop e256d190a538 - ID
# To delete or remove all built containers
docker rm -vf $(docker ps -a -q)

