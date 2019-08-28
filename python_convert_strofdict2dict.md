# Convert a String representation of a Dictionary to a dictionary

아래 test는 dictionary 형태의 string type이라고 가정

```text
test = { "key1":"value1","key2":"value2" }
```

## using ast module

```text
import ast
dict = ast.literal_eval(test)
print type(dict)
```

## using json module

```text
import json
j = json.loads(test)
print type(j)
```

## testing

* [http://13.230.201.242:8888/notebooks/python%20/string%20representation%20of%20a%20dictionary%20convert%20to%20dict.ipynb](http://13.230.201.242:8888/notebooks/python%20/string%20representation%20of%20a%20dictionary%20convert%20to%20dict.ipynb)

