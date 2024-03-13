## Difference in difference
- Analytical approach that facilitates **causal inference** even when randomization is not possible
- We cannot draw causal conclusions by observing simple before-and-after changes in outcomes
  - as factors other than the treatment may influence the outcome over time
- Difference-in-differences compare the before-and-after changes in outcomes for treatment and control groups
  - to estimate the overall impact of the program

### Implementation ⚙️
- 1st diff: before-after difference in treatment group’s outcomes
  - controls for factors that are constant over time in that group 
- 2nd diff: before-after difference in the control group to capture time-varying factors
  - which was exposed to the same set of environmental conditions as the treatment group
- impact estimation = 1st diff - 2nd diff
  - difference-in-differences “cleans” all time-varying factors from the first difference
  - by subtracting the second difference from it


### Others
- [Quasi-Experimental_Methods](https://dimewiki.worldbank.org/Quasi-Experimental_Methods)
