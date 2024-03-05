# What does "stat sig" mean? 🎯
Statistically significance means that a difference between 2 groups is NOT just due to chance 🥎
- When a result is stat-sig, we can be "confidence" that the difference is real ☑️
- ie. A marketing campaign ("treatment") to a sample results in a stat-sig +10% increase in conversion vs. the control group, we can be confident that this increase is due to the campaign effect, not just chance  

## 1) Stat-sig vs. P-Value 🧵
**Statistical significance is quantified in p-value**
- Q: How likely it is for the difference we see to occur under the the null hypothesis?
  - The H0 is the claim that an experimentally observed diff is due to chance alone => no real difference
  - The HA (contradicts H0) says that experimentally observed difference CANNOT be due to chance => T/C are different!

**We usually consider a `p-value < 0.05` to be stat-sig:**
- This means there's <5% chance the difference we observe is due to chance alone; hence we can reject H0; 
- This also means we might call a result stat-sig by mistabke 1 in 20 times!  
     
## 2) P-Value vs. alpha
- `H0 distribution`: a bell curve is an example probability distribution that shows all the possible values and their likelihood that a given varaible/metric can have
- Usually we want to be 95% sure a diff we observe is real (not due to chance)
- `1 - a` = 0.95, a = 0.05 is the significance level
- `p-value`: What is the probability that we observe this value given we assume the probabilty distribution is true?
  -  If `p < a`: the observed value is stat-sig since the chance of this observation being random is low;
  -  If `p > a`: the observed value is NOT stat-sig since this is likely due to chance!
