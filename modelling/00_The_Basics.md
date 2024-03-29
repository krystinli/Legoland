## The_Basics 👶
ML is the science of making computers learn without programming them explicitly. For example, Netflex recommendation system predicts user's preference for movies based on past ratings.

## Supervised Learning
The goals is to learn a general rule or function that maps inputs to outputs. The function is general enough and we try to minimize some err metrics on a held-out dataset. 

****Examples:****
- [ ] Regression: target variable is continuous 
- [ ] Logistic regression
- [ ] Support vecotr machines
- [ ] Neural networks
- [ ] Decision trees, random forests, and gradient boosted machines
- [ ] Classification: target variable (output) is categorial (ie. Y or N)
 
## Unsupervised Learning
Learner is provided with a set of inputs **but no output**❗ 
- With the goal of finding structure in the input, such as clustering (putting inputs in categories) 
- Since observations do NOT come with targets, we cannot preform regression or classification
- The goal is to find intrinsic structure in the data by identifying similarities btw observations 

**Examples:**
- [ ] Clustering
- [ ] K-means clusters
- [ ] Mixture models,
- [ ] The expectation maximization algorithm 

## Reinforcement Learning
The learner interacts with the environment by taking certain actions. The environment reacts with a reward or punshiment for each action.The goal is to maximize the long-term reward, ie. AlphaGo. 
- The learner interacts with the environment by performing certain actions and learn based on the feedbacks received
- The feedback is in the form of rewards or punishments, and the goal is the maximize long-term rewards
- A move that generates immediate reward may not be the best move in the long-term
- Reinforcement learning is usedful in A/B testing, marketing, and robot control 

