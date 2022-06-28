# pandas 🐼
- [x] [pd.DataFrame](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pddataframe) `DataFrame`
- [x] [pd.info](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pdinfo) `info` `describe` `shape` `columns` `count` `nunique` `mean`
- [x] [pd.read_csv](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pdread_csv) `to_csv` `read_csv`
- [x] [pd.merge](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pdmerge) `merge` `concat`
- [x] [pd.loc](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pdloc) `loc` `iloc`
- [x] [pd.datetime](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pddatetime) `to_datetime` `strftime` `groupby` `dt.now()`
- [x] [pd.fillna](https://github.com/krystinli/Legoland/blob/main/python/python_pandas.md#pdapply) `fillna` `dropna` `isna` `isnull` `replace`

## pd.DataFrame
```py
# 1) Constructing DataFrame from random data (dictionary)
d = {
    'col1': [1, 2], 
    'col2': [3, 4],}
df = pd.DataFrame(data=d)

>>> df
   col1  col2
0     1     3
1     2     4

# or build it from array:
pd.DataFrame(
    np.array([
        [1, 3],
        [2, 4],
    ])
)

# To enforce a single dtype and set col names
>>> df = pd.DataFrame(
    data = d, 
    dtype = np.int8, 
    columns = ['col1','col2' ..],
   )

# 2) remove header
data = data.xs(
    "Category: All categories", 
    axis = 1, 
    drop_level = True,
    )

# drop columns/rows
df.drop(
    ["Column1"],
    axis = 1,
    ) 

# 3) convert pd series into data frame
new_df = col.to_frame()

# 4) extract a single value from panda series row
df[
    df[col] == A][col2].tolist()[0]
```

## pd.info
```py
# 1) General stats
df.info() # dtypes of all columns
df.describe() # distribution of all columns

df.shape # return (rows, cols) 
df.columns # show all the column names

# 2) Counting
df.col.nunique() # select count(distinct col_nm)
df.col.count() # select count(*)
df.col.value_counts() # count(distinct) 
df.drop_duplicates(keep=False) # drop dup rows

# 3) sorting
df.sort_values(
    by=["some_col"], 
    ascending=False, 
    inplace=True
)

df.sort_values(
    "some_col").head(10) 
    
# 4) Rename 
df = df.rename(
    columns={
        'oldName1': 'newName1', 
        'oldName2': 'newName2'}
)

# Name first row as col names        
df.rename(
    columns = df.iloc[0]) 

# Change column names to upper/lower case 
df["col_name"] = df["col_name"].str.lower()
df["col_name"] = df["col_name"].str.upper()

# 5) The memory footprint of object dtype columns is ignored by default:
df.memory_usage()
df.memory_usage(deep=True)
df.infer_objects().dtypes # infer better dtypes for object columns

# Use a Categorical for efficient storage of an object-dtype column with many repeated values:
>>> df['object'].astype('category').memory_usage(deep=True)
5244
```

## pd.read_csv
```py
# 1) avoid saving or getting index_col
data.to_csv("path/filename.csv", index = False)
pd.read_csv("path/filename.csv", index_col = 0)

# 2) remove index
pd.read_csv("filename.csv", sep=",").drop(["unnamed 0"], axis=1) 
pd.read_csv(
    "folder/filename.csv", 
    sep = "|", 
    header = None, 
    names = ["col1_nm","col2_nm",...] # assign new col names 
) 

# 3) result back to csv
df2.to_csv(
    "filename_xxxx.csv", 
    sep = ',', 
    index = False, 
    date_format = '%Y-%m-%d'
)

# 4) reading with chunksize option 
df_chunk = pd.read_csv(
    "test_data_75MB.csv", 
    chunksize=100000,)

# recombine the data
chunk_list = []  
for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)
```

## pd.merge
```py
# 1) Inner join and left join on column named a
df1.merge(df2, how='inner', on='a')
df1.merge(df2, how='left', on='a') # or cross 

# 2) Full outer join with left and right suffixes appended to any overlapping columns
df1.merge(
    df2, 
    left_on='lkey', 
    right_on='rkey', 
    suffixes=('_left', '_right')
) 

>>> lkey  column_left rkey  column_right
0   foo        1      foo          5
1   foo        1      foo          8
2   foo        5      foo          5

# 3) Join to multiple columns
new_df = pd.merge(df1, df2,
    how = 'left', 
    on = ['key1','key2',...])

# 4) joining on index 
new_df = pd.merge(
    df1, df2, 
    right_index=True, 
    left_index=True,) 

# 5) concat is same as union all 
new_df = pd.concat(df1, df2) 
```

## pd.loc
```py
# 1) Filter df based on condition: df[condition]
df[df['name'] == 'Andrew']

df[ 
    (df['acct_id'] == 1) & 
    (df['stmt_num'] >= 20)]

# 2) LOC: if column1 = xxx, column2 = yyy
df.loc[
    df["Column1"] = xxx, "Column2"] = "yyy" 

# 3) ILOC: select specific rows: df.iloc[row:col]
df.iloc[0:5, :] # first 5 rows 
df.iloc[:, 0]   # the first column, and all of the rows for the column

# 4) Condition on rows
pd.where(condition, value) # Where False, replace with corresponding value from other
pd.mask(condition, value) # Where True, replace with corresponding value from other
```

## pd.datetime
`to_datetime` converts a string column to a pandas datetime object:
```py
from datetime import datetime as dt

# 1) Convert a date column to datetime
df["Date"] = pd.to_datetime(df.Date)
df["Year-Month"] = df["Date"].apply(lambda x: x.strftime("%Y-%m"))

# 2) strftime() method takes timestamp and returns a formatted string
dt.now() # datetime.datetime(2022, 4, 29, 16, 18, 40, 491854)
dt.now().strftime("%Y-%m") # '2022-04'

# 3) groupby
df.groupby(["Year-Month"]).sum()
df.groupby(by=["b"], dropna=False).sum()
```

## pd.fillna
```py
# 1) Replace NA/NaN with value 0 
df.fillna( 
    value = 0, 
    inplace = True
    )

# 2) Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively.
values_dict = {
    "A": 0, 
    "B": 1, 
    "C": 2, 
    "D": 3,
    }
df.fillna(value = values_dict)

# 3) Drop the rows where at least one element is missing
df.dropna(
    inplace = True)

# Define in which columns to look for missing values
df.dropna(
    subset = ['name', 'toy']
    )

# Drop the rows where all elements are missing
df.dropna(
    how = "all")

# 4) Show which entries in a DataFrame are NA
df.isna()

# 5) Replace str None with NaN
df.replace(
    {None:np.nan}, 
    inplace = True,
    )

# 6) Count num of NaNs in a columns
df[col].isnull().sum() 

# Count num of NaNs in the entire df
df.isnull().sum().sum()
```
