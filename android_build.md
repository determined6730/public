### bashrc 
```
# make the folder ( mkdir ~/bin)
# add the path in bashrc file
PATH=$PATH:/home/determined/bin
# source ~/.bashrc
# make the working directory ( mkdir ~/workspace/aosp )
# cd ~/workspace/aosp
```

### repo 
Repo는 android환경에서 Git을 더 쉽게 사용할 수 있게 도와주는 도구 
```
$ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
$ repo init
$ repo init -u https://android.googlesource.com/platform/manifest
# master 이외의 브랜치를 체크아웃하려면.. 
# repo init -u https://android.googlesource.com/platform/manifest -b android-4.0.1_r1
$ repo sync
$ source build/envsetup.sh
```

##  
```
```
