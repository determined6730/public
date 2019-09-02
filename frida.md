# frida
dynamic instrumentation toolkit

## requirements
- python – latest 3.x is highly recommended
- pip

## install
windows 에서 진행 함
```
pip install frida-tools
```

## settings
1. download [firda-server](https://github.com/frida/frida/releases)
2. device에 옮겨서 실행 해야 함 
```
$ adb root # might be required
$ adb push frida-server /data/local/tmp/ 
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell "/data/local/tmp/frida-server &"
```
3. testing : device의 process list 출력 
```
$ frida-ps -U
```


## hook 시작 

### script 제작 
타겟에서 수행하고 싶은 것들을 javascript로 제작함 
```
'use strict;'

if (Java.available) {
    Java.perform(function() {

        // Create an instance of java.lang.String and initialize it with a string.
        const JavaString = Java.use('java.lang.String');

        var exampleString1 = JavaString.$new('Hello World, this is an example string in Java.');
        console.log('[+] exampleString1: ' + exampleString1);
        console.log('[+] exampleString1.length(): ' + exampleString1.length());

        // Create an instance of java.nio.charset.Charset, and initialize the default character set.
        const Charset = Java.use('java.nio.charset.Charset');
        var charset = Charset.defaultCharset();
        // Create a byte array of a Javascript string
        const charArray = "This is a Javascript string converted to a byte array.".split('').map(function(c) {
            return c.charCodeAt(0);
        })

        // Create an instance of java.lang.String and initialize it through an overloaded $new, 
        // with a byte array and a instance of java.nio.charset.Charset.
        exampleString2 = JavaString.$new.overload('[B', 'java.nio.charset.Charset').call(JavaString, charArray, charset)
        console.log('[+] exampleString2: ' + exampleString2);
        console.log('[+] exampleString2.length(): ' + exampleString2.length());

        // Intercept the initialization of java.lang.Stringbuilder's overloaded constructor.
        // Write the partial argument to the console.
        const StringBuilder = Java.use('java.lang.StringBuilder');
        //We need to overwrite .$init() instead of .$new(), since .$new() = .alloc() + .init()
        StringBuilder.$init.overload('java.lang.String').implementation = function (arg) {
            var partial = "";
            var result = this.$init(arg);
            if (arg !== null) {
                partial = arg.toString().replace('\n', '').slice(0,10);
            }
            // console.log('new StringBuilder(java.lang.String); => ' + result)
            console.log('new StringBuilder("' + partial + '");')
            return result;
        }
        console.log('[+] new StringBuilder(java.lang.String) hooked');

        // Intercept the toString() method of java.lang.StringBuilder and write its partial contents to the console.        
        StringBuilder.toString.implementation = function () {
            var result = this.toString();
            var partial = "";
            var n = result.indexOf("[0,0]")
            if (n == -1 ) {
                //console.log('[DEBUG] => ' + result)
            }
            
            return result;
        }
        StringBuilder.append.overload('java.lang.String').implementation = function (arg1) {
            console.log("[APPEND]"+arg1);
            var result = this.append(arg1);
            return result;
        }
        jj.b.overload('java.lang.String','java.lang.String').implementation = function (arg1,arg2) {
            console.log("[j.b]"+arg1+" "+arg2);
        }
        /*helpersK.a.overload('android.content.Context', 'java.lang.String', 'java.lang.String').implementation = function (arg1,arg2,arg3){
            console.log("[helper.k.b]arg2:"+arg2);
            console.log("[helper.k.b]arg3:"+arg3);
            return this.a.call(this,arg1,arg2,arg3);

        }*/
        bb.getString.overload('int').implementation = function (arg1){
            var test = this.getString.call(this,arg1);
            console.log("[GET_STRING]"+arg1.toString()+"------->"+test.toString());
            return test;

        }
        console.log('[+] StringBuilder.toString() hooked');
        
    }
)}
```
### apk attach with script 
```
frida-trace -U -l test.js com.samsung.familyhub
```




	
