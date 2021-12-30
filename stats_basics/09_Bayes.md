## Conditional_Probability
**Conditional Probability** is the likelihood of an outcome occuring basd on previous outcome occuring 
- `P(A|B)=P(A∩B)/P(B)`
- `P(A∩B)=P(B|A).P(A)`

**Bayes’ Theorem**: 🌟🌟🌟🌟🌟
- Describes the probability of an event based on prior knowledge of conditions that might be related to the event
- It provides a way to revise existing predictions or update probability given new additional avidence 

<img src="https://miro.medium.com/max/1400/1*LnJh6KyCUcbgZG6Mslwj0Q.png" width=700 />

### Example_01 🤧
A doctor performs a test with 99% reliability -> 99% of people who are sick test positive and 99% of healthy people test negative. Only 1% of the people in the country are sick. If the patient test positive, what're the chance of patient being sick?

**Answer:** 
```
- P(A) = Patient being sick = = 0.01
- P(B|A) = 0.99
- P(B) = Patient test positive = 0.99x0.01 (sick people test positive) + 0.99x0.01 (healthy people test positive)
- P(A|B) = P(B|A).P(A) / P(B) = 0.99x0.01 / 0.99x0.02 = 0.5
```

### Example_02 ⛈️
You're head to Seattle. You want to know if you should bring an umbrella so you call 3 random friend who live there and ask each independently whether it's raining or not. Each friend has a 2/3 chance of telling the truth and 1/3 chance of lying. All 3 friends tell you "yes it's raining". What's the probability of Seattle actually rain?
- Hint: the chance of truth is a compounded probability since it relies on all of 3 people's combined responses 

**Answer:** 
```
- P(A) chance of rain - we need to come up with an assumption, say 25%
- P(B) chance of truth - 2/3
- P(A|B) = P(B|A).P(A) / P(B) = (2/3)^3.(0.25) / (2/3)^3.(0.25) + (1/3)^3.(0.75) = 72.7%
```

### Example_03 🏀
Bag I contains 4 white and 6 black balls while Bag II contains 4 white and 3 black balls. One ball is drawn at random from 1 of the bags, and it is found to be black. Find the probability that it was from Bag I.

**Answer:** 
```
- P(A) chance of Bag1 = 0.5 (chance of choosing 1 bag out of 2 is 50/50)
- P(B) chance of Black
- P(A|B) = P(B|A).P(A) / P(B) = 0.6 x 0.5 / 0.6 x 0.5 + 0.5 x 3/7 = 7/12
```

### Example_04
Tom takes a cancer test and the test is advertised as being 99% accurate: if you have cancer you will test positive 99% of the time, and if you don't have cancer, you will test negative 99% of the time. If 1% of all people have cancer and Tom tests positive, what is the prob that Tom has the disease? 

