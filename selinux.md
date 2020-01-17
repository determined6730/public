# selinux
types for file objects   
domains for processes   

SELinux는 모든 프로세스와 객체마다 보안 컨텍스트를 부여하고 관리함  

-Z옵션에서 
사용자:역할:타입:레벨 정보가 출력됨    


px -ZC httpd   
-C옵션은 pid대신 이름으로 정보를 얻어오는것   
-Z 옵션은 컨텍스트 확인 가능  

## type enforcement 
기본적인 접근 통제를처리하는 매커니즘  
주체가 객체에 접근하려할대 주체의 컨텍스트가 객체에 접근할 권한이 있는지 판단하는 역할을 수행  

어떠한 프로세스가 어디 폴더에 접근한다고 치면   
프로세스가 주체 폴더가 객체 프로세스에 부여된 컨텍스트 가 해당 객체에 접근할 권한이 있는지 체크해야함  

주체에 대한 컨텍스트는 ps -ZC를 통해서 확인할수 있으며 흠..  

TE관련 에러 메세지는 기본적으로 /var/log/audit/audit.log에 남게 됨  


## Targeted Policy
/etc/selinux/targeted/에 정의   
```
allow httpd_t httpd_sys_content_t : file { ioctl read getattr lock open };
```
위의 의미는 httpd_t 주체가 httpd_sys_content_t 에 연결이 가능하며 관련 작업은 ioctl... 등등이 가능하단 의미이다.   


## android 에서의 policy


## 동작 모드
```
현재 적용되어있는 지확인 
getenforce
sestatus 

```

