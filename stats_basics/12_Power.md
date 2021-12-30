# Power
Power is the probability of correctly rejecting the null hypothesis. As your sample size increases, so does the power of your test.
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

### Questions
**If decrease the effect size by half, how to adjust sample size to achieve the same statistical power, assume standard deviation remains the same?**
- 4 times, 1.05 * 1.05
