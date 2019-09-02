# tcpdump 
  
## how to

| <center>option   | <center>description                         |
| :-----:          | :------:                                    |
| -i eth0          | interface 선택                              |
| src x.x.x.x      | src 아이피 기반 덤프                        |
| dst x.x.x.x      | dst 아이피 기반 덤프                        |
| host x.x.x.x     | 해당 host로 통신하는 패킷 덤프              |
| and or           | 조건 조합                                   |
| -w -r [filename] | write read 로 파일을 저장하거나 읽을수 있음 |
| -c [num]         | num 만큼 보여줌                             |
| tcp port [num]   | 특정 port number 덤프                       |
| -v               | 자세한 정보를 보여줌                        |
| -vv              | 더욱 자세한 정보를 보여줌                   |
| -x               | 패킷 내용을 hex로 보여줌                    |
| -xx              | 패킷 내용을 hex와 ascii로 보여줌            |
|                 |                                             |


## install
```
sudo apt-get install tcpdump
```

