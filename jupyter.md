# jupyter

## install 
~~~
sudo pip install --upgrade pip
sudo pip install jupyter
~~~

## remote settings
~~~
1. create config file (~/.jupyter/jupyter_notebook_config.py)
   ~~~
   jupyter notebook --generate-config
   ~~~
2. password setting 
   ~~~python
   from notebook.auth import passwd
   passwd()
   ~~~
   > 'sha1:xxxxx~~xxxx' 와 같은 결과가 나옴
3. ip & passwd setting 
   jupter_notebook_config.py 파일에 아래 내용 수정 
   ~~~
   c.NotebookApp.ip = '0.0.0.0'
   c.NotebookApp.port = 8888
   c.NotebookApp.port_retries = 50
   c.NotebookApp.open_browser = False #원격 서버에서 실행시 브라우저 오픈 X
   ~~~
4. execute  
   ~~~
   jupyter notebook
   ~~~

## shortcut 
### 셀 선택 모드에서 
| <center>key  | <center>description   |
| :-----:      | :------:              |
| a            | 위에 셀 추가          |
| b            | 아래에 셀 추가        |
| dd           | 셀 삭제               |
| x            | 셀 잘라내기           |
| c            | 셀 복사하기           |
| p            | command palette 열기  |
| shift+v      | 셀 위에 붙여넣기      |
| v            | 셀 아래 붙여넣기      |
| o            | 결과 열기/닫기 토글   |
| m            | 마크다운으로 변경     |
| y            | 코드로 변경           |
| s or ctrl+s  | 저장                  |
| enter        | 해당 셀 코드입력 모드 |
| z            | 실행 취소             |
| ctrl+shift+p | 명령어 검색           |
|              |                       |

## issues
- pwntools가 동작을 하지 않음 
  
## references
- shortcut : <https://ljs93kr.tistory.com/54>

