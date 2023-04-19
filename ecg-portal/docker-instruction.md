cd ecg-portal

docker build -t ecg-portal:latest .

docker run -p 3000:3000 ecg-portal

open browser, http://172.17.0.2:3000/

####### TEST ######
docker build -t ecg-portal:test .

docker run -dit ecg-portal:test bash

docker ps

docker exec -it container_name bash

##########
