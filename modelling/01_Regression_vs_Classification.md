## Logistic vs. Linear Regression 📈
Supervised Learning is when the algorithm learns on a **labeled dataset** and analyses the training data. These labeled data sets have inputs and expected outputs. [[KDD]](https://www.kdnuggets.com/2022/03/linear-logistic-regression-succinct-explanation.html#:~:text=Linear%20Regression%20and%20Logistic%20Regression,used%20to%20solve%20Classification%20problems.) 

<img width="450" src="https://github.com/krystinli/Legoland/assets/33378140/eb554f29-a8f9-4c03-b8e2-fa96931238ef" />

The relation between Linear vs Logistic Regression is the fact that:
- They both use labeled datasets to make predictions, but:
- **1) Linear Regression** is used to solve `regression problems`:
  - Predicting a **continuous** output
  - by finding the correlations between dependent and independent variables 
- **2) Logistic Regression** is used to solve `classification problems`:
  - Classification is about **predicting a label**
  - by identifying which category an object belongs to based on different parameters 

## 1) Regression
Make predictions on continuous dependent variables with the knowledge from independent variables:
- The goal is to find the best fitting line, to be used to predict the output Y (continuous dependent variables)
- Examples: house prices 🏚️, age 👵, and salary 💰
- Simple Linear Regression is a regression model that:
  - Estimates the relationship between 1 independent variable and 1 dependent variable using a straight line
  - Multiple Linear Regression: ff there are >2 independent variables
- Assuming linear relationship

## 2) Classification
