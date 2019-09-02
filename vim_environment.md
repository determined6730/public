# vimrc

2019-06-18 사용버전
- [ ] ctag,cscope 셋팅 
- [ ] 자동 인덴트 toggle


```
" 한글 깨짐 현상 
set fencs=ucs-bom,utf-8,euc-kr.latin1
" esc 관련해서 셋팅 
set backspace=eol,start,indent
" swapfile 생성 막음
set noswapfile
" 붙여넣기 할때 자동 인덴트 막기
set paste
set encoding=utf-8
set fileencodings=utf-8,cp949

set ignorecase
let mapleader=","

call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vimwiki/vimwiki'
Plug 'iamcco/markdown-preview.vim'
Plug 'mhinz/vim-startify'
Plug 'mhinz/vim-startify'
Plug 'mattn/calendar-vim'
call plug#end()
nnoremap <Leader>p :MarkdownPreview<CR>
nnoremap <Leader>n :NERDTreeToggle<CR>
nnoremap <Leader>vv :VimwikiVSplitLink<CR>
nnoremap <Leader>vs :VimwikiSplitLink<CR>
nnoremap <Leader>q :wq<CR>
nnoremap <Leader>ll :lopen<CR>
nnoremap <Leader>ln :lnext<CR>
nnoremap <Leader>lp :lprevious<CR>
nnoremap <Leader>vws :VWS /
nnoremap <Leader>vll :execute "VWS /" . expand("<cword>") . "/" <Bar> :lopen<CR>
nnoremap <Leader>gd :VimwikiDiaryGenerateLinks<CR>
nnoremap <Leader>vt :VimwikiToggleListItem<CR>
nnoremap <Leader>s :SrcExplToggle<CR>
"NERDTree
let NERDTreeQuitOnOpen=1
let NERDTreeShowHidden=1
let NERDTreeShowHidden=1
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif " exit vim if only nerdtree remains
"for  SrcExpl list 
"let g:SrcExpl_winHeight=8
"let g:SrcExpl_refreshTime=100
"let g:SrcExpl_jumpKey="<ENTER>"
"let g:SrcExpl_gobackKey="<SPACE>"
"let g:SrcExpl_isUpdateTags=0

nmap <Leader>wn <Plug>VimwikiNextLink

" for Tag list 
let Tlist_Auto_Open=0
let Tlist_Use_Right_Window=1
let Tlist_Exit_OnlyWindow=1
nnoremap <Leader>t :Tlist<CR>

" for CtrlP list 
nnoremap <Leader>c :CtrlP<CR>


let NERDTreeQuitOnOpen=1
" for vim-airline
let g:airline#extensions#tabline#enabled = 1 " turn on buffer list
"let g:airline_theme='hybrid'
set laststatus=2 " turn on bottom bar



"for vimwiki
let g:vimwiki_conceallevel = 0
let g:vimwiki_autowriteall = 1
let g:vimwiki_list = [
    \{ 
    \   'path': '~/wiki/private',
    \   'ext' : '.md',
    \   'diary_rel_path': '.',
    \},
    \{
    \   'path': '~/wiki/public',
    \   'ext' : '.md',
    \   'diary_rel_path': '.',
    \},
\]
function! ToggleCalendar()
  execute ":Calendar"
  if exists("g:calendar_open")
    if g:calendar_open == 1
      execute "q"
      unlet g:calendar_open
    else
      g:calendar_open = 1
    end
  else
    let g:calendar_open = 1
  end
endfunction
:autocmd FileType vimwiki map c :call ToggleCalendar()<CR>

"let wiki.nested_syntaxes = {'ruby': 'ruby', 'python': 'python', 'c++': 'cpp', 'sh': 'sh', 'racket': 'racket'}

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

