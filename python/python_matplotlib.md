# matplotlib 📈
**Basics**
- 00_Prep
- 01_Plot
- 02_Labels
- 03_Output

**Advances**
- [Date_Tick_Labels]()

---------------------

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

# Equivalanet plot
ax.plot(
    data.index, # x-axis
    data.Work,  # y-axis
    linewidth = 1,
    marker = 'o',
    markersize = 8,
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

![image](https://user-images.githubusercontent.com/33378140/176675843-3fb21bed-3376-4a62-b2a4-5a0347c7396b.png)

## Date_Tick_Labels
### 00_Prep
Build a canvas for the plot
```py
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

# Start the canvas 
fig, axs = plt.subplots(
    3, 1, # 3 rows 1 column
    figsize = (6.4, 7),  
    constrained_layout = True
)
```

### 01_Plot
```py
# Basic plot: common to all three:
for ax in axs:
    ax.plot(
        "date",      # x-axis column
        "adj_close", # y-axis column
        data = data, # data
    )
    # Major ticks every half year, minor ticks every month,
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    
    # Labelling
    ax.grid(True)
    ax.set_ylabel(r"Price [\$]")
```

### 02_Labels
Different formats for each plot
```py
# Plot 1
ax = axs[0]
ax.set_title(
    'DefaultFormatter', 
    loc='left', 
    y=0.85, 
    x=0.02, 
    fontsize='medium'
)

# Plot 2
ax = axs[1]
ax.set_title(
    'ConciseFormatter', 
    loc='left', 
    y=0.85, 
    x=0.02, f
    ontsize='medium'
)
ax.xaxis.set_major_formatter(
    mdates.ConciseDateFormatter(
        ax.xaxis.get_major_locator()
        ))

# Plot 3
ax = axs[2]
ax.set_title(
    'Manual DateFormatter', 
    loc='left', 
    y=0.85, 
    x=0.02,
    fontsize='medium'
    )
    
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(
    mdates.DateFormatter('%Y-%b'))

# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```

