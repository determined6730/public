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

-------------------------------------------------------------

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

