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


