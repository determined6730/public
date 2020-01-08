# RELRO(Relocation Read-Only)
binary or process의 data section을 read-only로 변경하여 attacker가 해당 영역을 overriding하지 못하도록 하는 것.
(.ctors, .dtors, .jcr, .dynamic, .got)  

위 보호기법이 나오게 된 원인은 [dynamic_link](elf_dynamic_link.md)방식 때문임.  
기본적으로 dynamic link는 함수 호출 시점에 해당 함수의 주소만 공유 라이브러리로부터 알아오는 방법을 활용(lazy-binding)  
만약 바이너리에 임의의 영역에 data를 write할 수 있는 취약점이 있다면 [got_overwrite](ctfs_tech_got_overwrite.md)를 통해서 원하는 위치로 insturction point를 변경 할 수 있게 됨.

이를 방지 하기 위해서 



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



