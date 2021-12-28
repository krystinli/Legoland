## Hypothesis_Testing 
- **Null Hypothesis - H0:** A general statement that there is no association among groups. 
- **Alternative Hypothesis - Ha:** Be contrary to the null hypothesis.

### P-value
The probability of the test statistic being at least as extreme as the one observed given that the null hypothesis is true. 
- It's a measure of the probability that an observed difference could have occurred just by random chance.
  - When `p-value > α`, we fail to reject the null hypothesis
  - While `p-value ≤ α`, we reject the null hypothesis and we can conclude that we have the significant result.
- The **lower the p-value, the greater the statistical significance** of the observed difference
  - So the stronger the evidence that you should reject the null hypothesis.

In a formal significance test: 
- The null **hypothesis H0 is rejected** if 
  - The **p-value <** a pre-defined threshold value **a - significance level**
- For example, a p value of `0.0254` is `2.54%`: (would be < 0.05, or 5% critical value) 
  - This means there is a 2.54% chance your results could be random (i.e. happened by chance)

Consider an observed test-statistic t from unknown distribution T:
- p-value p is what the prior probability would be of observing a test-statistic value at least as "extreme" as t if null hypothesis H0 were true
  - `p = Pr(T>t|H0)` for a one-sided right-tail test
  - `p = Pr(T<t|H0)` for a one-sided left-tail test 
  - `p = {Pr(T>t|H0), Pr(T<t|H0)}` for a two-sided test
