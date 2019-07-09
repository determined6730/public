# tmux

## Shortcuts

### session 관련 

| <center>key | <center>description    |
| :------:    | :------:               |
| tmux ls     | session 정보 list 출력 |
| Ctrl+B , d  | detached 세션 중단     |
| Ctrl+B , s  | session change         |

### 외부에서 session 관리 

| <center>key                                                            | <center>description    |
| :------:                                                               | :------:               |
| tmux ls                                                                | session 정보 list 출력 |
| tmux attach -t [session-name or session-number]                        | sessiona attach        |
| tmux rename-session -t [session-name or session-number] [session-name] | session name 변경      |

### 기본 
| <center>key | <center>description |
| :------:    | :------:            |
| Ctrl + B    | tmux 기본 단축키    |
| ^B + :      | tmux 내 명령어 모드 |

### Copy mode

| <center>key | <center>description |
| :------:    | :------:            |
| ^B + [      | 스크롤 모드 진입    |
| Spacebar    | 블락 모드 진입      |
| Enter       | 복사                |
| q           | 나가기              |
| Ctrl B + ]  | 붙여넣기            |

### pane 

| <center>key | <center>description |
| :------:    | :------:            |
| Ctrl B + %  | vertical split      |
| Ctrl B + "  | horizontal split    |
| Ctrl B + o  | swap pane           | <- 이거 잘 안됨 확인 해야함 //TODOLIST
| Ctrl B + z  | toggle pane zoom    |

## tmux config file 
~/.tmux.conf 

## tip 

- 스크롤 하는 것   
<https://blog.outsider.ne.kr/702>  
셋팅해보고 있는데 전혀 잘 안됨.. 

- up down등의 키를 vim과 같이 만들기   
tmux.config 파일에 아래 내용 작성
``` 
set-window-option -g mode-keys vi
```  
<https://stackoverflow.com/questions/31154887/tmux-change-scroll-up-down-keys>  
<http://teamcrak.tistory.com/400>

- .tmux.config 파일 적용하기 
```
Ctrl B + : 
source-file ~/.tmux.conf
```

