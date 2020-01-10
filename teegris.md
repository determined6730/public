# 


TEE에서 실행되는 data와 code는 무결성과 기밀성을 보장함   
cpu가 normal 인지 secure world인지 알리기 위해서 SCR(Secure configuration register) 의 least significant 사용함   
NS bit 인데 0 은 secure state , 1 non secure state  

이제 두녀석이 서로 통신을 해야겠지..  데이터도 주고받고 뭐 왔다리 갔다리 해야하니까    
이걸 충족시키기 위해서 암에서 monitor mode를 만들어 줌  
이녀석은 두 월드 교환을 책임지는 녀석임   

> There are different ways to enter the Monitor Mode. From the NWd, it can be entered using a Secure Monitor Call, or SMC, instruction, through an interrupt or by raising an External Abort exception, as shown in the next figure. The same mechanisms can be used from the SWd in addition to writing directly to the Current Program Status Register, or CPSR, which can only be performed by privileged processes in the SWd.

노멀에서는 smc 콜을 통해서 시큐어 모니터로 들어가고 시큐어 오에스에서는 직접 CPSR에다가 써서 간다   

exception level 0~3 까지 있음 

ATF : Arm Trusted Firmware   
arm사에서 제공하는  TEE 인듯 이걸 삼성이 자체적으로 개발하는듯함   
최근에 변경된거고 원래 트러스트오닉에서 개발한 키니비를 쓰다가 최근 teegris로 변경함  


- secure boot : 다음것을 체크함 .. 한가지 중요 포인트는 첫번재 stage는 암묵적으로 trusted 해야함   
  보통 제조사에서 이걸 soc에 직접 넣어버림 bootrom 

- REE : Rich Execution Environment
- TEE : Trusted Execution environments  
- SMC call : Secure Monitor Call   
- switches execution from NWd to SWd  
- this jumps to what is called the monitor mode   
- TA 와 trustlet의 차이..?  ....?? 
trustlet은 movicore loadable format(MCLF)를 사용한다..?  
현재는 아닌것 같지만.. 햇갈린다..  

SWI(Software Interrupts) WSM(World Shared Memory)를 통해서 NWd SWd사이를 통신함  

### trustlet ( trustonic때의 kinibee? 이라서 teegris랑은 다를수도..?)
- loaded at virtual address 0x1000




## references
- http://allsoftwaresucks.blogspot.com/2019/05/reverse-engineering-samsung-exynos-9820.html
- https://blog.quarkslab.com/a-deep-dive-into-samsungs-trustzone-part-1.html
