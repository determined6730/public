# analysis apk

0. [get application](#0)
1. [extract source list](#1)

## get application <a name="0"></a>
- check apk list 
```bash
# pm list packages -f | grep [app name]
adb shell pm list packages -f
package:/data/app/com.lgeha.nuts-uXMVK36q5J3VG6DQBiQhlA==/base.apk=com.lgeha.nuts
# or 
# apk extractor 라는 application을 통해서 추출 가능 함 
```
- file extraction 
```bash
# adb pull [package_path] [store_path]
adb pull data/app/com.lgeha.nuts-uXMVK36q5J3VG6DQBiQhlA==/base.apk ./
```

## extract source list <a name="1"></a>


## static 
## dynamic 

## [[frida]] 를 이용해 hooking

## tools 
- [tcpdump](https://www.androidtcpdump.com/android-tcpdump/downloads)
- [[house]]

## apk 분석 


2. apktool(<https://ibotpeaches.github.io/Apktool/install/>) 사용하여 decompile
```
apktool d sample.apk 
```

3. 압축프로그램을 통해 apk파일 압축 해제
4. dex2jar(<https://sourceforge.net/projects/dex2jar/files/>)를 이용해서 jar파일 생성 
```
d2j-dex2jar.sh classes.dex
```
5. JD-GUI(<http://jd.benow.ca/>)을 이용해서 분석 시작 

## repackaging
### apktool rebuild 
```
<application 
...
android:debuggable="true"
...
```

```
apktool b [folder-name] -o new.apk
```
### selfsign

```
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore app-debug.apk alias_name
```

##
- https://crosp.net/blog/software-development/mobile/android/android-reverse-engineering-debugging-smali-using-smalidea/


