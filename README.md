# public wiki

* Language
    * [go](go.md)
    * [python](python.md)
    * [praat](praat.md)
    * [CSharp](CSharp.md)

* Web
    * [REST](REST.md)

* CTFs
    * [tech](CTFs_tech.md)
        * [PIE](CTFs_tech_PIE.md) 
    * [pwnable.kr](pwnable.kr.md)
    * [temp](temp.md)
    * [ctf_tools](ctf_tools.md)
        * [libc-database](ctf_tools_libc-database.md)
    * [Load of SQL Injection](Load_of_Sql_injection.md)

* network
    * [mdns](mdns.md)

* Tools
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
* ELF
    * [ld.so](elf_ld.so.md)
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

* Language
    * [smali](smali.md)
    * [dot_net](dot_net.md)

* [blog](blog.md) 
    * [gitbook](blog_gitbook.md)





## docs 
- System V Application Binary Interface <https://www.uclibc.org/docs/psABI-x86_64.pdf>
