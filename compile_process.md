# compile 과정 
컴파일할때 어떤 일들이 일어나는지 궁금해서..   

test.c -> test.i -> test.s -> test.o -> test   

위 과정에 대해서 간략하게 하나씩 ..


## 전처리 과정 (test.c -> test.i) 
"#"으로 시작하는 전처리 구문들에 대해서 정리하는 작업   
- #include  -> header file 삽입
  "headerTest.h" -> 현재 폴더 위치에서 찾게됨 
  <stdio.h> -> 시스템에 저장된 header 파일 기본 위치에서 순서대로 찾게됨 
- #define or #ifdef ..  -> macro관련 치환 
 
### 예제 
test.c headerTest.h 파일 제작 후 전처리 진행(**gcc -E**)

```C
// test.c 
#include <stdio.h>
#include "headerTest.h"
#define SWAP(a,b) {int c = a; a = b; b = c;}
#define MAX 256

#define debug 0

#if debug
void test{void}(
	printf("test\n");
}
#endif

int main(void){
	int a = 10;
	int b = 20;
	headerF();
	SWAP(a,b);
	printf("a = %d b = %d MAX = %d\n",a,b,MAX);
	return 0;
}


// headerTest.h
#include <stdio.h>

void headerF(void){
        printf(" this is funcion in header files\n");
}
```
```
// gcc -E 진행 
gcc -E test.c
```
### 결과 
```
gcc -E test.c > test.i 
cat test.i 

extern int pclose (FILE *__stream);





extern char *ctermid (char *__s) __attribute__ ((__nothrow__ , __leaf__));
# 840 "/usr/include/stdio.h" 3 4
extern void flockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__));



extern int ftrylockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__)) ;


extern void funlockfile (FILE *__stream) __attribute__ ((__nothrow__ , __leaf__));
# 868 "/usr/include/stdio.h" 3 4

# 2 "test.c" 2
# 1 "headerTest.h" 1



# 3 "headerTest.h"
void headerF(void){
	printf(" this is funcion in header files\n");
}
# 3 "test.c" 2
# 14 "test.c"
int main(void){
	int a = 10;
	int b = 20;
	headerF();
	{int c = a; a = b; b = c;};
	printf("a = %d b = %d MAX = %d\n",a,b,256);
	return 0;
}
```  
위 내용을 보면 실제 headerTest.h파일 내용이 삽입된 것을 확인할 수 있으며,   
headerTest.h파일 위에 삽입된 내용들은 stduio.h파일임  
define관련 내용들이 정리된 것을 확인 할 수 있음 

## 컴파일 과정 (test.i -> test.S)
컴파일 과정은 상당히 복잡함.. 이부분에 대해선 나중에 기회되면 자세히 공부해보고 싶음 //TODOLIST  
여러 작업들이 이루어진 후에 최종적으로 어셈블리어(test.S)가 결과물로 나오게됨   

- hello.i
- 어휘분석
- 구분분석
- 의미분석
- 중간표현 생성 
- SSA(Static Single Assignment)
- SSA Optimizer
- RTL(Register Transfer Language)
- RTL Optimizer
- Code Generator
- hello.S

```
gcc -S test.i 
```

```
        .file   "test.c"
        .text
        .section        .rodata
        .align 8
.LC0:
        .string " this is funcion in header files"
        .text
        .globl  headerF
        .type   headerF, @function
headerF:
.LFB0:
        .cfi_startproc
        pushq   %rbp
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        movq    %rsp, %rbp
        .cfi_def_cfa_register 6
        leaq    .LC0(%rip), %rdi
        call    puts@PLT
        nop
        popq    %rbp
        .cfi_def_cfa 7, 8
        ret
        .cfi_endproc
.LFE0:
        .size   headerF, .-headerF
        .section        .rodata
.LC1:
        .string "a = %d b = %d MAX = %d\n"
        .text
        .globl  main
        .type   main, @function
main:
.LFB1:
        .cfi_startproc
        pushq   %rbp
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        movq    %rsp, %rbp
        .cfi_def_cfa_register 6
        subq    $16, %rsp
        movl    $10, -12(%rbp)
        movl    $20, -8(%rbp)
        call    headerF
        movl    -12(%rbp), %eax
        movl    %eax, -4(%rbp)
        movl    -8(%rbp), %eax
        movl    %eax, -12(%rbp)
        movl    -4(%rbp), %eax
        movl    %eax, -8(%rbp)
        movl    -8(%rbp), %edx
        movl    -12(%rbp), %eax
        movl    $256, %ecx
        movl    %eax, %esi
        leaq    .LC1(%rip), %rdi
        movl    $0, %eax
        call    printf@PLT
        movl    $0, %eax
        leave
        .cfi_def_cfa 7, 8
        ret
        .cfi_endproc
.LFE1:
        .size   main, .-main
        .ident  "GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
        .section        .note.GNU-stack,"",@progbits
```

## assemble 과정  (test.s -> test.o)
위에서 생성된 assembly code를 relocatable object code(기계어)로 변환되는 과정   

```
# -c option : assemble 과정 까지만 진행하고 linking은 진행 하지않음 
gcc -c test.s
```

```
ubuntu@ip-172-26-12-50:~/workspace/compile_process$ objdump -d test.o

test.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <headerF>:
   0:   55                      push   %rbp
   1:   48 89 e5                mov    %rsp,%rbp
   4:   48 8d 3d 00 00 00 00    lea    0x0(%rip),%rdi        # b <headerF+0xb>
   b:   e8 00 00 00 00          callq  10 <headerF+0x10>
  10:   90                      nop
  11:   5d                      pop    %rbp
  12:   c3                      retq

0000000000000013 <main>:
  13:   55                      push   %rbp
  14:   48 89 e5                mov    %rsp,%rbp
  17:   48 83 ec 10             sub    $0x10,%rsp
  1b:   c7 45 f4 0a 00 00 00    movl   $0xa,-0xc(%rbp)
  22:   c7 45 f8 14 00 00 00    movl   $0x14,-0x8(%rbp)
  29:   e8 00 00 00 00          callq  2e <main+0x1b>
  2e:   8b 45 f4                mov    -0xc(%rbp),%eax
  31:   89 45 fc                mov    %eax,-0x4(%rbp)
  34:   8b 45 f8                mov    -0x8(%rbp),%eax
  37:   89 45 f4                mov    %eax,-0xc(%rbp)
  3a:   8b 45 fc                mov    -0x4(%rbp),%eax
  3d:   89 45 f8                mov    %eax,-0x8(%rbp)
  40:   8b 55 f8                mov    -0x8(%rbp),%edx
  43:   8b 45 f4                mov    -0xc(%rbp),%eax
  46:   b9 00 01 00 00          mov    $0x100,%ecx
  4b:   89 c6                   mov    %eax,%esi
  4d:   48 8d 3d 00 00 00 00    lea    0x0(%rip),%rdi        # 54 <main+0x41>
  54:   b8 00 00 00 00          mov    $0x0,%eax
  59:   e8 00 00 00 00          callq  5e <main+0x4b>
  5e:   b8 00 00 00 00          mov    $0x0,%eax
  63:   c9                      leaveq
  64:   c3                      retq

```

assembly code에서 object code로 변환한 것을 확인 할 수 있음. 

```
ubuntu@ip-172-26-12-50:~/workspace/compile_process$ file test.o
test.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped

```

## linking 과정 (test.o -> test)
위 assemble과정이 끝난뒤 object file이 생성이 되는데, 여전히 실행 가능한 파일은 아님  
assemble의 결과에서 main함수의 call(첫번째 call은 headerF함수이고 두번째 call은 pinrtf)을 확인하게 되면 단순히 그다음 위치로 가는것을 확인 할 수가 있음  
즉 call하는 부분에서 symbol들의 주소가 정확하지 않다는 것임..  이런 부분이  링킹과정에서 어떻게 변화는지 확인을 해보면 좋을것 같음  

링커의 역활은 assemble과정에서 생성된 object file을 모아서 하나의 바이너리로 만들어 지도록 도와주는 역활  
object file이 여러개가 있다면 이 여러개를 합쳐서 각각의 영역( text, data 영역들..)을 모아서 하나의 바이너리로 만들어 준다고 보면 됨  
여기서 말하는 object file이란 사용자가 작성한 프로그램, 표준 c 라이브러리, 사용자 라이브러리등이 된다.   
즉 위에서 예시로 든 경우는 test.o 파일 하나밖에 없어 보이지만 printf를 사용하기 때문에 이미 만들어진 표준 C 라이브러리 오브젝트 파일을 링크하게 됨  


```
ubuntu@ip-172-26-12-50:~/workspace/compile_process$ objdump -s test.o

test.o:     file format elf64-x86-64

Contents of section .text:
 0000 554889e5 488d3d00 000000e8 00000000  UH..H.=.........
 0010 905dc355 4889e548 83ec10c7 45f40a00  .].UH..H....E...
 0020 0000c745 f8140000 00e80000 00008b45  ...E...........E
 0030 f48945fc 8b45f889 45f48b45 fc8945f8  ..E..E..E..E..E.
 0040 8b55f88b 45f4b900 01000089 c6488d3d  .U..E........H.=
 0050 00000000 b8000000 00e80000 0000b800  ................
 0060 000000c9 c3                          .....
Contents of section .rodata:
 0000 20746869 73206973 2066756e 63696f6e   this is funcion
 0010 20696e20 68656164 65722066 696c6573   in header files
 0020 0061203d 20256420 62203d20 2564204d  .a = %d b = %d M
 0030 4158203d 2025640a 00                 AX = %d..
Contents of section .comment:
 0000 00474343 3a202855 62756e74 7520372e  .GCC: (Ubuntu 7.
 0010 342e302d 31756275 6e747531 7e31382e  4.0-1ubuntu1~18.
 0020 30342e31 2920372e 342e3000           04.1) 7.4.0.
Contents of section .eh_frame:
 0000 14000000 00000000 017a5200 01781001  .........zR..x..
 0010 1b0c0708 90010000 1c000000 1c000000  ................
 0020 00000000 13000000 00410e10 8602430d  .........A....C.
 0030 064e0c07 08000000 1c000000 3c000000  .N..........<...
 0040 00000000 52000000 00410e10 8602430d  ....R....A....C.
 0050 06024d0c 07080000                    ..M.....
```
object file을 objdump 를 해보면 위와 같이 간단하게 나옴 
여기서 실제로 링킹과정까지 완성을 시킨후 다시 objdump를 진행해보면 실질적으로 실행 될 수 있는 파일로 만들기 위해 여러 기능들이 추가된 것을 확인 할 수 있으며, objectfile에선 보이지 않던 여러 section들도 확인 할 수가 있음 


```
gcc -o test test.o
```

```
ubuntu@ip-172-26-12-50:~/workspace/compile_process$ objdump -s test

test:     file format elf64-x86-64

Contents of section .interp:
 0238 2f6c6962 36342f6c 642d6c69 6e75782d  /lib64/ld-linux-
 0248 7838362d 36342e73 6f2e3200           x86-64.so.2.
Contents of section .note.ABI-tag:
 0254 04000000 10000000 01000000 474e5500  ............GNU.
 0264 00000000 03000000 02000000 00000000  ................
Contents of section .note.gnu.build-id:
 0274 04000000 14000000 03000000 474e5500  ............GNU.
 0284 340e262a 9bb29fb6 6e489776 d26eaee8  4.&*....nH.v.n..
 0294 725c9a79                             r\.y
Contents of section .gnu.hash:
 0298 01000000 01000000 01000000 00000000  ................
 02a8 00000000 00000000 00000000           ............
Contents of section .dynsym:
 02b8 00000000 00000000 00000000 00000000  ................
 02c8 00000000 00000000 44000000 20000000  ........D... ...
 02d8 00000000 00000000 00000000 00000000  ................
 02e8 0b000000 12000000 00000000 00000000  ................
 02f8 00000000 00000000 10000000 12000000  ................
 0308 00000000 00000000 00000000 00000000  ................
 0318 26000000 12000000 00000000 00000000  &...............
 0328 00000000 00000000 60000000 20000000  ........`... ...
 0338 00000000 00000000 00000000 00000000  ................
 0348 6f000000 20000000 00000000 00000000  o... ...........
 0358 00000000 00000000 17000000 22000000  ............"...
 0368 00000000 00000000 00000000 00000000  ................
Contents of section .dynstr:
 0378 006c6962 632e736f 2e360070 75747300  .libc.so.6.puts.
 0388 7072696e 7466005f 5f637861 5f66696e  printf.__cxa_fin
 0398 616c697a 65005f5f 6c696263 5f737461  alize.__libc_sta
 03a8 72745f6d 61696e00 474c4942 435f322e  rt_main.GLIBC_2.
 03b8 322e3500 5f49544d 5f646572 65676973  2.5._ITM_deregis
 03c8 74657254 4d436c6f 6e655461 626c6500  terTMCloneTable.
 03d8 5f5f676d 6f6e5f73 74617274 5f5f005f  __gmon_start__._
 03e8 49544d5f 72656769 73746572 544d436c  ITM_registerTMCl
 03f8 6f6e6554 61626c65 00                 oneTable.
Contents of section .gnu.version:
 0402 00000000 02000200 02000000 00000200  ................
Contents of section .gnu.version_r:
 0418 01000100 01000000 10000000 00000000  ................
 0428 751a6909 00000200 38000000 00000000  u.i.....8.......
Contents of section .rela.dyn:
 0438 b00d2000 00000000 08000000 00000000  .. .............
 0448 80060000 00000000 b80d2000 00000000  .......... .....
 0458 08000000 00000000 40060000 00000000  ........@.......
 0468 08102000 00000000 08000000 00000000  .. .............
 0478 08102000 00000000 d80f2000 00000000  .. ....... .....
 0488 06000000 01000000 00000000 00000000  ................
 0498 e00f2000 00000000 06000000 04000000  .. .............
 04a8 00000000 00000000 e80f2000 00000000  .......... .....
 04b8 06000000 05000000 00000000 00000000  ................
 04c8 f00f2000 00000000 06000000 06000000  .. .............
 04d8 00000000 00000000 f80f2000 00000000  .......... .....
 04e8 06000000 07000000 00000000 00000000  ................
Contents of section .rela.plt:
 04f8 c80f2000 00000000 07000000 02000000  .. .............
 0508 00000000 00000000 d00f2000 00000000  .......... .....
 0518 07000000 03000000 00000000 00000000  ................
Contents of section .init:
 0528 4883ec08 488b05b5 0a200048 85c07402  H...H.... .H..t.
 0538 ffd04883 c408c3                      ..H....
Contents of section .plt:
 0540 ff35720a 2000ff25 740a2000 0f1f4000  .5r. ..%t. ...@.
 0550 ff25720a 20006800 000000e9 e0ffffff  .%r. .h.........
 0560 ff256a0a 20006801 000000e9 d0ffffff  .%j. .h.........
Contents of section .plt.got:
 0570 ff25820a 20006690                    .%.. .f.
Contents of section .text:
 0580 31ed4989 d15e4889 e24883e4 f050544c  1.I..^H..H...PTL
 0590 8d05ca01 0000488d 0d530100 00488d3d  ......H..S...H.=
 05a0 f9000000 ff15360a 2000f40f 1f440000  ......6. ....D..
 05b0 488d3d59 0a200055 488d0551 0a200048  H.=Y. .UH..Q. .H
 05c0 39f84889 e5741948 8b050a0a 20004885  9.H..t.H.... .H.
 05d0 c0740d5d ffe0662e 0f1f8400 00000000  .t.]..f.........
 05e0 5dc30f1f 4000662e 0f1f8400 00000000  ]...@.f.........
 05f0 488d3d19 0a200048 8d35120a 20005548  H.=.. .H.5.. .UH
 0600 29fe4889 e548c1fe 034889f0 48c1e83f  ).H..H...H..H..?
 0610 4801c648 d1fe7418 488b05d1 09200048  H..H..t.H.... .H
 0620 85c0740c 5dffe066 0f1f8400 00000000  ..t.]..f........
 0630 5dc30f1f 4000662e 0f1f8400 00000000  ]...@.f.........
 0640 803dc909 20000075 2f48833d a7092000  .=.. ..u/H.=.. .
 0650 00554889 e5740c48 8b3daa09 2000e80d  .UH..t.H.=.. ...
 0660 ffffffe8 48ffffff c605a109 2000015d  ....H....... ..]
 0670 c30f1f80 00000000 f3c3660f 1f440000  ..........f..D..
 0680 554889e5 5de966ff ffff5548 89e5488d  UH..].f...UH..H.
 0690 3de30000 00e8b6fe ffff905d c3554889  =..........].UH.
 06a0 e54883ec 10c745f4 0a000000 c745f814  .H....E......E..
 06b0 000000e8 d2ffffff 8b45f489 45fc8b45  .........E..E..E
 06c0 f88945f4 8b45fc89 45f88b55 f88b45f4  ..E..E..E..U..E.
 06d0 b9000100 0089c648 8d3dbb00 0000b800  .......H.=......
 06e0 000000e8 78feffff b8000000 00c9c390  ....x...........
 06f0 41574156 4989d741 5541544c 8d25ae06  AWAVI..AUATL.%..
 0700 20005548 8d2dae06 20005341 89fd4989   .UH.-.. .SA..I.
 0710 f64c29e5 4883ec08 48c1fd03 e807feff  .L).H...H.......
 0720 ff4885ed 742031db 0f1f8400 00000000  .H..t 1.........
 0730 4c89fa4c 89f64489 ef41ff14 dc4883c3  L..L..D..A...H..
 0740 014839dd 75ea4883 c4085b5d 415c415d  .H9.u.H...[]A\A]
 0750 415e415f c390662e 0f1f8400 00000000  A^A_..f.........
 0760 f3c3                                 ..
Contents of section .fini:
 0764 4883ec08 4883c408 c3                 H...H....
Contents of section .rodata:
 0770 01000200 00000000 20746869 73206973  ........ this is
 0780 2066756e 63696f6e 20696e20 68656164   funcion in head
 0790 65722066 696c6573 0061203d 20256420  er files.a = %d
 07a0 62203d20 2564204d 4158203d 2025640a  b = %d MAX = %d.
 07b0 00                                   .
Contents of section .eh_frame_hdr:
 07b4 011b033b 40000000 07000000 8cfdffff  ...;@...........
 07c4 8c000000 bcfdffff b4000000 ccfdffff  ................
 07d4 5c000000 d6feffff cc000000 e9feffff  \...............
 07e4 ec000000 3cffffff 0c010000 acffffff  ....<...........
 07f4 54010000                             T...
Contents of section .eh_frame:
 07f8 14000000 00000000 017a5200 01781001  .........zR..x..
 0808 1b0c0708 90010710 14000000 1c000000  ................
 0818 68fdffff 2b000000 00000000 00000000  h...+...........
 0828 14000000 00000000 017a5200 01781001  .........zR..x..
 0838 1b0c0708 90010000 24000000 1c000000  ........$.......
 0848 f8fcffff 30000000 000e1046 0e184a0f  ....0......F..J.
 0858 0b770880 003f1a3b 2a332422 00000000  .w...?.;*3$"....
 0868 14000000 44000000 00fdffff 08000000  ....D...........
 0878 00000000 00000000 1c000000 5c000000  ............\...
 0888 02feffff 13000000 00410e10 8602430d  .........A....C.
 0898 064e0c07 08000000 1c000000 7c000000  .N..........|...
 08a8 f5fdffff 52000000 00410e10 8602430d  ....R....A....C.
 08b8 06024d0c 07080000 44000000 9c000000  ..M.....D.......
 08c8 28feffff 65000000 00420e10 8f02420e  (...e....B....B.
 08d8 188e0345 0e208d04 420e288c 05480e30  ...E. ..B.(..H.0
 08e8 8606480e 3883074d 0e40720e 38410e30  ..H.8..M.@r.8A.0
 08f8 410e2842 0e20420e 18420e10 420e0800  A.(B. B..B..B...
 0908 10000000 e4000000 50feffff 02000000  ........P.......
 0918 00000000 00000000                    ........
Contents of section .init_array:
 200db0 80060000 00000000                    ........
Contents of section .fini_array:
 200db8 40060000 00000000                    @.......
Contents of section .dynamic:
 200dc0 01000000 00000000 01000000 00000000  ................
 200dd0 0c000000 00000000 28050000 00000000  ........(.......
 200de0 0d000000 00000000 64070000 00000000  ........d.......
 200df0 19000000 00000000 b00d2000 00000000  .......... .....
 200e00 1b000000 00000000 08000000 00000000  ................
 200e10 1a000000 00000000 b80d2000 00000000  .......... .....
 200e20 1c000000 00000000 08000000 00000000  ................
 200e30 f5feff6f 00000000 98020000 00000000  ...o............
 200e40 05000000 00000000 78030000 00000000  ........x.......
 200e50 06000000 00000000 b8020000 00000000  ................
 200e60 0a000000 00000000 89000000 00000000  ................
 200e70 0b000000 00000000 18000000 00000000  ................
 200e80 15000000 00000000 00000000 00000000  ................
 200e90 03000000 00000000 b00f2000 00000000  .......... .....
 200ea0 02000000 00000000 30000000 00000000  ........0.......
 200eb0 14000000 00000000 07000000 00000000  ................
 200ec0 17000000 00000000 f8040000 00000000  ................
 200ed0 07000000 00000000 38040000 00000000  ........8.......
 200ee0 08000000 00000000 c0000000 00000000  ................
 200ef0 09000000 00000000 18000000 00000000  ................
 200f00 1e000000 00000000 08000000 00000000  ................
 200f10 fbffff6f 00000000 01000008 00000000  ...o............
 200f20 feffff6f 00000000 18040000 00000000  ...o............
 200f30 ffffff6f 00000000 01000000 00000000  ...o............
 200f40 f0ffff6f 00000000 02040000 00000000  ...o............
 200f50 f9ffff6f 00000000 03000000 00000000  ...o............
 200f60 00000000 00000000 00000000 00000000  ................
 200f70 00000000 00000000 00000000 00000000  ................
 200f80 00000000 00000000 00000000 00000000  ................
 200f90 00000000 00000000 00000000 00000000  ................
 200fa0 00000000 00000000 00000000 00000000  ................
Contents of section .got:
 200fb0 c00d2000 00000000 00000000 00000000  .. .............
 200fc0 00000000 00000000 56050000 00000000  ........V.......
 200fd0 66050000 00000000 00000000 00000000  f...............
 200fe0 00000000 00000000 00000000 00000000  ................
 200ff0 00000000 00000000 00000000 00000000  ................
Contents of section .data:
 201000 00000000 00000000 08102000 00000000  .......... .....
Contents of section .comment:
 0000 4743433a 20285562 756e7475 20372e34  GCC: (Ubuntu 7.4
 0010 2e302d31 7562756e 7475317e 31382e30  .0-1ubuntu1~18.0
 0020 342e3129 20372e34 2e3000             4.1) 7.4.0.
```

code 작성 부터 컴파일 링킹 까지 과정을 봤지만 실제 내부는 더 복잡한 과정들이 있음   
이부분에 대해선 다른 page에서 설명을 하도록 하겠음...   
- compiler 
- linking 에 필요한 부분들
- 등등 

## references 
- linking 관련 : <file:///C:/Users/samsung/AppData/Local/Microsoft/Windows/INetCache/IE/OG4URWGQ/11-linking.pdf>
