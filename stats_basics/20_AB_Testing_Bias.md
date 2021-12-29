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
If randomization unit between the variants is not close to the designed ratio, the experiment suffers from a Sample Ratio Mismatch. Examples:
- **Browser Redirect**: you should redirect both Treatment and Control so they're under the same set-up
- **Lossy Instrumentation**: not 100% of clicks are properly recorded and treatment sometimes skew the instrumentation 
- **Residual or carryover effects**: New experiments usually involve new code and the bug rate tends to be higher 
  - Run pre-experiment A/A tests and proactively re-randomize users 
  - Residual info in browser cookies can impact experiments   
- **Bad hash function for randomization**
- **Triggering impacted by treatment**: If triggering is done based on attributes changing over time, you need to make sure no attributes used for triggering could be impacted by the Treament. 
- **Time of day effects**: Time of sending emails to control vs. treatment can bias the outcome
- **Date pipeline imapcted by treatment**: Treament group triggers so much engagement that some users got classfied as bots and got filtered out 

### 6) External Validity
Refers to the extent to which the results of a controlled experiment can be generalized along axes such as diff populations (by country, websites, etc), and over time. 
- **Primary Effects**: 
- **Primary Effects**:

### Reference:
- [x] <Trustworthy Online Control Experiments> Chapter 3 - Twyman's Law and Experimentation Trustworthiness 