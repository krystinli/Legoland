# Simpsons_Paradox 
Occurs when we observe a certain trend in the aggregate data but not in the underlying segments that comprise the data. [post](https://medium.com/swlh/how-simpsons-paradox-could-impact-a-b-tests-4d00a95b989b) 
- For AB testing, Simpson’s Paradox can occur when the overall mean conversion rate to a result 
- Different from the mean conversion rates of the underlying segments. 

## 00_What causes Simpson’s Paradox? 🧙‍♀️
Essentially caused by `weighted averages`:
- When we combine the results by traffic sources 
  - The **dominant traffic source** for each of the variants heavily influences the **aggregate conversion rates**
  - Thereby switching the direction of the results
  - The traffic source volume is **unevenly distributed** between the experiences and is in fact responsible for the observed results
- This can easily move our test dangerously close to comparing apples to oranges.

## 01_How to avoid it?
`Action 1`: The samples are **completely randomized** and free from bias
- Ensure that the **distribution of visitors from different traffic** sources, browsers etc is comparable across the experiences
  - A visitor coming to the page is equally likely to see any of the experiences.  
- The underlying differences in conversion rates do not unequally impact one experience more than the other

`Action 2`: Segment the experiences based on traffic sources, devices, browsers etc.
- Make sure that there are no confounding factors at play.

`Action 3`: If you are concerned about the impact of the test on website conversions:
- **Do NOT change the traffic allocation** between the experiences after starting the test
- You may want to allocate a lower % of traffic to the test to start with
- Based on the stability and performance of the test, you can then increase the traffic to 100%.
- Should you absolutely need to start a test with different traffic allocation between experiences for any reason, start a new test when you are actually ready to test.

`Action 4`: **Stratified Sampling**
- The process of dividing members of the population into homogeneous and mutually exclusive subgroups before sampling

In general:
- The decision on whether to act on the aggregate or on the by segment data is up to the story behind the numbers, not the numbers themselves
- Evaluate each pair of **confounding variable** and experience qualitatively
- We could treat each pair as a separate experience and perform some additional testing 
  - Until we reach the desired statistically significant result for each pair

### Case 1 - Split Channels 👨‍🔧
**Suppose you run an A/B test between Page A and Page B and see the following results:**
<img src="https://miro.medium.com/max/1400/1*yybF-lwyCEkxQxzys_SnjQ.png" width=700 />

Looking at the average conversion rate: 
- You have a conclusive test with B beating A:
- Assuming the sample size requirements, other conditions such as statistical significance and power

<br />

**When you segment the data by the different traffic sources:**
<img src="https://miro.medium.com/max/1400/1*cjGUyNQOIYkVkQjLZcpuDA.png" width=700 />

<br />

### Case 2 - Ramping Up ⤵️
Occurs when the traffic allocation between experiences is changed

**Microsoft Example**
A website got one million daily visitors, on both Friday and Saturday
- On Friday, 1% of the traffic was assigned to the treatment (i.e. the variation)
- On Saturday that percentage was raised to 50%.

Even though the treatment had a higher conversion rate than the Control 
- On both Friday (2.30% vs. 2.02%)
- And Saturday (1.2% vs. 1.00%)
- When the data was combined over the two days, the treatment seemed to underperform (1.20% vs. 1.68%)

**Simpson’s Paradox due to change in traffic allocation between experiences:**
<img src="https://miro.medium.com/max/1400/1*vrqqF0eMail94iu1cV2V2A.png" width=700 />

This is again because we are dealing with weighted averages:
- The data from Saturday, a day with an overall worse conversion rate
- Impacted the treatment more than that from Friday.
