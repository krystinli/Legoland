# Rolling Window Features 🪟
- Predict what will happen next, or what will happen in next N weeks [medium](https://medium.com/analytics-vidhya/predictive-models-using-rolling-window-features-i-691172c19e95)
- The model, and required features + dependent variable, needs to be designed to accommodate the relative time element

## Q: Which customers will make a purchase in next 4 weeks? 🛍️
Given past sales data for 2 years from Jan 2019 to Dec 2020:

![image](https://github.com/krystinli/Legoland/assets/33378140/c1efb735-9ed2-44ec-bce8-b890ec32f7f9)

### Step (1): test/train split 🚋
Choose a **reference date** and then base everything to be relative to this date:
- The timeframe post the reference date will become the **target window**
  - to check whether a customer bought anything or not
- All activity prior to the reference date will be summarized to get **features** for the model

![image](https://github.com/krystinli/Legoland/assets/33378140/04e065b6-3fe2-432b-86d9-a0a04854b488)
