# Python_Basics
- [ ] datetime
- [ ] lambda
- [ ] strftime
- [ ] strptime
- [ ] isinstance
- [ ] notebook
- [ ] data_load
- [ ] random_num
- [ ] matplotlib
- [ ] time.time()
- [x] [os](https://github.com/krystinli/Legoland/blob/main/python/python_basics.md#os)

### datetime
```py
import datetime
from datetime import date, datetime as dt

# datetime object containing current date and time
today = date.today()
today.month
current_ts = datetime.now()

today_formatted = today.strftime("%Y-%m-%d")
today_formatted => '2023-05-10'
```

### lambda
```py
x = lambda a, b : a * b
x(5, 6) >>> 30

# nested function 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mydoubler(11) >>> 22
```



### strftime
formats a datetime as a string
```py
dt.strftime('%y-%m-%d') >>> '20-08-05'

dt = datetime(2020, 10, 25)
dt.strftime("%B") >>> 'October'
```

### strptime
str parsed into datetime objects
```py
datetime.strptime("202008", "%Y%m") >>> datetime.datetime(2020, 8, 1, 0, 0)
```

### isinstance(target, type)->bool
```py
a = 5
isinstance(a, int) >>> True

# isinstance can accept a tuple of types:
a = 4.5; b = 5
isinstance(a, (int, float)) >>> True
```

### notebook
functions specific for notebooks
```python
# notebook viewing option for pandas
pd.set_option('display.max_columns', 999)
pd.set_option('display.max_rows', 999)

# latex conversion or HTML
%%latex
Some important equations:$E = mc^2$
$e^{i pi} = -1$

%%HTML
This is <em>really</em> neat!

%load imports.py
load another py file, a great way to store all the imports

%run imports.py
run a py file

# plotting
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# or
%matplotlib notebook
```

### data_load
With Dask vs. Pandas chunksize option
```python
# 1) data loading with pandas 
df_chunk = pd.read_csv("test_data.csv", chunksize=100000) 

chunk_list = []  
for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)

# 2) data loading with dask 
data = dask.dataframe.read_csv("test_data.csv").compute()
```

### string_attributes
```python
.strip() # remove whitespace
.lower()
.replace(old,new)

#  splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
a.split(",") # returns ['Hello', ' World!']
```

### random_num
```python
import random
random.randrange(1,10)
```

### matplotlib
```python
%matplotlib inline
import matplotlib.pyplot as plt

plt.plot(np.random.randn(50).cumsum())
```

### time.time()
runtime measure
```python
# 1) time.time()
import time
start_time = time.time()
...
print("This process takes %s seconds" %(time.time()-start_time))

# 2) %timeit magic function
import numpy as np

a = np.random.randn(100,100)
%timeit np.dot(a, a)
>> 35.6 µs ± 256 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

### OS
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. 
```py
import os 

# 1) Current Path
cwd = os.getcwd() # Get the current working directory
os.chdir("../newfolder")

# 2) Join Path
directory = "Documents"
parent_dir = "home/user/"
path = os.path.join(parent_dir, directory) 

mode = 0o666
os.mkdir(path, mode) 

# 3) Get the list of all files under root
path = "/"
dir_list = os.listdir(path) 
```
