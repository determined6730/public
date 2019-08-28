# \[python\]requests

## install

### pip install

```bash
pipenv install requests
```

or

```text
pip install requests
```

### source code

get source code

```text
git clone git://github.com/requests/requests.git
```

or

```text
curl -OL https://github.com/requests/requests/tarball/master
```

install

```text
cd requests
pip install .
```

## how to

### default

```python
import requests 
url = "http://www.google.com"

# for get method
params = {
}
# for post method
data = {
}
cookies = {
}

# get
r = requests.get(url)

# passing parameters 
paylaod = {'key1':'value1','key2':'value2'}
r = requests.get(url,params=payload)


print r
# post
# r = requests.post(url,headers=headers,data=data,cookies=cookies,headers=headers)  
values =  { 'key':'value' }
r = requests.post(url,data=values)
print r
```

* jupyter python requests example : [http://13.230.201.242:8888/notebooks/python%20/requests.ipynb](http://13.230.201.242:8888/notebooks/python%20/requests.ipynb)
* python requests 관련 : [https://2.python-requests.org//en/latest/user/quickstart/](https://2.python-requests.org//en/latest/user/quickstart/)

