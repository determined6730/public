# android 

## apk 분석 
0. check apk list 
```
adb shell pm list packages -f
package:/data/app/com.lgeha.nuts-uXMVK36q5J3VG6DQBiQhlA==/base.apk=com.lgeha.nuts
```
1. apk file extraction
0번에서 나온결과물에서 처음부터 base.apk까지가 package_path 가 됨  
adb shell 밖에서 pull 하면 apk을 얻을 수 있음 
```
adb pull [package_path] [store_path]
```

또는 위방식 말고 apk extractor application을 down받아 추출해도 됨 

2. apktool(<https://ibotpeaches.github.io/Apktool/install/>) 사용하여 decompile
```
apktool d sample.apk 
```

3. 압축프로그램을 통해 apk파일 압축 해제
4. dex2jar(<https://sourceforge.net/projects/dex2jar/files/>)를 이용해서 jar파일 생성 
```
d2j-dex2jar.sh classes.dex
```
