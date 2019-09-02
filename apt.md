# apt (advanced package tool)
Debian시스템에 포함된 핵심 도구들의 집합체   

- 응용프로그램 설치
- 응용프로그램 삭제
- 응용프로그램 업데이트 
- 등등....



## repository 
/etc/apt/sourcel.list에 기본 repository 주소가 저장되어 있음   
만약 이를 변경 한게 되면 update&upgrade를 해줘야함

### 새로운 repository 추가 및 삭제 
기본 respository에 설치하고자 하는 package가 존재하지 않는 경우 추가해서 사용하면 됨   
추가 하게 되면 /etc/apt/sources.list.d 위치에 파일로 추가가 됨   
```
sudo add-apt-repository ppa:<repository-name>
sudo add-apt-repository ppa:<repository-name> -r
sudo apt-get update
sudo apt-get install <package-name>
```

## how to 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install [package-name]
sudo apt-get remove [package-name]
sudo apt-get purge [package-name]
sudo apt-get autoremove
sudo apt-get search <key-word>
sudo apt-get show <package_name>
sudo apt-get list
sudo 
```



