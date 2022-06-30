# matplotlib 📈
- 00_Prep
- 01_Plot
- 02_Labels
- 03_Output

### 00_Prep
Build a canvas for the plot
```py
import matplotlib.pyplot as plt

# Set time column as index for time series plot
data.Date = pd.to_datetime(data.Date)
data.set_index("Date", inplace=True)

# Start the canvas 
fig, ax = plt.subplots()
fig.set_size_inches(18, 5) # img size
```

### 01_Plot
```py
# Basic plot
ax.plot(
    "Work",      # y-axis column 
    data = data, # dataframe with pre-specified index as the x-axis
)

# With parameters
ax.plot(
    colname,
    data = data,
    color = "black",
    linewidth = 1,
    marker = 'o',
    markeredgecolor = color,
    markersize = 8,
)

# Stacked bars
df.plot(
    x = "Week of the Month",
    y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    kind = "bar",
    figsize = (18,8),
    title = "May Workout Breakdown Analysis",
    stacked = True,
    legend = True,
    colormap = "Pastel1" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
)
```

### 02_Labels
```py
ax.set(
    xlabel = "Date",
    ylabel = "Work",
    title = "Work Plot",
)

# In case yaxis no in the right order
plt.gca().invert_yaxis()

# target line
plt.axhline(y=target_low, c='black', linestyle='--', linewidth=2)

plt.legend()
```

### 03_Output
```py
plt.show()
plt.savefig("img/" + "work_trend" + ".png")

```


