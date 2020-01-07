

- bash에서 특정 함수만 disasemble 하고 싶을때.. 
  objdump -d a.out 하면 모든 함수가 다 disassemble되는데..   
  아래와 같이하면 원하는 함수만 disassemble 되어짐 
  ```
  gdb -batch -ex 'file ./pie' -ex 'disassemble main'
  ```
