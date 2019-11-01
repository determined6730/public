# inetd(interface service daemon)
유닉스 시스템에서 돌아private가는 슈퍼 서버 데몬으로서 인터넷 서비스들을 제공   
TCP,UDP packet이 특정 Port를 통해 들어오면 inetd가 해당 port에 해당하는 적절한 서버 프로그램을 실행해서 연결을 처리해 줌   
즉 1000번은 hello_world라는 프로그램과 매칭 시켜 놓으면 1000번을 통해 packet이 request를 하게 되면 hello_word를 실행시켜 통신이 가능하게끔 처리해 준다는 뜻임  
(항상 서버를 동작시켜 놓는 것이 아니라 요청이 올때 서버 프로그램을 동작시킨 뒤에 연결이 끊어지면 프로그램도 종료됨)

## 동작 
- 이 데몬은 부팅할 때 /etc/inetd.conf라는 설정 파일을 읽어들여 제공할 네트워킹 서비스들의 목록을 얻음  
- 해당 서비스들에 매칭되는 port를 생성   

<h2 name="sometext">aaaaa</h2>

```
test
asdlfkjasdflas
fa
sdf
d

d
d
d
d
d
d
d

d
d
d
d
d
d

d
d
d
d
d
d
d
d

d
d
d
d

dd


```

## 서비스들의 목록 
/etc/inetd.conf   
[test](#someText)

