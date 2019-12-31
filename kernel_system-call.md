# system call 

System calls are the primary mechanism by which user-space programs interact with the Linux kernel.     

System calls differ from regular function calls because the code being called is in the kernel. Special instructions are needed to make the processor perform a transition to ring 0 (privileged mode). In addition, the kernel code being invoked is identified by a syscall number, rather than by a function address.


## defining a syscall with SYSCALL_DEFINEn()

```
 SYSCALL_DEFINE3(read, unsigned int, fd, char __user *, buf, size_t, count)
    {
    	struct fd f = fdget_pos(fd);
    	ssize_t ret = -EBADF;
    	/* ... */
```

These SYSCALL_DEFINEn() macros are the standard way for kernel code to define a system call, where the n suffix indicates the argument count. The definition of these macros (in include/linux/syscalls.h) gives two distinct outputs for each system call.

```
    SYSCALL_METADATA(_read, 3, unsigned int, fd, char __user *, buf, size_t, count)
    __SYSCALL_DEFINEx(3, _read, unsigned int, fd, char __user *, buf, size_t, count)
    {
    	struct fd f = fdget_pos(fd);
    	ssize_t ret = -EBADF;
    	/* ... */
```

The first of these, SYSCALL_METADATA(), builds a collection of metadata about the system call for tracing purposes.   

TODOLIST  
>the generic definition of asmlinkage_protect() explains that it's used to prevent the compiler from assuming that it can safely reuse those areas of the stack.

## Syscall table entries 
 For "generic" architectures that don't provide an override of their own, the include/uapi/asm-generic/unistd.h file includes an entry referencing sys_read:
```
    #define __NR_read 63
    __SYSCALL(__NR_read, sys_read)
```
This defines the generic syscall number __NR_read (63) for read(), and uses the __SYSCALL() macro to associate that number with sys_read(), in an architecture-specific way. For example, arm64 uses the asm-generic/unistd.h header file to fill out a table that maps syscall numbers to implementation function pointers.



## references 
- Anatomy of a system call, part 1 : https://lwn.net/Articles/604287/
