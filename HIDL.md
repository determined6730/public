# hidl 
hal interface definition language   
framework 랑 vendor사이의 통신을 위한 것임  

HIDL 은 클라랑 서버의 구현체를 가짐   
클라는 메소드를 콜링하는 것을 사용하고 서버는 클라로부터 요청을 받고 결과를 리턴하는 것을 구현함  

android.hardware.samples.lFoo@1.0  
[그림추가]  
이걸 보면 좀 이해가 될텐데   
1. iFoo.hal 을 hidl-gen을 통해서 auto generated를 하면   
2. Fooall.cpp , BpFoo.h iFoo.h BnFoo.h , iHWFoo.h가 생성이 된다. 
3. 그러면 iFoo.h를 클라랑 서버를 개발할때 header include해야하는것  


iFoo.h -> Ifoo의 인터페이스가 정의되어있는 파일임  
메소드와 타입이 정의되어 있다   
RPC메카니즘에 대해서는 구현되어있지 않은듯 함     

ihwFoo.h -> 인터페이스에서 데이터 타입에 대해 동기화를 하기 위한 함수에 대한 정의들이 구현되어있음   


## references 
- http://wisebada.blogspot.com/2018/05/android-hal-and-device-driver.html
