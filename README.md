# public wiki

* shortcuts
    - [chrome](shortcuts_chrome.md) 
    - [vim](shortcuts_vim.md)
    - [vimwiki](shortcuts_vimwiki.md)
    - [tmux](shortcuts_tmux.md) 

* language
    * [go](go.md)
    * [python](python.md)
    * [praat](praat.md)
    * [csharp](csharp.md)

* web
    * [rest](rest.md)

* ctfs
    * tech
        * [PIE](ctfs_tech_pie.md) 
        * [RELRO](ctfs_tech_relro.md)
        * [ASLR](ctfs_tech_aslr.md)
        * [load of sql injection](ctfs_tech_load_of_sql_injection.md)

    * [pwnable.kr](pwnable.kr.md)
    * [temp](temp.md)
    * [ctf_tools](ctf_tools.md)
        * [libc-database](ctf_tools_libc-database.md)

* network
    * [mdns](mdns.md)

* tools
    * [common](tools_common.md)
        * [jupyter](tools_common_jupyter.md)
        * [vim](tools_common_vim.md)
        * [netstat](netstat.md)
    * [linux](tools_linux.md)
        * [gdb](gdb.md)
        * [tmux](tmux.md)
        * [remmina](remmina.md)
        * [objdump](objdump.md)
        * [inetd](inetd.md)
        * [crosscompile](crosscompile.md)
        * [tcpdump](tcpdump.md)
    * [windows](tools_windows.md)
        * [dnspy](dnspy.md)
        * [process_explorer](process_explorer.md)

* kernel
	* [system-call](kernel_system-call.md)

* ELF
    * [ld.so](elf_ld.so.md)

* temporary 
    * [blah](blah.md)


- [[android]]
- [[linux]]
- [[컴파일과정|compile_process]]
- [ubuntu](ubuntu.md)

## Blog 
- <https://bpsecblog.wordpress.com/2016/09/23/ultrarev_hktrace/>
- <https://holinder4s.tistory.com/category/Wargame/LOB%28FC3%29>
- <https://12bme.tistory.com/138>
- <https://webdir.tistory.com/235>
- <https://mrrootable.tistory.com/38>

## TODO
- 왜 0x400000인가? in x86_64에서..
```
ld -verbose | grep -i text-segment
  PROVIDE (__executable_start = SEGMENT_START("text-segment", 0x400000)); . = SEGMENT_START("text-segment", 0x400000) + SIZEOF_HEADERS;

https://www.tutorialfor.com/questions-48876.htm
       --image-base value
           Use value as the base address of your program or dll.  This is the
           lowest memory location that will be used when your program or dll
           is loaded.  To reduce the need to relocate and improve performance
           of your dlls, each should have a unique base address and not
           overlap any other dlls.  The default is 0x400000 for executables,
           and 0x10000000 for dlls.  [This option is specific to the i386 PE
           targeted port of the linker]

```
- scapy (ip spoofing)
-  ASE CBC CRT mode IV 정리..
- <http://www.mantech.co.kr/micro-service/>
- <https://stackoverflow.com/questions/39861660/does-printf-allocate-memory-in-c>
- B-Tree
- [[radare2]]  :  아직 사용법을 전혀 모름.. 
- relocatable_vs_position-independent-code
- page
- relocatable
- position_independent_code
- section 
- 메모리 구역
- [[library]]
- [[object_file]]
- [[PLT]]
- [[ld_preload vs ld_library_path|ld-preload_vs_ld-library-path]]
- [[hooking]]
- [[frida]]
- [[docker]]
- asmlinkage  
당연히 인자를 레지스터에 저장하여 넘기는 방식이 빠르기 때문에 (fastcall)
최적화 옵션을 켜고 컴파일하는 경우 인자를 레지스터를 통해 전달하도록
함수의 호출부와 구현부를 변경해 버릴 수 있다. (일반적인 최적화 방법)
이 경우 GCC를 통해 자동 생성되는 코드는 적절히 변환되므로 문제가 없을테지만
직접 작성한 어셈블리 코드에서 함수를 호출하는 경우 문제가 발생하게 된다.

이 경우를 방지하기 위해 어셈블리 코드와 링크되는 함수는
인자를 (레지스터를 이용하지 않고) 스택을 이용해서 전달하도록
선언하는 데, 이 때 asmlinkage가 사용된다.  
http://egloos.zum.com/studyfoss/v/4951809

- inline 
C++은 인라인 함수(inline function)라는 내부에서 작성된 코드의 속도와 함수의 장점을 결합하는 방법을 제공한다. inline 키워드는 컴파일러에서 함수를 인라인 함수로 처리하도록 요청한다. 컴파일러가 코드를 컴파일하면 모든 인라인 함수가 인-플레이스(in-place) 확장된다. 즉, 함수 호출이 함수 자체의 내용 복사본으로 대체되어 함수 오버헤드가 제거된다! 단점은 인라인 함수가 모든 함수 호출에 대해 적절한 위치에서 확장되므로 인라인 함수가 길거나 인라인 함수를 여러 번 호출하는 경우 컴파일된 코드를 약간 더 크게 만들 수 있다는 것이다.

출처: https://boycoding.tistory.com/220 [소년코딩]  


* Language
    * [smali](smali.md)
    * [dot_net](dot_net.md)

* [blog](blog.md) 
    * [gitbook](blog_gitbook.md)





## docs 
- System V Application Binary Interface <https://www.uclibc.org/docs/psABI-x86_64.pdf>
