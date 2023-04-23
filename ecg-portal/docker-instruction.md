cd ecg-portal

docker build -t ecg-portal:latest .

docker run -p 3000:3000 ecg-portal

open browser, access http://localhost:3000

on the other hand, we can open the url expose from container: http://172.17.0.2:3000/

###### Docker list container

docker ps

###### docker remove container

docker rm -f container_name

####### TEST ######
docker build -t ecg-portal:test .

docker run -dit ecg-portal:test bash

docker ps

docker exec -it container_name bash

##########
