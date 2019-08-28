# blukat

### file bluakt

```text
./blukat: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=cdf0b81df732844320ce82d036143c402f821439, not stripped
```

### checksec blukat

Arch: amd64-64-little RELRO: Partial RELRO Stack: Canary found \[\[NX\]\]: NX enabled \[\[PIE\|PICnPIE\]\]: No PIE \(0x400000\)

## blukat.c

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
char flag[100];
char password[100];
char* key = "3\rG[S/%\x1c\x1d#0?\rIS\x0f\x1c\x1d\x18;,4\x1b\x00\x1bp;5\x0b\x1b\x08\x45+";
void calc_flag(char* s){
    int i;
    for(i=0; i<strlen(s); i++){
        flag[i] = s[i] ^ key[i];
    }
    printf("%s\n", flag);
}
int main(){
    FILE* fp = fopen("/home/blukat/password", "r");
    fgets(password, 100, fp);
    char buf[100];
    printf("guess the password!\n");
    fgets(buf, 128, stdin);
    if(!strcmp(password, buf)){
        printf("congrats! here is your flag: ");
        calc_flag(password);
    }
    else{
        printf("wrong guess!\n");
        exit(0);
    }
    return 0;
}
```

입력 받는 곳이 buf변수에 128 length를 입력 받음  
buf는 100 length의 local variable 임  
\[fp\]\[buf\]\[canary\]....  
있어서 fp를 넘길수 있고 동시에 canary까지 덮을 수 있는데 ....

buf에 입력을 받은 뒤에 password와 buf를 비교후 else로 가서 exit\(0\)를 호출하게 됨

fp 로 부터 읽어온 값을 맞추지 못하면 곧장 exit\(0\)으로 흘러가게 되는데..  
이걸 어떻게 뭐 해야하는지...

