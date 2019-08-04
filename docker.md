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
