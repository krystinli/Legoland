# Rolling Window Features 🪟
[[code]](https://github.com/patilvijay23/MLinPython/blob/main/pyspark/3_rolling_window_features.ipynb) | [medium](https://medium.com/analytics-vidhya/predictive-models-using-rolling-window-features-i-691172c19e95)
- Predict what will happen next, or what will happen in next N weeks 
- The model, and required features + dependent variable, needs to be designed to accommodate the relative time element

## Q: Which customers will make a purchase in next 4 weeks? 🛍️
Given past sales data for 2 years from Jan 2019 to Dec 2020:

![image](https://github.com/krystinli/Legoland/assets/33378140/c1efb735-9ed2-44ec-bce8-b890ec32f7f9)

### Step (1): Build a rolling window features dataset
Choose a **reference date** and then base everything to be relative to this date:
- The timeframe post the reference date will become the **target window**
  - to check whether a customer bought anything or not
- All activity prior to the reference date will be summarized to get **features** for the model
- The chosen reference date can induce it’s own biases into the dataset
  - Especially if there is seasonality to the variable we are trying to predict 

![image](https://github.com/krystinli/Legoland/assets/33378140/04e065b6-3fe2-432b-86d9-a0a04854b488)

We can choose multiple reference dates spread out over a year or two:
- We can also randomly sample from the 24 reference dates

![image](https://github.com/krystinli/Legoland/assets/33378140/c8107a78-1036-45ff-9cfb-fa791648e34f)

### Step (2): Target
Our target is to predict who will buy something in the next 4 weeks (1 or 0)
- For each `week_end`, we will create a flag variable that tells whether the customer bought something
- Then we can use the window definitions to agg the next 4 weeks relative to week_end
  - as the target variable for each week_end
- Similarly we will use the window definitions to agg various timeframes of the past year for all features



