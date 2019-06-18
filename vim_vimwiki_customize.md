#custom_vimwiki
vimwiki�� gollum�� �����ؼ� ����ϰ� �ִµ� ��ũ ���� ����� �޶� �̺κ��� �������ָ� ���� �����ϴ�. 
```
//vimwiki 
LinkUrl|Description 

//gollum
Description|LinkUrl
```

���� ���� ��Ȳ�̱� ������ vimwiki���� �ۼ��� ���ϰ� gollum���� ���� �ø��� Link�� ���� ���� ����. 

���� �⺻ vimwiki���� ������ �κ��� �� 3���� �̸�, ���� �� ������ �ϸ� ���� ����ϰ� ��� �� �� ���� �� ����.   
//TODOLIST
(������ ���� git���� �����ؼ� ��𼭵� ������ �� �ֵ��� �ϸ� ��)  

#### vars.vim 120 line
Diary������ �ϳ��� ���� ���� ������ gollum�� �°� �����Ͽ���   
�������� '  ' �̰����� �����̽��� 2ĭ�� �� �̰��� �ٹٲ��ϱ� ����
~~~
  " templates for the creation of wiki links
    " [[URL]]
      let g:vimwiki_global_vars.WikiDiaryLinkTemplate1 = wikilink_prefix . '__LinkUrl__'. wikilink_suffix . '  '
        " [[URL|DESCRIPTION]]
	  let g:vimwiki_global_vars.WikiDiaryLinkTemplate2 = wikilink_prefix . '__LinkDescription__'. wikilink_separator
	          \ . '__LinkUrl__' . wikilink_suffix . '  '
		  ~~~
		  [[/images/vimwiki/vimwiki2.JPG]]

		  #### diary.vim 150,153,162 line
		  WikiLinkTemplate -> WikiDiaryLinkTemplate ���� ���� 
		  ~~~
		  // 150��° �� month �ڿ� �����̽��� 2���� �־ �� ���� �ϵ��� �� 
		   \ '__Header__', s:get_month_name(month), '') . '  ')

		   // ���� vars.vim���� ������ ������ ������ ������ ��
		   let link_tpl = vimwiki#vars#get_global('WikiDiaryLinkTemplate2')
		   let link_tpl = vimwiki#vars#get_global('WikiDiaryLinkTemplate1')
		   ~~~
		   [[/images/vimwiki/vimwiki1.JPG]]

		   #### base.vim 1113 +line & 1116,1117 -line
		   ~~~
		   "���� �κ��� ���� �� (1116~1117line)
		     " try WikiLink
		       let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
		               \ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchUrl'))

			       "���Ӱ� �߰��� �� �κ� (1113line������)
			         if vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')) =~ "|"
				     let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
				              \ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchDescr'))
					        else
						    let lnk = matchstr(vimwiki#base#matchstr_at_cursor(vimwiki#vars#get_syntaxlocal('rxWikiLink')),
						             \ vimwiki#vars#get_syntaxlocal('rxWikiLinkMatchUrl'))
							       endif
							       ~~~
							       [[/images/vimwiki/vimwiki0.JPG]]
