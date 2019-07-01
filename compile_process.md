# compile 과정 
컴파일할때 어떤 일들이 일어나는지 궁금해서..   

test.c -> test.i -> test.s -> test.o -> test   

위 과정에 대해서 간략하게 하나씩 ..


## 전처리 과정 test.c -> test.i 
"#"으로 시작하는 구문들에 대해서 정리하는 작업   
- #include 
- #define
위 구문에 대해서 헤더파일 추가 및 define 구문을 replace 함  
  
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
test.c 파일과 headerTest파일은 위와 같으며 **gcc -E** 를 통해서 작업 진행   

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
define되었던 내용들이 정리된 것을 확인 할 수 있음 



## 바이너리 코드 제작 
```C
#include <stdio.h>
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
	SWAP(a,b);
	printf("a = %d b = %d MAX = %d\n",a,b,MAX);
	return 0;
}
```
