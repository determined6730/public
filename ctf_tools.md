# ctf tools

## pwntools

### install 
```
apt-get update
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install --upgrade pip
pip install --upgrade pwntools
```

### usage

#### recv & send 
```
```
#### debug 
```
context.terminal = ['tmux','sp','-h']
r = process("./ctf")
script = ```
b main
```
gdb.attach(r,script)
r.interactive()
```


## libc-database 
libc version을 찾아줌  
12bit는 aslr이 걸려 있어도 고정이라는 점을 활용해서 libc version을 찾아냄
```
# install 
git clone https://github.com/niklasb/libc-database.git

# Fetch all the configured libc versions and extract the symbol offsets. It will not download anything twice, so you can also use it to update your database:
./get 

# add custom libc 
./add /usr/lib/libc-2.21.so

# find the libc version 
./find printf 260 puts f30

```

