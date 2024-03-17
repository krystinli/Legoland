## Logistic vs. Linear Regression 📈
Supervised Learning is when the algorithm learns on a **labeled dataset** and analyses the training data. These labeled data sets have inputs and expected outputs. [[KDD]](https://www.kdnuggets.com/2022/03/linear-logistic-regression-succinct-explanation.html#:~:text=Linear%20Regression%20and%20Logistic%20Regression,used%20to%20solve%20Classification%20problems.) 

<img width="400" src="https://github.com/krystinli/Legoland/assets/33378140/eb554f29-a8f9-4c03-b8e2-fa96931238ef" />

The relation between Linear vs Logistic Regression is the fact that:
- They both use labeled datasets to make predictions, but:
- **1) Linear Regression** is used to solve `regression problems`:
  - Predicting a **continuous** output
  - by finding the correlations between dependent and independent variables 
- **2) Logistic Regression** is used to solve `classification problems`:
  - Classification is about **predicting a label**
  - by identifying which category an object belongs to based on different parameters 

## 1) Linear Regression 🧵
Make predictions on _continuous_ dependent variables with the knowledge from independent variables:
- The goal is to find the best fitting line, to be used to predict the output Y (continuous dependent variables)
- Examples: house prices 🏚️, age 👵, and salary 💰
- Simple Linear Regression is a regression model that:
  - Estimates the relationship between 1 independent variable and 1 dependent variable using a straight line
  - Multiple Linear Regression: ff there are >2 independent variables
- Assuming linear relationship:
<img width="450" src="https://github.com/krystinli/Legoland/assets/33378140/f43bc917-98bc-47e3-b548-86bcde154b0e"/>

### Cost Function
A mathematical formula used to calculate the error:
- The difference between our predicted vs. actual value
- Measures how "wrong" the model with its ability to estimate the relationship between x and y
- For linear regression, cost function = MSE (root mean squared error)

<img width="300" src="https://www.kdnuggets.com/wp-content/uploads/arya_logistic_linear_regression_succinct_1.png" />

## 2) Classification 🪙
Make predictions on _categorical_ dependent variable with the knowledge of independent variables:
- Example: whether it will rain today or not, by using 0 or 1, yes or no, or true and false ☂️
- Logistic Regression: is based on Maximum Likelihood Estimation
  - A method of estimating the parameters of an assumed probability distribution given some observed data
- The overall aim of Logistic Regression is to classify outputs, which can only be between 0 and 1
- In Logistic Regression, the weighted sum of inputs is passed through an activation function
- called **Sigmoid Function:** <img width="150" src="https://www.kdnuggets.com/wp-content/uploads/arya_logistic_linear_regression_succinct_6.png" />
- which maps values between 0 and 1: <img width="300" src="https://github.com/krystinli/Legoland/assets/33378140/33a1421f-8da8-4fdb-bd53-d981c425ac1a" />

### Cost Function
- Cannot use MSE because our prediction function is non-linear (due to sigmoid transform)
- Therefore we use a cost function called Cross-Entropy, also known as **Log Loss**
- Cross-entropy measures the difference between two probability distributions for a given random variable:

![image](https://github.com/krystinli/Legoland/assets/33378140/4ae034f2-72b4-4da0-bc2f-423a36a680b8)

## 3) Linear vs Logistic Comparison



