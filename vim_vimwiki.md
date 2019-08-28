# vimwiki

## install

\[\[vim-plug\|vim\_vim-plug\]\] 를 이용해서 설치 가능

```text
Plug 'vimwiki/vimwiki'
```

## setting in vimrc

아래 내용을 ~/.vimrc 에 추가

```text
" for vimwiki setting 
set nocompatible
filetype plugin on
syntax on

"특별한 기호등을 표현하는지 [[]]등.. //TODOLIST
let g:vimwiki_conceallevel = 0


"for vimwiki
let g:vimwiki_list = [
\{
\    'path': '~/wiki/sample1', " sample1에 대한 위키의 위치 
\    'ext' : '.md', " 생성되는 파일 확장자 
\    'diary_rel_path': '.', " 다이어리의 위치
\},
\{
\    'path': '~/wiki/sample2', " ssample2에 대한 위키의 위치 
\    'ext' : '.md',
\    'diary_rel_path': '.',
\},
\]
```

## shortcut

[http://www.picb.ac.cn/~xiaohang/vimwiki/tools/commands/vimwiki/Vimwiki1.1.1QR.pdf](http://www.picb.ac.cn/~xiaohang/vimwiki/tools/commands/vimwiki/Vimwiki1.1.1QR.pdf)

### wiki start

| shortcut | description |  |
| :--- | :--- | :--- |
| \ww | 기본 wiki의 index.md 파일 열기 |  |
| \numberww | number에 해당하는  wiki index.md 파일 열기 |  |
| \ws | 등록된 wiki의 리스트를 보여주고 선택할 수 있음 |  |
| \wi | 기본 wiki의 diary index.md 파일 열기 |  |
| \wd | wiki file 삭제 |  |
| \wr | wiki file 이름 변경 |  |
| \wi |  |  |
|  |  |  |
|  |  |  |

### follow link

| shortcut | description |
| :--- | :--- |
| Enter | 위키 링크 따라가기 |
| Shift+Enter | 창을 split해서 링크 따라가기 |
| Control+Enter | 창을 vsplit해서 링크 따라가기 |
| Tab | 문서 내에서 존재하는 다음 링크 찾기 |
| Shift+Tab | 문서 내에서 존재하는 이전 링크 찾기 |

### image link

| shortcut | description |
| :--- | :--- |
|  |  |

### todolist

> shift+enter // control+enter 이 두명령어 들이 먹히지 않는데 알아봐야할 것 같음 terminal에 따라 다름 즉 vim안에서의 문제가 아니라 terminal에 따라서 shift+enter, control+enter를 어떻게 받아들이는지에 따라서 다른것임 이것을 알아보기 위해선 일반 bash shell에서 control+v를 누른상태에서 shift+enter나 control+enter 그리고 enter를 눌러 보면 ^M 이런식으로 기호가 나타나는데 이게 터미널이 받아들이는 형식이다.

그런데 control+enter와 enter가 동일시하게 ^M이렇게 인식하고 있는데 이런경우 답이 없는 것임... 결국엔 vimrc내에서 key mapping을 통해서 진행 하는 수밖에 없음.. 현재 나는 +l , +w 등을 통해서 단축키를 지정해 놓은 상태임

### wiki search

```text
:VWS /wiki/
# 위명령어를 치면 wiki를 찾아서 가장 먼저 찾게되는 문서가 열리는데 
# 저 단어를 포함한 모든 리스트를 보고싶으면 아래 명령어를 이어서 하면 된다. 
:lopen
```

위 같은 경우 매번 타이핑하는 번거로움이 있는데 이것도 맵핑을 통해서 진행하고 싶음.. 근데 어떻게 해야할까... //TODOLIST

### convert vimwikinextlink

vimwiki tab이 vimwikiNextLink로되어 있어서 Ctrl+I가 먹히질 않음 이걸 해결 하기 위해선 아래와 같이 remapping 해주면 됨  
관련 내용 -&gt; [https://github.com/vimwiki/vimwiki/blob/master/doc/vimwiki.txt\#L259](https://github.com/vimwiki/vimwiki/blob/master/doc/vimwiki.txt#L259)

```text
nmap <Leader>wn <Plug>VimwikiNextLink
```

### markdown preview

Vim-Plug 를 이용해서 install

```text
Plug 'iamcco/markdown-preview.vim'
```

~/.vimrc에 아래 내용 기입 - 각각 설정 값등에 대해선 개인의 입맛에 맞춰서 셋팅

```text
nnoremap <Leader>m :MarkdownPreview<CR>

let g:mkdp_path_to_chrome = ""
" Path to the chrome or the command to open chrome (or other modern browsers).
" If set, g:mkdp_browserfunc would be ignored.

let g:mkdp_browserfunc = 'MKDP_browserfunc_default'
" Callback Vim function to open browser, the only parameter is the url to open.

let g:mkdp_auto_start = 0
" Set to 1, Vim will open the preview window on entering the Markdown
" buffer.

let g:mkdp_auto_open = 0
" Set to 1, Vim will automatically open the preview window when you edit a
" Markdown file.

let g:mkdp_auto_close = 1
" Set to 1, Vim will automatically close the current preview window when
" switching from one Markdown buffer to another.

let g:mkdp_refresh_slow = 0
" Set to 1, Vim will just refresh Markdown when saving the buffer or
" leaving from insert mode. With default 0, it will automatically refresh
" Markdown as you edit or move the cursor.

let g:mkdp_command_for_global = 0
" Set to 1, the MarkdownPreview command can be used for all files,
" by default it can only be used in Markdown files.

let g:mkdp_open_to_the_world = 0
" Set to 1, the preview server will be available to others in your network.
" By default, the server only listens on localhost (127.0.0.1).
```

## syntax

### link

```c
// 기본 링크 
[[]] 
// 이미지 링크 
{{file:../../images/vimwiki...}}
{{file:../../sample|Vimwiki}}
Transclude image with alternate text and some style: >
{{http://.../vimwiki_logo.png|cool stuff|style="width:150px;height:120px;"}}
```

## references

* [https://github.com/vimwiki/vimwiki/blob/master/doc/vimwiki.txt](https://github.com/vimwiki/vimwiki/blob/master/doc/vimwiki.txt)
* [http://thedarnedestthing.com/vimwiki%20cheatsheet](http://thedarnedestthing.com/vimwiki%20cheatsheet)
* [http://www.picb.ac.cn/~xiaohang/vimwiki/tools/commands/vimwiki/Vimwiki1.1.1QR.pdf](http://www.picb.ac.cn/~xiaohang/vimwiki/tools/commands/vimwiki/Vimwiki1.1.1QR.pdf)
* [https://github.com/vim-scripts/vimwiki/blob/master/doc/vimwiki.txt](https://github.com/vim-scripts/vimwiki/blob/master/doc/vimwiki.txt)
* [https://dokk.org/library/Vimwiki\_1.1.1\_Quick\_Reference\_\(Pospichal\_2001\)](https://dokk.org/library/Vimwiki_1.1.1_Quick_Reference_%28Pospichal_2001%29)
* [https://raw.githubusercontent.com/vimwiki/vimwiki/master/doc/vimwiki.txt](https://raw.githubusercontent.com/vimwiki/vimwiki/master/doc/vimwiki.txt)  

  엄청 자세히 설명되어있는 메뉴얼임 

