# PIE(Position Independent Executable)
위치 독립 실행 파일로 실행될 때마다 매핑되는 주소가 어디든 상관없이 실행되는 파일   
맵핑되는 주소와 상관없이 실행이 가능하단 뜻은 symbol들의 주소값이 절대값이 아니라 상대값이란 것  
PIE가 걸린 파일과 안걸린 파일을 보면 좀더 확연히 차이를 알 수 있음   





## PIE vs No PIE
### compile 
ubuntu 18.04 , gcc 7.4 에선 default로 PIE가 적용되어 있어 *-no-pie* 옵션을 통해서 강제로 적용 안시킬 수 있음 
```
# pie 해제
gcc -no-pie -o test test.c
# pie 적용
gcc -fPIE -o test_pie test.c
```

### pie check 
컴파일된 파일에 PIE가 적용되었는지 *checksec* 을 통해 확인 할 수 있음 
```
chekcsec [filename] 
```
[[/images/pie/pie1.PNG]]  


### symbol check
*objdump* 를 통해서 두 파일의 차이를 확인 할 수 있음 
```
objdump -d test
objdump -d test_pie
```

왼쪽 스크린샷이 *test_pie* 이며 우측 스크린샷이 *test* 파일임   
[[/images/pie/pie2.png]]    
symbol이 맵핑된 주소를 보게 되면 PIE가 적용된 경우 작은 값으로 맵핑되어 있으며, PIE가 적용 안되었을 때에는 절대값으로 맵핑되어 있음  
gdb를 통해서 실제 실행될 때 주소값을 확인해 보면 PIE가 적용되지 않은 실행파일은 disassemble해서 보인 주소값이 그대로 사용되며 PIE 가 적용된 파일은 맵핑된 주소값으로부터 해당 symbol의 주소값(offset)이 더해져 사용된다. 
[[/images/pie/pie3.png]]








