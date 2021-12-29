## P-value 🔢 
> Given the null hypothesis is true, p-value is the probability of obtaining results at least as extreme as the observed results of a statistical hypothesis test.

A p-value is a measure of the probability that an observed difference could have occurred just by random chance.
- The **lower the p-value, the greater the statistical significance** of the observed difference
  - So the stronger the evidence that you should reject the null hypothesis.
  
In a hypothesis test:
- The null **hypothesis H0 is rejected** if: 
  - **α - significance level** - a pre-defined threshold value
  - While `p-value ≤ α`, we reject the null hypothesis and we can conclude that we have the significant result.
- For example, a p value of `0.0254` is `2.54%`: (would be < 0.05, or 5% critical value) 
  - This means there is a 2.54% chance your results could happened by chance.

### 01_How Is P-Value Calculated?
- Base on assumed probability distribution of the specific statistic being tested, p-values are usually found using p-value tables or spreadsheets/statistical software.
- Mathematically, the p-value is calculated using integral calculus from the area under the probability distribution curve for all values of statistics that are at least as far from the reference value as the observed value is, relative to the total area under the probability distribution curve.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/P-value_in_statistical_significance_testing.svg/741px-P-value_in_statistical_significance_testing.svg.png" width=450 />

Consider an observed test-statistic t from unknown distribution T:
- p-value p is what the prior probability would be of observing a test-statistic value at least as "extreme" as t if null hypothesis H0 were true
  - `p = Pr(T>t|H0)` for a one-sided right-tail test
  - `p = Pr(T<t|H0)` for a one-sided left-tail test 
  - `p = {Pr(T>t|H0), Pr(T<t|H0)}` for a two-sided test

### References
- [x] [P-value Explained Simply for Data Scientists](https://towardsdatascience.com/p-value-explained-simply-for-data-scientists-4c0cd7044f14)
- [x] [How to interpret p-value with COVID-19 data?](https://towardsdatascience.com/how-to-interpret-p-value-with-covid-19-data-edc19e8483b)

Hypothesis_Testing 
- **Null Hypothesis - H0:** A general statement that there is no association among groups. 
- **Alternative Hypothesis - Ha:** Be contrary to the null hypothesis.