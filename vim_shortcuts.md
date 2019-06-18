# vim shortcuts

TODOLIST  
맨위에 리스트업해줘야지 보고 넘어갈 수 있을듯.. 
스크롤로 내려가면서 항목을 보기가 너무 어려움

### 커서 이동
| <center>key | <center>description                      |
| :------:    | :------:                                 |
| 0           | 라인의 제일 앞으로 이동                  |
| ^           | 라인의 제일 앞으로 이동 nonblock으로     |
| f{char}     | 우측으로 해당 캐릭터 로 곧장 이동        |
| F{char}     | 좌측으로 해당 캐릭터로 곧장 이동         |
| t{char}     | 우측으로 해당 캐릭터 바로 앞위치로 이동  |
| T{char}     | 좌측으로 해당 캐릭터 바로 앞위치로 이동  |
| ;           | f,F,t,T 마지막 명령어 반복               |
| w           | 워드 단위로 이동  앞쪽 커서              |
| W           | 워드 단위(공백구분)로 이동 앞쪽커서      |
| e           | 워드 단위로 이동  제일 뒤쪽 커서         |
| E           | 워드 단위(공백구분)로 이동 뒤쪽커서      |
| b           | 워드 단위로 앞으로 이동 앞쪽 커서        |
| B           | 워드 단위(공백구분) 앞으로 이동 앞쪽커서 |
| ge          | 워드 단위로 앞으로 이동 뒤쪽 커서        |
| gE          | 워드 단위(공백구분) 앞으로 이동 뒤쪽커서 |
|             |                                          |

### 위치 관련
| <center>key | <center>description        |
| :------:    | :------:                   |
| ctrl+o      | **이전 위치로 돌아가기     |
| ctrl+i      | **앞선 위치로 돌아가기     |
| ctrl+e      | 스크롤 다운(커서는 그대로) |
| ctrl+y      | 스크롤 업(커서는 그대로)   |

> *현재 이전 위치로 돌아가기 는 되는데 다시 앞선 위치로 돌아가는게 tab과 같은기능을 함
이 문제는 좀 해결해야 함... *

### 다중 창   

| <center>key      | <center>description                  |
| :------:         | :------:                             |
| ctrl+w           | 창 관련 command mode                 |
| ctrl+w,hjkl      | 창 이동                              |
| ctrl+w,w         | 순차적으로 창 이동                   |
| ctrl+w,v         | 현재 파일을 수직으로 나눔            |
| ctrl+w,s         | 현재 파일을 수평으로 나눔            |
| ctrl+w,o         | 현재 커서의 창만 남기고 모든 창 삭제 |
| ctrl+w,r         | 창의 위치를 순환시킴                 |
| ctrl+w,=         | 창의 크기를 균등하게 만들어줌        |
| ctrl+w,_         | 수평상태에서 현재창의 크기를 최대화  |
| ctrl+w,\         | 수직상태에서 현재창의 크기를 최대화  |
| ctrl+w, [N] +or- | 창의 크기를 [N]숫자만큼 + 하거나 -   |
| ctrl+w, [N] >or< | 창의 크기를 [N]숫자만큼 > 하거나 <   |



### my settings   

| <center>key    | <center>description    |
| :------:       | :------:               |
| < Leader > p   | :MarkdownPreview<CR>   |
| < Leader > n   | :NERDTreeToggle<CR>    |
| < Leader > vv  | :VimwikiVSplitLink<CR> |
| < Leader > vs  | :VimwikiSplitLink<CR>  |
| < Leader > q   | :wq<CR>                |
| < Leader > ll  | :lopen<CR>             |
| < Leader > VWS | :VWS /                 |

### file buffer 

| <center>key           | <center>description                                  |
| :------:              | :------:                                             |
| e [file]              | 버퍼로 file 열기                                     |
| b [number]            | 버퍼 선택                                            |
| ls                    | 버퍼 목록 출력                                       |
| sp [file]             | 가로 분할 열기                                       |
| vsp file]             | 세로 분할 열기                                       |
| [number]bd            | 해당 버퍼 닫기                                       |
| bd + space + tab      | 버퍼를 앞에서 하나씩 선택하면서 삭제할수 있게 도와줌 |
| bw                    | 버퍼를 닫아주긴하는 //TODOLIST 위와 차이점?          |
| vert sb[number]       | 특정 buffer를 vertical 분할                          |
| vert sb + space + tab | 위 기능을 숫자 말고 파일이름으로 선택할 수 있게끔..  |
|                       |                                                      |



### Vim folding commands

zf#j creates a fold from the cursor down # lines.  
zf/ string creates a fold from the cursor to string .  
zj moves the cursor to the next fold.  
zk moves the cursor to the previous fold.  
za toggle a fold at the cursor.  
zo opens a fold at the cursor.  
zO opens all folds at the cursor.  
zc closes a fold under cursor.  
zm increases the foldlevel by one.  
zM closes all open folds.  
zr decreases the foldlevel by one.  
zR decreases the foldlevel to zero -- all folds will be open.  
zd deletes the fold at the cursor.  
zE deletes all folds.  
[z move to start of open fold.  
]z move to end of open fold.

https://wiki.ubuntu-kr.org/index.php/Vim

zf1G : fold everything before this line [N]  
" folding : hide sections to allow easier comparisons  
zf} : fold paragraph using motion  
v}zf : fold paragraph using visual  
zf'a : fold to mark  
zo : open fold  

zc : re-close fold  
" also visualise a section of code then type zf [N]  
:help folding

## VIMWIKI



### zfG : fold everything after this line [N]

http://daeny2.tistory.com/entry/VIM-mark-%EA%B8%B0%EB%8A%A5  
vim 마크 기능

https://m.blog.naver.com/PostView.nhn?blogId=chhh92&logNo=220569044272&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F  
https://blog.outsider.ne.kr/540 http://woowabros.github.io/tools/2017/07/06/vim-game-code-break.html
https://www.fprintf.net/vimCheatSheet.html
https://opentutorials.org/course/730/4581



