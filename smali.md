# smali 

## types
```
V	void - can only be used for return types
Z	boolean
B	byte
S	short
C	char
I	int
J	long (64 bits)
F	float
D	double (64 bits)
L	# Object type ex->Lpackage/name/ObjectName; java->package.name.ObjectName
ex ) Ljava/lang/String -> java.lang.String

#array 
[I -> int[] 
[[I -> int[][] 
[Ljava/lang/String -> java.lang.String[]
```

## methods 
```
Lpackage/name/ObjectName;->MethodName(III)Z
(III) -> parameters  ( int , int , int )
Z -> return type 
method(I[[IILjava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;
String method(int, int[][], int, String, Object[])
```

## fields 
```
Lpackage/name/ObjectName;->FieldName:Ljava/lang/String;
object name -> method name -> type 

java.lang.String package.name.ObjectName.FieldName;
```

## get
```
iget-object vo,po,xxxx
po -> this 
v0 =  this.xxx
```

