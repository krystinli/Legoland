# Hypothesis Testing with Binomial Dist 🔢
To hypothesis test with the binomial distribution, we must calculate the probability **p** of the observed event and any more extreme event happening. We compare this to the level of significance **α**:
- If `p > α` then we **do not reject** the null hypothesis
- If `p < α` then we **accept** the alternative hypothesis

## Coin Flipping 🪙
A coin is tossed 20 times, landing on heads 6 times. Perform a hypothesis test at a 5% significance level to see if the coin is biased:
- `H0`: The coin is not biased (ie. This happens at random)
- `H1`: The coin is biased in favour of tails (This is not random)

The important thing to note here is that we only need a **one-tailed** test as the alternative hypothesis says “in favour of tails”. A **two-tailed** test would be the result of an alternative hypothesis saying “The coin is biased”.

### Cumulative Binomial Distribution
We need to calculate more than just the probability that it lands on heads 6 times. If it landed on heads fewer than 6 times, that would be even more evidence that the coin is biased in favour of tails. Consequently we need to add up the probability of it landing on heads 1 time, 2 times, … all the way up to 6 times.

Although a calculation is possible, it is much quicker to use the cumulative binomial distribution table.<img width="456" alt="Screenshot 2024-02-22 at 12 54 23 AM" src="https://github.com/krystinli/Legoland/assets/33378140/bc9161e6-9db0-4a17-a821-3b0d6854fd59">
- This gives `P[X<=6]=0.058` => Probability of landing < 6 heads with 20 tosses

### Significance
We are asked to perform the test at a 5% significance level. This means,
- If there is less than 5% chance of getting <= 6 heads then it is so unlikely that we have sufficient evidence to claim the coin is biased in favour of tails
- Now note that our p-value of 0.058 > 0.05 so we do not reject the null hypothesis
- We don't have sufficient evidence to claim the coin is biased.

## Q: What if the coin had landed on heads just 5 times? 


