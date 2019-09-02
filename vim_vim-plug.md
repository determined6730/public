# vim plug

# Vim-Plug
vim 관련 plugin들을 쉽게 설치하고 관리 할 수 있도록 해줌 

## install Vim-Plug
```bash
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

## installing plugins
1. .vimrc 파일 내에 아래 내용을 기입 후에 begin ~ end 사이에 사용하고자 하는 plugin 기입 
```
call plug#begin('~/.vim/plugged')
Plug 'itchyny/lightline.vim'
call plug#end()
```

2. 그리고 vim 을 실행 시킨 이후에 명령 모드에서 아래 명령어 실행 
```
:PlugInstall
```

## removing plugins
1. .vimrc 파일 내에서 지우고자 하는 Plug 라인을 삭제 한 후에 vim내에서 아래 명령어 실행 
```
:PlugClean
```

## setting in vimrc

## plugin list 
TODOLIST 
아래 내용 한단계 위로 올려서 각각에 대해서 간단히 설명을 할 것 

vim을 통해서 보통 src를 보거나 아님  vimwiki를 작성 하는 정도이며, 이때 설치하면 도움이 되는 
plugin-lists 들임..   

```
# vim의 위 아래 현재 탭과 그리고 파일 줄 시간 등을 보여주는 plugin
Plug 'vim-airline/vim-airline'
# 테마 
Plug 'vim-airline/vim-airline-themes'
# vim 내에서 [[vimwiki]]를 사용하게 해주는plugin
Plug 'vimwiki/vimwiki'
# markdown을 보여주는 plugin인데 remote에선 사실 쓸모가 없어보임 
Plug 'iamcco/markdown-preview.vim'
# vim을 시작할대 이전에 작성중이였떤 파일들을 세션으로 관리하고 곧장 시작할 수 있게 끔 해주는 것
Plug 'mhinz/vim-startify'
```




## References 
- <https://github.com/junegunn/vim-plug> 
- <https://www.ostechnix.com/vim-plug-a-minimalist-vim-plugin-manager/>
