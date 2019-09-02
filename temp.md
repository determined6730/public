# research 

## heap 
- house of heap   
: <https://github.com/midnight-sun-ctf/challenges2018/blob/master/qualifiers/haxpresso/exploit.py>
Vuln: Input not null terminated. Address leaks through stack data copied over to heap along with input. Followed by House of Force
// input not null terminaterd 
// leaking libc address 
// heap을 조작하여 포인터 조작 
// house of force ->
// top chunk의 값을 조작한 뒤에 
// 그다음 공격자가 heap의 크기를 조작하며 
// 할당받은 chunk의 영역에 값을 저장함으로써 공격을 함 

- heap overflow for leak and escape 
: <https://david942j.blogspot.com/2018/09/write-up-tokyowesterns-ctf-2018.html>

- double free 
: <https://ctftime.org/writeup/15063>
. Script://david942j.blogspot.com/2018/09/write-up-tokyowesterns-ctf-2018.html
## overflow 
- out of bound , uninitialized stack pointer 
: <https://changochen.github.io/2018-09-01-Tokyo-Western-CTF-2018.html>



