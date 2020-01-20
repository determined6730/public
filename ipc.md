# Inter Process Communication(IPC)

## PIPE(익명 PIPE)
두개의 프로세스를 연결하고 하나의 프로세스는 읽기만 하나의 프로세스는 쓰기만 가능함  
한쪽 방향으로만 통신이 가능한 파이프의 특징 때문에 Half-Duplex(반이중) 통신이라고 함  
송수신을 원한다면 파이프를 두개를 만들어서 사용 해야 함  

## Named PIPE(FIFO)
통신을 할 프로세스가 명확하게 알 수 있는 경우 사용  
부모프로세스와 무관하게 전혀 다른 모든 프로세스들 사이에서 통신이 가능함 ( 이름이 있는 파일을 사용하기 때문 )   
mkfifo를 통해서 생성하고 성공하면 명명된 파일이 생성됨  
이것 역시 반이중 통신임  

## Message Queue

## Shared Memory

## Memory Map

## Socket

## Semaphore



