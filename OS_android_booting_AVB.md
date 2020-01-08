# android verified boot 
Verified boot는 Device위에서 동작하는 end user의 소프트웨어에 대한무결성을 보장함   
Device firmware의 read only영역의 코드가 안전하고 알려진 보안 결함이 없는지 암호학적으로 확인후 메모리에 로드하고 실행함   
AVB는 Verified boot의 여러 구현 방법중 하나임   

## VBMeta struct 
AVB에서 쓰는 data struct 임  
여러 descriptors 와 metadata를 포함하고 있으며 이는 암호학적으로 Sign되어 있음   
descriptors는 image hash, image hashtree metadata, chained partitions등을 위해 사용되어짐  



