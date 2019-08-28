# custom\_vimwiki

vimwiki는 자동으로 링크를 생성해 주며, description과 같이 사용할 수도 있음  
하지만 이때 description과 link address의 순서가 달라서 github wiki와 연동하는데 수정해서 사용해야 함

```text
//vimwiki 
LinkUrl|Description 

//gollum
Description|LinkUrl
```

위와 같은 상황이기 때문에 vimwiki에서 작성을 다하고 gollum으로 곧장 올리면 Link를 따라갈 수가 없다.

현재 기본 vimwiki에서 수정한 부분은 총 3군데 이며, 좀더 잘 정리를 하면 좀더 깔끔하게 사용 할 수 있을 것 같다. TODOLIST \(수정한 것은 git으로 관리해서 어디서든 가져올 수 있도록 하면 굿\)

vars.vim 120 line Diary변수를 하나더 만들어서 기존 순서를 gollum에 맞게 수정하였음 마지막에 ' ' 이것으로 스페이스바 2칸을 줌 이것은 줄바꿈하기 위함

```text
" templates for the creation of wiki links
" [[URL]]
let g:vimwiki_global_vars.WikiDiaryLinkTemplate1 = wikilink_prefix . '__LinkUrl__'. wikilink_suffix . '  '
" [[URL|DESCRIPTION]]
let g:vimwiki_global_vars.WikiDiaryLinkTemplate2 = wikilink_prefix . '__LinkDescription__'. wikilink_separator
\ . '__LinkUrl__' . wikilink_suffix . '  '
[[/images/vimwiki/vimwiki2.JPG]]

diary.vim 150,153,162 line
WikiLinkTemplate -> WikiDiaryLinkTemplate 으로 변경

// 150번째 줄 month 뒤에 스페이스바 2개를 넣어서 잘 정리 하도록 함 
\ '__Header__', s:get_month_name(month), '') . '  ')

// 위에 vars.vim에서 수정한 변수를 가지고 오도록 함
let link_tpl = vimwiki#vars#get_global('WikiDiaryLinkTemplate2')
let link_tpl = vimwiki#vars#get_global('WikiDiaryLinkTemplate1')
```

\[\[/images/vimwiki/vimwiki1.JPG\]\]

base.vim 1113 +line & 1116,1117 -line

```text
"기존 부분은 삭제 함 (1116~1117line)
" try WikiLink
let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
\ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchUrl'))

"새롭게 추가해 준 부분 (1113line밑으로)
if vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')) =~ "|"
let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
\ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchDescr'))
else
let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
\ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchUrl'))
endif
```

\[\[/images/vimwiki/vimwiki0.JPG\]\]

