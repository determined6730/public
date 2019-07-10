# ld_preload vs ld_library_path
#hooking#hook#ld_preload#ld_library_path

## ld_preload 
ld.so 의 man page를 확인해 보면 아래와 같음
>  A list of additional, user-specified, ELF shared objects to be loaded before all others.  This feature can be used to selectively override functions in other shared objects.
즉 shared object가 load되기 전에 앞서 선택적으로 shared object의 function을 override 할 수 있다는 얘기임   
만약 ld_preload에 custom_stdio.so를 추가하고 여기에 printf를 작성하게 되면 기존 libc의 printf문이 링킹되지 않고 내가 작성한 printf문이 실행된다는 뜻임


- secure-execution mode에서는 '/'를 포함한 pathname들은 무시 됨 
- set-user-ID 걸린 실행파일이라면 standard search directory에서만 searching됨 

## ld_library_path


//TODOLIST ld_library_path로 하면 잘되는데 ld_preload로 하면 안되는데 이거 이유가 뭔지 확인해야함..
LD_LIBRARY_PATH=. ./so_test
LD_LIBRARY_PATH 는 라이브러리를 탐색하는 위치를 추가하는 것이고 LD_PRELOAD 는 앞서서 로딩하는 것 즉 기존 것을 추가한 뒤에 그 앞에 다른 라이브러리를 참조하도록 하는 것 같음. 그래서 새롭게 추가한 것은 라이브러리 패스가 맞지만 프리로드를 할 경우 그 뒤의 라이브러리도 찾아야 하기 때문에 그렇게 하지를 못하는 것임..
이게 뭔소리냐 하면... 기존 A프로그램에서 필요한 라이브러리들이 있을거고 기본적으로 이녀석들을 다 추가를 해놔야 한다. 이상황에서 엘디 프리로드로 라이브러리를 추가할 경우 가장 맨앞에 추가가 되고 실제 사용될대 여기서 심볼을 찾은뒤에 있는 경우 먼저 쓰게 되는 것이다. 그런데 만약! 뒤에 라이브러리가 없다면? 그냥 죽어버리는것.. 왜냐 뒤에 라이브러리르릴 참조하려고 하지만 실제 참조하는 라이브러리가 없기 때문에 라이브러리 패스는 라이브러리의 패스를 지정해서 찾는거기 때문에 이와 상관은 없음..
This can be used to selectively override functions in other shared objects.
재정의 하는데 사용되지 정의를 할때 사용되는 것이 아님
참고 문헌
https://www.joinc.co.kr/w/Site/C/Documents/Make_Library

## referneces 
- ld.so man page : <http://man7.org/linux/man-pages/man8/ld.so.8.html>

