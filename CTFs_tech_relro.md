# RELRO(Relocation Read-Only)
data 영역을 read-only로 하여금 data overwite를 할 수 없게 하는 기법   

> 어떤 부분들이 있는지 확인해보자. 

각 기법들에 대해서 동작 원리를 해보자 

## RELRO mode 
|                | partial                                   | full                                          |
| :---:          | :---:                                     | :---:                                         |
| compile option | gcc -Wl,-z,relro                          | gcc -wl,-z,relro,-z,now                       |
| GOT 상태       | Writable                                  | Read-Only                                     |
| 특징           | 함수 호출시에 해당함수의 주소를 알수 있음 | ELF 실행 시 GOT에 모든 라이브러리 주소 바인딩 |

## build with relro 
```bash 
# in ubuntu 18.04 version 

# default 
$ gcc -o test test.c 
$ checksec test 
[*] '/home/ubuntu/workspace/pie_test/test'
Arch:     amd64-64-little
RELRO:    Full RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      PIE enabled

# norelro 
$ gcc -o test test.c -Wl,-z,norelro
$ checksec test
[*] '/home/ubuntu/workspace/pie_test/test'
Arch:     amd64-64-little
RELRO:    No RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      PIE enabled

# with partial relro 
# ubuntu 18.04 version 이하에서는 relro옴션을 주게 되면 partial relro가 적용이 되었지만   
# 18.04의 경우 PIE가 활성화 되면 default로 full relro 적용됨 그래서 partial relro 할때 no-pie 옵션을 같이 줘야함
$ gcc -o test test.c -wl,-z,relro
$ checksec test
[*] '/home/ubuntu/workspace/pie_test/test'
Arch:     amd64-64-little
RELRO:    Full RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      PIE enabled

# option : -Wl,-z,relro
$ gcc -o test test.c -Wl,-z,relro -no-pie
$ checksec test
[*] '/home/ubuntu/workspace/pie_test/test'
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)

# with full relro 
# option : -Wl,-z,relro,-z,now
$ gcc -o test pie.c -Wl,-z,relro,-z,now -no-pie
$ checksec test
[*] '/home/ubuntu/workspace/pie_test/test'
Arch:     amd64-64-little
RELRO:    Full RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
```

