# android booting


LK bootloader -> Little Kernel android Boot Loader   
(https://android.googlesource.com/kernel/lk/)  
- Hardware initialization: setting up vector table, MMU, cache, initialize peripherals,storage, USB, crypto, etc.
- Loads boot.img from storage.
- Supports flashing and recovery.  



## boot loader 
LK라고 불리는 부트로더는 실제 커널을 적재하고 실행하는 역할을 담당  
download mode & fastboot 기능 지원   
fastboot mode에서 각 파티션 이미지들을 Device의 메모리영역에 저장   
안드로이드 이외의 부트로더는 벤더와 같은 제조사에서 만든 부트로더에 해당  
부팅단계로보면 LK이전 단계에 해당하며 제조사마다의 고유의 Secure Boot메커니즘을 적용 가능   

## recovery image
부트로더와 비슷한 성격의 부트로더   
치명적인 에러(다운로드중 다운로드 실패, 부팅중 에러등)에 대한 복구를 위한 부트로더  
이복구이미지는 OTA로 배포되는 이미지에 포함되어 사후 업데이트시에 적용되는 솔루션임  

## Verified boot
안드로이드의 Verified Bootsms디바이스의 무결성을 검증하는 dm-verify(device Mapper -verify)에 기반해서 구현  
Device-Mapper는 가상 블럭 디바이스를 구현할 수 있는 범용 기법으로 제공하는 리눅스 커널 프레임워크   
DM은 LVM(Logical Volume Manager)에 기반하여 dm-crypt알고리즘을 이용하여 디스크 전체를 암호화   

[AVB](OS_android_booting_AVB.md)  









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
- file:///home/determined/Downloads/lm80-p0436-1_little_kernel_boot_loader_overview.pdf



