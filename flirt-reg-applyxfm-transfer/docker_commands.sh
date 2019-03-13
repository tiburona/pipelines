docker stop new-container && docker rm new-container
docker image rm friendlyhello
docker build -t friendlyhello .
docker create -it --name new-container friendlyhello
docker start new-container
docker exec -it new-container bash
