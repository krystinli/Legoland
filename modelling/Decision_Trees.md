# Decision Trees 🌳
Are used for residual modeling (ReMo): 
- we fit a tree to the residuals for another model 
- and identify features that're important in modeling those residuals 
- **Residual**: diff btw model prediction and true value 
- basis for **Random Forests** (RF) and **Gradient Boosted Machines** (GBM)

## Pros
- Interpretable: easy to interprete the relative importance of various attributes
- Non-parametirc: the relationship btw `x` and `y` might be too complex to be captured by a parametric function
- Robust to missing attributes: no need to impute the missing variables in R but still need in Scikitlearn
- No need for feature scaling or normalizing the data
- Computational efficient to score
- Form the basis for more advanced method such as RF and GBM

## Classification Trees
- When decision trees are used for classification, it is common to refer to as **classification trees**
- When used for regression, they are referred to as **regression trees**
- Look at Iris Data, a popular benchmark set, and apply classification trees to that data
- Learn how to visualize trees and determine the relative importance of various features
- Understand the type of decision boundary that a classification tree is capable of generating
- Learn what overfitting is and how to avoid it
- How to select the right values for the various parameters? For example, what should be the maximum height?
- Use a classification tree to predict charge-off of customers
