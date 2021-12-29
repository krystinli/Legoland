## AB Testing Bias 🔍

### 1) Lack of Statistical Power
Just because you cannot reject the null hypothesis, doesn't mean the alternative hypothesis is not true. 
- The experiment can be underpowered to detect the effect size we're seeing (not enough users in the test group) 
- If an experiement only impact a small subset of population, we should analyze only the impacted subset. A large impact on a small set of users can be diluted and not be detectable overall.  

### 2) Multiple Hypothesis Test
Running multiple experiements can pick the lowest p-value is considered cheating. The same thing can be done by running multiple iterations of the same experiement, looking at p-value across time, looking at a specific segment/metric, etc. These are all considered gaming the p-value, which introduced bias. 

### 3) Threats to Internal Validity
- Network effect or spill over between control and treatment groups
- 2-sided marketplaces (such as ad auctions, Airbnb, Uber) can containminate the users on the other side of the market. 
- Share resouces (like CPU, Storage, caches) can cause process to slow down and possibly swapping resources to disk, all variants suffer. 

### 4) Selection Bias
- Survivorship Bias: Analyzing users who have been active for sometime introduces suvivorship bias. 
- Intention-to-Treat: non-random attrition from the variants 
  - Intention-to-treat uses the initial assginment, whether it was executed or not. The treatment effect we're measuring is therefore based on the offer, or intention to treat, not whehter it was actually applied.  

### 5) Sample Ratio Mismatch
If randomization unit between the variants is not close to the designed ratio, the experiment suffers from a Sample Ratio Mismatch. 
