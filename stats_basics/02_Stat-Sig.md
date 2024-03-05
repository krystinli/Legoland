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

## 3) One or Two Tail 🍸
Looking for stat-sig in 1 direction is a one-tail test:
- We allot all a in one direction
- while completely ignoring the possibility that the effect could be in the other direction
- It's easier to reach stat-sig

If we care NOT only about whether a treatment increase a metric, but also whether it decreases a metric:
- When we apply a treatment to a sample, we hope for a + result but we don't know for sure
- We're looking at any change, not just increase or decrease
- Hence, a (0,05) is split in half, at both ends of the distribution
- This means we need to observe a more positive (top 2.5%) or more negative (bottom 2.5%) value to declare stat-sig
- It's harder to reach stat-sig, but more applicable to business, as most treatment can go both ways 

## 4) Alpha & Beta 🐛
Alpha, a is the probability of a false positive, or Type I Error
- Alpha: The probability we reject H0 when it's in fact, a true false positive => Type I Error
- Beta: Probability we couldn't reject H0 when there's a real diff, a false negative => Type II Error
- Power: 1 - beta => greater power, smaller beta, more likely to reject H0 when observed diff not due to chance! 



