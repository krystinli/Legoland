## matplotlib 📈

### 00_Canvas
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
    "Work",
    data = data,
    linewidth = 1,
    marker = 'o',
    markersize = 8,
)
```

