# booting


## boot loader 
LK라고 불리는 부트로더는 실제 커널을 적재하고 실행하는 역할을 담당한다.   





- KVB(Knox Verified Boot)  
  AVB(Android Verified Boot)를 향상 시킨 새로운 solution   
  AVB는 kernel 과 platform components의 integrity를 check  
  KVB는 bootloader까지 cover 함   
  bootloader에서 component check가 수행되며, 시스템이 시작되기 전에 validation이 됨   
  KVB는 Samsung S10 & android P 이상에서 지원됨   
- AVB(Android Verified Boot)   
  

# References
- https://docs.samsungknox.com/whitepapers/knox-platform/trusted-boot.htm
- https://android.googlesource.com/platform/external/avb/+/master/README.md#What-is-itAVB


