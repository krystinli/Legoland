# Power
- [01_significance_level_and_rejection_region](https://github.com/krystinli/Legoland/blob/main/stats_basics/13_Power.md#01_significance_level_and_rejection_region)
- [02_critical_value](https://github.com/krystinli/Legoland/blob/main/stats_basics/13_Power.md#02_critical_value)
- [03_error](https://github.com/krystinli/Legoland/blob/main/stats_basics/13_Power.md#03_error)

The power of a test is the probability of correctly rejecting the null hypothesis. As your sample size increases, so does the power of your test.
- This should intuitively make sense as a larger sample means that you have collected more information -- which makes it easier to correctly reject the null hypothesis when you should.
- To ensure that your sample size is big enough, you will need to conduct a power analysis calculation, which require:
  - What type of test you plan to use (e.g., independent t-test, paired t-test, ANOVA, regression, ...)
  - The alpha value or significance level you are using (usually 0.01 or 0.05)
  - The expected effect size
  - The sample size you are planning to use

AB test: 
- Group A, group B, there is a 5% lift in group B relative to group A (B = A + 5%)
- Run another AB test, group B, group C, there is a 5% lift in group C relative to group B (C = B + 5%)
- Then what's the lift in group C relative to group A. (C should be 10% higher than group A) 

### 01_Significance_Level_and_Rejection_Region
- The rejection region depends on the significance level. 
- The significance level is denoted by α and is the probability of rejecting the null hypothesis if it is true. 

### 02_Critical_Value
A point on the scale of the test statistic beyond which we reject the null hypothesis
- Derived from the level of significance α of the test
- It depends upon a test statistic, which is specific to the type of test
- The significance level, α, defines the sensitivity of the test

### 03_Error
- **Type I error** is the rejection of a true null hypothesis
- **Type II error** is the non-rejection of a false null hypothesis.

<img src="https://miro.medium.com/max/4800/1*vpRxfDM8MHLtfTrO7Sx3zQ.png" width=800 />

<br />

### Questions
**Q1: If decrease the effect size by half, how to adjust sample size to achieve the same statistical power, assume standard deviation remains the same?**
- 4 times, 1.05 * 1.05
