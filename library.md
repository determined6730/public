# library 
소프트웨어 프로그램 및 응용프로그램을 개발하는데 사용되는 일련의 데이터 및 프로그래밍 코드들(functions,subroutines)의 집합체 라고 볼 수 있음.   
이것을 왜 쓰냐 하면.. 자주 쓰이는 코드들(재사용성이 높은)에 대해서 매번 코딩을 하지 않고 한번 잘 만들어 둔 뒤 필요할 때 가져다 쓰기 위해서 사용되며 미리 컴파일된 파일이기 때문에 내부 로직이 외부로 유출 되지 않는 장점도 있음  
(reversing을 통해서 로직을 분석할 수도 있찌만.. code를 제공할 필요는 없으니..)  
개발자 입장에서도 자신의 목적에 맞는 잘 만들어진 library가 있다면 직접 개발하지 않고 가져다 쓰면 되기 때문에 편리함   
ex) printf 문은 가장 많이 쓰이는 표준 함수인데 이것을 매번 코딩해야한다고 하면 정말 환장할 일이다.. 하지만 이것은 이미 표준 라이브러리에 이미 구현되어있어서 우리는 단순히 가져다 쓰기만 하는 것일 뿐이다.    

library는 링킹 방법에 따라 static, dynamic 두가지 종류로 나뉨

## static library 
정적라이브러리를 사용하여 컴파일 하면 링커가 프로그램에서 필요한 부분(라이브러리 함수를 가져다 쓰는곳)을 라이브러리에서 찾아서 프로그램에 복사해 넣음  
복사해 넣기 때문에 당연히 프로그램 용량은 증가 됨. 하지만 프로그램 실행시 별도의 라이브러리가 필요없음
확장자는 보통 .a를 가짐 

### make static library 
```
# make object file 
gcc -c libtest.c 

# make archive 
# ar은 archive 로 static library 만들때 사용되며
# r option -> libtest.o 를 libtest.a에 새롭게 포함
# c option -> libtest.a 가 없다면 새롭게 생성
ar rc libtest.a libtest.o

# 해당 library의 내용을 확인하고 싶을 때 ar -t 를 사용하면 됨
ar -t ./libtest.a

# objdump -D libtest.a 를 해보면 실제로 testlib.c에 작성한 function을 assem으로 확인 할 수 있음. 

# file libtest.a 를 통해 파일 타입을 확인해보면 current ar archive라고 나옴 
file libtest.a 
```
### static library와 함게 프로그램 제작 
```
# test.c 를 libtest.a 와 함께 compile 진행할 것임 
# -ltest -> -l option은 라이브러리를 포함시키겠다는 뜻이며 libXXXX.a인 경우 XXXX만 뒤에 바로 입력해주면 됨
# -L 옵션은 라이브러리의 위치를 지정하는 옵션으로 현재 디렉토리(.)을 입력해야함. 만약 -L을 사용하지 않는다면 표준라이브러리 디렉토리를 참조할 것임 
# 표준라이브러리 디렉토리는 /etc/ld.so.conf에 명시되어있음 
# 테스트용이며 분석을 편하게 하기 위해 -no-pie옵션을 통해 PIE disable 시킴 
gcc -o test test.c -ltest -L. -no-pie

# 또는 라이브러리 전체 명을 적어줘도 가능함. 자동으로 링킹시켜줌 :
gcc -o test test.c libtest.a
```

*objdump* 를 통해서 확인을 해보면 libtest관련 code 가 포함된 것을 확인 할 수 있음  

*file* 을 통해서 링킹 방식을 확인해보면 여전히 *dynamically linked 라고 나오는데 이는 표준 libc가 dynamic으로 링킹되었기 때문에   
즉 내가 지정한 libtest만 static 하게 들어간 상태이다. 전체를 static 하게 하고싶으면 *--static* 옵션을 사용하면 된다.
~~~
gcc -o test test.c -ltest -L. -no-pie --static
~~~
이렇게 하면 libc전체소스코드가 포함되어 용량이 확실히 늘어 나게된다..( 쓸데없는 것 까지 모두 추가가 됨.. printf만 추가할수 없나...?)TODOLIST


## shared library 
공유 라이브러리를 사용하여 컴파일을 하면 링커가 실행파일에 **실행될 때 우선 이 라이브러리를 로딩시킬것** 표시 하고 실제 바이너리가 실행될 때 라이브러리 오브젝트 파일을 가져와 사용하게 됨   

```
# ldd 를 사용해서 실행파일이 어떤 라이브러리를 필요로 하는지 확인 가능 
ubuntu@ip-172-26-12-50:~/workspace/library$ ldd test
        linux-vdso.so.1 (0x00007ffc4cd5e000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fa0d5e39000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fa0d622a000)
```
- 실행 파일에 내용을 복사 하지 않아 사이즈가 줄어둠 
- 바이너리 실행시 라이브러리가 꼭 필요함
- 라이브러리가 어느 주소에 mapping될지 모르기 때문에 프로그램에서 해당 함수에 대한 주소를 저장 X 
- 실행 시 함수 호출(함수의 주소를 알아내기 위한)을 위한 로직이 따로 필요 

### shared library 제작 
```
```

### shared library를 사용해 바이너리 컴파일 









## dinamic library 


