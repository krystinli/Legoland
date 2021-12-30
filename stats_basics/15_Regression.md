# Regression
**Linear Regression** is a linear approach to modeling the relationship between a dependent variable and one independent variable. 
- An **independent variable** is the variable that is controlled in a scientific experiment to test the effects on the dependent variable. 
- A **dependent variable** is the variable being measured in a scientific experiment.

<img src="https://miro.medium.com/max/4800/1*AevSOm4o9acS44_Aqg6tjQ.png" width=700 />

**Assumptions:**
- Linear Relationship
- Multivariate Normality
- No or Little Multicollinearity
- No or Little Autocorrelation
- Homoscedasticity

**Multiple Linear Regression** is a linear approach to modeling the relationship between a dependent variable and two or more independent variables.

<img src="https://miro.medium.com/max/4800/1*LTxPp0CKoj9NbaUzEkhEGg.png" width=600/>

### Steps for Running Linear Regression:
1. Understand the model description, causality and directionality
2. Check the data, categorical data, missing data and outliers. **Outlier** is a data point that differs significantly from other observations. We can use **standard deviation method** and **interquartile range(IQR)** method. **Dummy variable** takes only the value 0 or 1 to indicate the effect for categorical variables.
3. Simple Analysis — Check the effect comparing between dependent variable to independent variable and independent variable to independent variable
4. Multiple Linear Regression — Check the model and the correct variables
5. Residual Analysis - Check normal distribution and normality for the residuals. **Homoscedasticity** describes a situation in which error term is the same across all values of the independent variables and means that the residuals are equal across the regression line.
6. Interpretation of Regression Output. 

**Output:**
- **R-Squared** is a statistical measure of fit that indicates how much variation of a dependent variable is explained by the independent variables. Higher R-Squared value represents smaller differences between the observed data and fitted values.
- P-value
- Regression Equation

**Simple Analysis:** Use scatter plots to check the correlation
- **Multicollinearity** occurs when more than two independent variables are highly correlated. We can use **Variance Inflation Factor(VIF)** to measure if VIF > 5 there is highly correlated and if VIF > 10 there is certainly multicollinearity among the variables.
- **Interaction Term** imply a change in the slope from one value to another value.
