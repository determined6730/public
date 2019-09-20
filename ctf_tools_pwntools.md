# pwntools 

## install 
```
apt-get update
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install --upgrade pip
pip install --upgrade pwntools
```

## usage

- get symbol
  ```
  elf = ELF("./xxx.so")
  readOffset = elf.sym["read"]
  ```

- find string /bin/sh
  ```

  => leak_libc = ELF("./leak_libc")
  => binsh = leak_base_addr + list(local_libc.search('/bin/sh'))[0] 



  => strings leak_libc | grep bin/sh
  ```

#### recv & send 
```
```

#### debug 
~~~
p = gdb.debug("./ctf") <- 이렇게 해도 됨 
p = gdb.debug("./ctf",script) <- 이렇게 스크립트를 넣어도 됨

context.terminal = ['tmux','sp','-h']
r = process("./ctf")
script = ```
b main
```
gdb.attach(r,script)
r.interactive()
~~~



