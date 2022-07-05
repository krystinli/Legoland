# Common_Functions

```sql
-- Syntax recap

-- 1) window function 
ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...) as row_num -- does NOT re-rank duplicated values 
SUM(daily_sales) OVER (order by date_) as rolling_sum -- cumulative sum 
FIRST_VALUE(col_name) OVER (PARTITION BY ... ORDER BY ...) as col_name -- does NOT dedup, need to sel distinct 

-- 2) dates
YEAR(ts) # '2021'
datepart(hour, order_created_at) # get the hour from timestamp
date_format(date_column, '%Y-%m') # '2020-10'
date_format(date_column, '%Y-%m-%d') # '2020-10-12'

-- 3) timestampdiff
SET @date1 = '2010-10-10 00:00:00', @date2 = '2010-10-10 23:59:59';
SELECT 
  DATEDIFF(@date1, @date2) AS 'DATEDIFF',
  TIMESTAMPDIFF(day, @date1, @date2) AS 'Days',
  TIMESTAMPDIFF(hour, @date1, @date2) AS 'Hours',
  TIMESTAMPDIFF(minute, @date1, @date2) AS 'Minutes',
  TIMESTAMPDIFF(second, @date1, @date2) AS 'Seconds'
  
+----------+------+-------+---------+---------+--------------+
| DATEDIFF | Days | Hours | Minutes | Seconds | Microseconds |
+----------+------+-------+---------+---------+--------------+
|        0 |    0 |    23 |    1439 |   86399 |  86399000000 |
+----------+------+-------+---------+---------+--------------+
```
