#libc-database

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

