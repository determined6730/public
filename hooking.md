# hooking
#hook#hooking

## sample code 

### test.c 
puts함수를 hooking 하고자 함   
```C
include <stdio.h>

int main(void){
        puts("this is the test for hooking");
        return 0;
}
```
build
```
gcc -test.c -o test
```

### libhook.c
```C
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>

int puts(const char *message)
{
	// function pointer : puts함수와 동일하게 작성 
        int (*origin_puts)(const char *message);
        int result;
	// dlsym을 통해 pusts함수를 로딩해야함 
	// RTLD_NEXT 는 이미 custom, 즉 지금 현재의 puts를 찾아놨기 때문에 다음걸 찾아야함 
        origin_puts = dlsym(RTLD_NEXT, "puts");
	// original_puts를 통해서 원래 함수 목적에 맞게 실행
        origin_puts("[hook]");
        result = origin_puts(message);
        return result;
}
```
build
```
#//TODOLIST option별설명들어가야함 
# -shared : shared library를 만들기 위해서 
# -Wl linker에게 넘기는 명령임
# --no-as-needed
# -ldl
# -D_GNU_SOURCE
gcc -shared -Wl,--no-as-needed -ldl -fPIC ./hook.c -o libhook.so -D_GNU_SOURCE
```

## LD_PRELOAD 를 이용해서 실행 또는 setting 
```
# ld_preload없이 실행 할 때 
ubuntu@ip-172-26-12-50:~/workspace/hooking$ ./test
this is the test for hooking

# ld_preload를 주고 실행한 경우 
ubuntu@ip-172-26-12-50:~/workspace/hooking$ LD_PRELOAD=./libhook.so ./test
[hook]
this is the test for hooking

# export를 통해서 셋팅하는 경우
ubuntu@ip-172-26-12-50:~/workspace/hooking$ export LD_PRELOAD=./libhook.so

ubuntu@ip-172-26-12-50:~/workspace/hooking$ env | grep LD
LD_PRELOAD=./libhook.so

ubuntu@ip-172-26-12-50:~/workspace/hooking$ ./test
[hook]
this is the test for hooking
```

