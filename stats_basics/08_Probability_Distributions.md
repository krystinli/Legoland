# Probability Distributions 📉 📈
1. Uniform Distribution `discrete`
2. Bernoulli Distribution `discrete`
3. Binomial Distribution `discrete`
4. Poisson Distribution `discrete`
5. Normal/Gaussian Distribution `continuous`
6. Exponential Distribution `continuous`
7. Chi-Square Distribution `continuous`

### 1) Uniform Distribution 🌟🌟🌟🌟
- All the outcomes are equally likely 🏋️‍♀️
- **Example:**
  - Consider the case of rolling a fair dice 🔢
  - Which can take any of the 6 possible values and all the values are *equally likely* 
  - The probability of any of the values is going to be `1/6`
  - The random variable can only take the value `1/6`
- We call such a random variable as the **uniform random variable**
- And its distribution is a **uniform distribution**  

<img src="https://miro.medium.com/max/1400/1*xa9Ar0oeTBlBTBF1a9ZTmA.png" width=400 /> <img src="https://miro.medium.com/max/1400/1*3viqmdluumhCiwiA2wM_DA.png" width=500 /> 

<img src="https://miro.medium.com/max/1400/1*lc7FIFFydtK_xSNEML2USQ.png" width=400 />

**In general:**
- `Rx = {x: a <= x <= b}`
- `E(X) = (a + b) / 2` the midpoint of the distribution 
  - a - min
  - b - max 
- The term in the denominator ‘b-a+1’ gives the number of elements between ‘a’ and ‘b’ as per the counting principle
  - Mean = Median: `(a + b) / 2`
  - Mode: any value between a and b
  - Skeness: 0 

<img src="https://miro.medium.com/max/1332/1*3PCTi-tyCCeUSoiXVw2B0A.png" width=400 />

### 2) Bernoulli Distribution 
<img src="https://miro.medium.com/max/1400/1*AbT3n4wrT2ldWPFZj_77Yg.png" width=400 />

**In general:**
- `E(X) = p`
- Variance: `p(1-p)`
- Only 2 possible outcomes: 
  - namely 1(success) with probability p
  - and 0(failure) with probability (1-p).

<img src="https://miro.medium.com/max/1400/1*0hPAexOgWAzOuCdyIxp8Rg.png" width=300 /> <img src="https://miro.medium.com/max/1400/1*RYylA-UwmjocxRp6VnTCrg.png" width=400 />

### 3) Binomial Distribution
The distribution of the number of successes in a sequence of n independent experiments, and each with only 2 possible outcomes: 
- namely 1(success) with probability p
- and 0(failure) with probability (1-p)
  - Expectation: `E(X) = np`
  - Variance: `np(1-p)`

**Probability Mass Function:**
- X: random variable indicating the num of success in n trials 
- Px(k): What's the probability of k success in n trials? 

<img src="https://miro.medium.com/max/1400/1*DSFk4sMwKdP-SR1dPF6xVA.png" width=400 />

**Cumulative Distribution Function:** <br />
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8689ba703ee51a5f66f605ea1f293fc74fa380b9" width=400 />

**Example:** Tossing a coin ‘n’ times 🪙
- These ‘n’ trials are independent which means that the success/failure of one trial does not affect the result of another trial.
- These ‘n’ trials are identical meaning the probability of success in each trial is the same

```
Q1. Suppose 10% of your co-workers infected, you contact 50 of them, what's the chance of you getting infected?
- Px(k>0)
- = 1- Px(k=0)=1- 50C0 * 0.1^0 * 0.9^50 = 1- 0.005 = 0.9948

Q2. What if you only interact with 10 out of 50 people?
- Px(k>0)
- = 1- Px(k=0)=1- 10C0 * 0.1^0 * 0.9^10 = 0.6513
```

### 4) Poisson Distribution 
The distribution that expresses the probability of 
- A given number of events k 
- Occurring in a fixed interval of time 
- If these events occur with a known constant average rate λ 
- Independently of the time.
  - Mean: λ 
  - Var: λ 

Probability mass function:
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/6c429d187b5d4ef8ddea32a2d224f423cf9fe5b0" width=200 />
- k is the number of occurrences ({\displaystyle k=0,1,2...}{\displaystyle k=0,1,2...})
- e is Euler's number ({\displaystyle e=2.71828...}e = 2.71828...)

**Examples:**
- The number of patients arriving in an emergency room between 10 and 11 pm
- On a particular river, overflow floods occur once every 100 years on average. Calculate the probability of k = 0, 1, 2, 3, 4, 5, or 6 overflow floods in a 100-year interval, assuming the Poisson model is appropriate.
  - Because the average event rate is one overflow flood per 100 years, λ = 1
 
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/56ecb437f5dc2d6fdd04104dd682909feab34802" width=400/>

**Comparison** <br />
<img src="https://miro.medium.com/max/4800/1*YVOAif6t_4Fzjfho1iLldQ.png" width=750/>

<br />

--------------

`Continuous_Probability_Distribution`

### 5) Normal/Gaussian Distribution
- The curve of the distribution is bell-shaped and symmetrical 
- Related to the Central Limit Theorem that the sampling distribution of the sample means approaches a normal distribution as the sample size gets larger. 

<img src="https://miro.medium.com/max/1400/1*TMdOva_Y1GAFlE7ELAq6zA.png" width=600 />

<img src="https://miro.medium.com/max/2000/1*5UVQaCmIwzlpYyeJEMXNhQ.png" />

### 6) Exponential Distribution 
A probability distribution of the time between the events in a Poisson point process.

### 7) Chi-Square Distribution
The distribution of the sum of squared standard normal deviates.

<img src="https://miro.medium.com/max/1400/1*C3kv6PpeNyTCQCTKXD0w9Q.png" width=700/>

**Functions**
- **Probability Mass Function(PMF):** A function that gives the probability that a discrete random variable is exactly equal to some value.
- **Probability Density Function(PDF):** A function for continuous data where the value at any given sample can be interpreted as providing a relative likelihood that the value of the random variable would equal that sample.
- **Cumulative Density Function(CDF):** A function that gives the probability that a random variable is less than or equal to a certain value.

Comparison between PMF, PDF and CDF: <br />
<img src="https://miro.medium.com/max/1400/1*ktIttLCFRAqdUlLE180v9g.png" width=500 />
