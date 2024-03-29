## Hypothesis Testing with Binomial Distribution 🧪
To hypothesis test with the binomial distribution, we must calculate the probability **p** of the observed event and any more extreme event happening:
- **Calculate probability of success under the null hypothesis:**
  - Determine the observed number of successes (X) in your sample: ie, getting 2 tail in 2 tosses;
  - Use the binomail probability formula to find the probability of observing X successes or more, => **p**
    - Given the sample size N and probability of success 0.5
- Compare p to sigificance level, ie  **α = 0.05**
  - If `p > α` then we **do not reject** the null hypothesis
  - If `p < α` then we **accept** the alternative hypothesis
- Exact formula for p-value depends on 1-tail / 2-tail test

## Example 🪙 [Coin Flipping](https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/statistics/hypothesis-testing/hypothesis-testing-with-the-binomial-distribution.html) 
A coin is tossed 20 times, landing on heads 6 times. 
- Perform a hypothesis test at a 5% significance level to see if the coin is biased:
  - `H0`: The coin is not biased (ie. This happens at random)
  - `H1`: The coin is biased in favour of tails (This is not random)

The important thing to note here is that we only need a: 
- **1-tailed** test as the alternative hypothesis says `in favour of tails`
- **2-tailed** test would be an alternative hypothesis saying `The coin is biased`

### 1) Cumulative Binomial Distribution
We need to calculate more than just the probability that it lands on heads 6 times. If it landed on heads fewer than 6 times, that would be even more evidence that the coin is biased in favour of tails. Consequently we need to add up the probability of it landing on heads 1 time, 2 times, … all the way up to 6 times.

Although a calculation is possible, it is much quicker to use the cumulative binomial distribution table.
- N = 20: sample size
- X = 6: num of success in sample
- p = 0.5: probability of 1 success
- P[X<=6] = 0.058: probability of observing 6 or less
- This gives `P[X<=6]=0.058` => Probability of landing < 6 heads with 20 tosses! 

<img width="456" alt="Screenshot 2024-02-22 at 12 54 23 AM" src="https://github.com/krystinli/Legoland/assets/33378140/bc9161e6-9db0-4a17-a821-3b0d6854fd59">

<img width="696" alt="Screenshot 2024-03-05 at 9 59 38 AM" src="https://github.com/krystinli/Legoland/assets/33378140/f6153784-17e9-4196-b7df-19742c6960ed">

### 2) Significance
We are asked to perform the test at a 5% significance level. This means,
- If there is less than 5% chance of getting <= 6 heads then it is so unlikely that we have sufficient evidence to claim the coin is biased in favour of tails
- Now note that our p-value of 0.058 > 0.05 so we do not reject the null hypothesis
- We don't have sufficient evidence to claim the coin is biased.

### 3) What if the coin had landed on heads 5 times? 
- N = 20, p = 0.5, C = 5
- P[X<5] = 0.021 => probability of observing 5 or less heads
- Since p < a, we can reject the null hypothesis and claims that **the coin is biased in favour of tails**!
- Since this is where we switch to accepting the althernative hypothesis, 5 is the **critical value**.

