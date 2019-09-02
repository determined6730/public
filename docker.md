# docker

```
## docker build images
sudo docker build -t ctftest0.0 .

## docker run 
sudo docker run -d -p 4000:4000 [repository:tag]

## docker exec 
sudo docker exec -i -t [container id] [command]

#docker ps 
sudo docker ps 

#docker ps -a 정지된 것 까지 모두 볼수 있음 
sudo docker ps -a 

#정지된 것까지 모두 삭제 
sudo docker rm `sudo docker ps -aq`

#docker kill 
sudo docker kill [container id]


```

## image 관리 
```
## 현재 이미지 정보를 출력해 줌 
sudo docker images 
## 이미지 삭제 
sudo docker rmi [image_id]
## 모든 이미지 삭제 
sudo docker rmi `sudo docker images -q`
## 실행중인 docker kill과 동시에 이미지 삭제
sudo docker rmi -f [image_id]

```


```
# docker container -> host
docker cp [container name]:[container 내부 경로] [host 파일경로]
```
