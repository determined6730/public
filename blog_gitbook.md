# gitbook 

0. [create gitbook account](#create-gitbook-account)
1. [import pages from github](#import-pages-from-github)
2. [write readme page](#write-readme-page)
3. [write summary page](#write-summary-page)
4. [about pages](#about-pages)


## create gitbook account
gitbook homepage에서 계정 생성을 함. 

## import pages from github
github 에서부터 동기화를 시킴   
새로운 commit이 push  되면 자동으로 repository에서 땡겨 옴   

## write readme page
repository에서 README.md파일을 작성 해 놓으면 처음 loading되는 페이지가 README.md 내용으로 로드됨   
하지만 이를 작성하지 않을 경우 자동으로 생성하게 됨   

## write summary page
왼쪽 page lists에 보이는 내용은 SUMMARY.md파일의 내용이 보이게 되며,  
이것도 마찬가지로 작성되지 않은 상태에서 import해오게 되면 자동으로 모든 page들을 그냥 순차적으로 보여주게 됨   

## about pages 
summary에 작성되지 않은 md파일의 경우 gitbook에서 load되지 않음  
무슨말이냐 하면은 ..   
현재 gitbook 페이지를 summary에 적어 놓지 않을 경우 blog page에서 gitbook link를 타고 들어왔을 경우   
github.com/~~~/gitbook 으로 이동하게 되어 보이게 됨   
즉 무조건 적으로 summary에 페이지를 적어줘야 gitbook url내에서 동작하게 된다는 뜻임.   




