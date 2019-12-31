# ld.so

The programs ld.so and ld-linux.so* find and load the shared objects
(shared libraries) needed by a program, prepare the program to run,
and then run it.

olving shared object dependencies, the dynamic linker first
       inspects each dependency string to see if it contains a slash (this
       can occur if a shared object pathname containing slashes was
       specified at link time).  If a slash is found, then the dependency
       string is interpreted as a (relative or absolute) pathname, and the
       shared object is loaded using that pathname.


