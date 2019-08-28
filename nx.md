# NX bit

No-execute bit는 프로세스의 명령어와 데이터 저장을 위한 메모리 영역을 분리시키기 위해 사용되는 cpu 기술로 Havard Architecture Process에서 나타나는 특징  
하지만 Von Neumann Architecture에서도 보안을 목적으로 사용되고 있음  
NX bit가 disable되어 있는 상태에서 EIP가 data영역으로 이동하게 될 경우 Processor 가 data를 instruction으로 해석해서 실행하게 됨

메모리 데이터 영역에 shell code등을 삽입 한 후에 buffer overflow 등으로 EIP를 해당 shell code가 위치한 data 영역으로 이동시켜 shell code를 실행 시킴.  
이를 NX bit를 통해 processor가 data영역에서 실행을 할 때 막고자 하는 것임

