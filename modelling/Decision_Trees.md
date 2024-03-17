# Decision Trees 🌳
Are used for residual modeling (ReMo): 
- we fit a tree to the residuals for another model 
- and identify features that're important in modeling those residuals 
- **Residual**: diff btw model prediction and true value 
- basis for **Random Forests** (RF) and **Gradient Boosted Machines** (GBM)

**Why?**
- Interpretable: easy to interprete the relative importance of various attributes
- Non-parametirc: the relationship btw `x` and `y` might be too complex to be captured by a parametric function
- Robust to missing attributes: no need to impute the missing variables in R but still need in Scikitlearn
- No need for feature scaling or normalizing the data
- Computational efficient to score
- Form the basis for more advanced method such as RF and GBM

**Extensions**
- When decision trees are used for classification, it is common to refer to as **classification trees**
- When used for regression, they are referred to as **regression trees**
- Look at Iris Data, a popular benchmark set, and apply classification trees to that data
- Learn how to visualize trees and determine the relative importance of various features
- Understand the type of decision boundary that a classification tree is capable of generating
- Learn what overfitting is and how to avoid it
- How to select the right values for the various parameters? For example, what should be the maximum height?
- Use a classification tree to predict charge-off of customers

### Classification w/ Decision Tree
- Height of a tree: longest node of the tree
- Depht of a tree: height - 1
- `stump`: a tree with depht = 2, just root and children
- Pure: all points of a subset belongs to the same class - we do not split pure nodes anymore
- If the leave (end-node) is impure: we assign a weight on each class given the mixture of nodes 
- There's no guarantee a local decision will lead to a global optimal tree
  - one that best models the relationship between the attributes and the target


