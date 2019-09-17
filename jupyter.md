# jupyter

## install 
~~~
sudo pip install --upgrade pip
sudo pip install jupyter
~~~

## remote settings

1. create config file (~/.jupyter/jupyter_notebook_config.py)
   ~~~sh
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
   ~~~python
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

### 셀 선택 모드 
- **a** : 바로 위에 셀 추가  
- **b** : 바로 아래 셀 추가
- **dd** : 셀 삭제   
- **x** : 셀 잘라내기  
- **c** : 셀 복사하기  
- **p** : command palette 열기
- **Shift+v** : 셀 위에 붙여넣기 
- **v** : 셀 아래에 붙여넣기  
- **o** : 결과 열기/닫기 토글  
- **m** : 마크다운으로 변경  
- **y** : 코드로 변경
- **s or Ctrl+s** : 저장
- **enter** : 코드입력 모드로 변경
- **z** : 실행 취소
- **Ctrl+Shift+p** : 명령어 검색

## issues
- pwntools가 동작을 하지 않음 

## tips
### other notebook import  
다른 노트북을 import시켜주는 module을 설치 진행 
  ```shell
  $ sudo pip install import-ipynb
  ```
  실제 import를 진행시 아래와 같이 사용하면 됨 
  ```python
  import import_ipynb
  import test

  test.print_test()
  ```
### setup python2 or python3 for jupyter
```bash
# install python2
$ sudo python2 -m pip install ipykernel
$ sudo python2 -m ipykernel install --user

# install python3
$ sudo python3 -m pip install ipykernel
$ sudo python3 -m ipykernel install --user
```

### install R in jupyter
```base
# install R
$ sudo apt install r-base

# install requirements
sudo apt-get install libzmq3-dev libcurl4-openssl-dev libssl-dev jupyter-core jupyter-client

# install R packages in R 
install.packages(c('repr', 'IRdisplay', 'IRkernel'), type = 'source')

# making the kernel for jupyter in R
IRkernel::installspec()
IRkernel::installspec(user = FALSE)
```



## references
- shortcut   : <https://ljs93kr.tistory.com/54>
- install R  : <https://irkernel.github.io/installation/#linux-panel>
- kernels    : <https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>
