# Ubuntu

## [apt install list](linux_apt-get-list.md)


### Ubuntu 관련 
### [setting_timezone](ubuntu_setting_timezone.md)
### [[16.04 -> 18.04 Update on CLI|linux_updateOnCLI]]
### [[apt]]
### [[version_check]]
### [[install wine|linux_wine]]

### [shortcut](ubuntu_shortcut.md)


[apache2](ubuntu_apache2.md)

### aslr on/off
```bash
# ASLR on/off file 
ls /proc/sys/kernel/ | grep randomize
randomize_va_space 
# check
# randomize_va_space=0 : ASLR 해제
# randomize_va_space=1 : 랜덤 스택 & 랜덤 라이브러리 설정
# randomize_va_space=2 : 랜덤 스택 & 랜덤 라이브러리 & 랜덤 힙 설정
cat /proc/sys/kernel/randomize_va_space
# setting ( require root permission)
echo [num] > /proc/sys/kernel/randomize_va_space

# 실제 잘 적용됬는지 확인하고 싶다면.. 아래를 여러번 실행 후 주소 관찰
cat /proc/self/maps
```