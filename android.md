# android

## \[\[frida\]\] 를 이용해 hooking

## tools

* [tcpdump](https://www.androidtcpdump.com/android-tcpdump/downloads)
* \[\[house\]\]

## apk 분석

1. check apk list 

   ```text
   adb shell pm list packages -f
   package:/data/app/com.lgeha.nuts-uXMVK36q5J3VG6DQBiQhlA==/base.apk=com.lgeha.nuts
   ```

   or 

   ```text
   apk extractor 라는 application을 통해서 추출 가능 함
   ```

2. apk file extraction

   0번에서 나온결과물에서 처음부터 base.apk까지가 package\_path 가 됨  

   adb shell 밖에서 pull 하면 apk을 얻을 수 있음 

   ```text
   adb pull [package_path] [store_path]
   ```

또는 위방식 말고 apk extractor application을 down받아 추출해도 됨

1. apktool\([https://ibotpeaches.github.io/Apktool/install/](https://ibotpeaches.github.io/Apktool/install/)\) 사용하여 decompile

   ```text
   apktool d sample.apk
   ```

2. 압축프로그램을 통해 apk파일 압축 해제
3. dex2jar\([https://sourceforge.net/projects/dex2jar/files/](https://sourceforge.net/projects/dex2jar/files/)\)를 이용해서 jar파일 생성 

   ```text
   d2j-dex2jar.sh classes.dex
   ```

4. JD-GUI\([http://jd.benow.ca/](http://jd.benow.ca/)\)을 이용해서 분석 시작 

## repackaging

### apktool rebuild

```text
<application 
...
android:debuggable="true"
...
```

```text
apktool b [folder-name] -o new.apk
```

### selfsign

```text
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore app-debug.apk alias_name
```

* [https://crosp.net/blog/software-development/mobile/android/android-reverse-engineering-debugging-smali-using-smalidea/](https://crosp.net/blog/software-development/mobile/android/android-reverse-engineering-debugging-smali-using-smalidea/)

