# radare2

## install 
```bash
git clone https://github.com/radare/radare2.git
sys/install.sh
```
### errors
ubuntu 16.04 gcc 4 or 5 version 대에서 설치를 진행하다 아래와 같이 지속적으로 컴파일 오류가 나는 경우가 발생  
>radare2 gcc: internal compiler error: Killed (program cc1)
ubuntu 18.04 및 gcc 7 으로 upgrade이후 오류없이 제대로 설치 가능했음

## 사용법 

### execute
```
r2 -w ./bin :  write mode 로 binary open ( binary 수정가능 )
r2 -d ./bin :  debug mode ( debugger command 사용가능 )
re ./bin : binary open
```

### prints

```
? : help -> 특정 명령어 뒤에 붙이게 되면 그 해당 명령어에 대한 설명이 나옴 
x 16 : hex 값으로 16개 를 출력 
s seek 명령어임  ->  현재 탐색 위치를 지정하는데 사용함 

a : analyze
aa : all analyze 

pdf : print disassemble function 
pdf @ main : main함수 disassem 

@ -> 실행되는 탐색 위치를 지정하는데 사용됨 

afn [name] [addr] : -> addr을 name으로 변경 함 

afl : function list

VV : 그래프 모드로 보여주는 것 
-> 그래프 모드에서는 방향키로 직이며 디스어셈블리를 볼수 있음 

현재노드는 하늘색으로 표시됨 
Tab키를 이용하여 다음 노드를 선택하거나 노드의 맨 윗부분에 적혀이는 g 명령어로 그 노드를 선택할 수 있음 
현재 노드로 가고싶으면 .을 누르면 됨 

p키를 누르면 그래프 타입이 바뀜 

x키를 누르면 현재 노드의 참조위치를 볼수 있음 
방향키를 이용하여 바로 그 위치로 이동가능하며 q를 누르면 나가고 
q를 통해서 그래프 모드 종료 

```

### strings 
```bash
fs # string이 어떻게 분류되어있는지 보여줌 
fs strings; f # 스트링을 보여줌 
izzq~[string] # [string]을 찾아줌 

axt @@ str.* -> 이게 뭐냐...

/c [addr] # 문자열이 어디서 참조되는지 알 수 있음. 
/c instr  # instruction을 검색하는 명령어인데 문자열 주소 그대로 가져다 쓰지 않는 경우 아무결과도 X

```


### graph mode 
```shell
vv # graph mode 
q  # exit graph mode

c # cursor mode   
   ㄴ b # break point
   ㄴ q # exit cursor mode
/ [string] # highlight

# move
g [offset] # go offset 
u/U # Undo/redo seek

# functions
df # define function

F2 # break point

```

## references 
- 공식 : <https://rada.re/r/>
- github : <https://github.com/radare/radare2>
- 공식가이드 : <https://radare.gitbooks.io/radare2book/content/>
- 한글설명 : <https://cpuu.postype.com/post/838572>

- 정리가 잘되어있음 : <https://fir3.tistory.com/22>
