# aslr(address space layout randomization) 
stack, heap, shared library를 virtual memory에 mapping 시킬 때 Random한 위치에 배치 시키는 것 



## commands 
```
# option (/proc/sys/kernel/randomize_va_sapce)
# 0 : ASLR off
# 1 : Stack & Library 
# 2 : Stack & Library & Heap

# check 
cat /proc/sys/kernel/randomize_va_space

# on & off 
echo [op_num] > /proc/sys/kerenl/randomize_va_space
```

## wakenesses 
- non-full address randomization 
  segment 위치가 있으며 각각의 sement들은 해당 범위 내에서 randomization 하기 때문에 상위 bit 고정   
  memory alignment로 인해 하위 bit 고정   
  


## references 
- https://cpuu.postype.com/post/4077799
