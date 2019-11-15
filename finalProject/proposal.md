## Title: Energy and demographics, how do we use it?
## Data: https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households
## Description
Smart meter readings from the United Kingdom over a three year period (2011 to 2014) at half hour intervals. What this means is that from ~5500 households we have total energy draw / usage at 30 minute intervals. They were "recruited as a balanced sample representative of the Greater London population". There are two types of groups, those under dynamic time of use pricing and others under static pricing. The main objective of this data collection process to understand how users of various demographics respond to dynamic pricing compared to static pricing. "The signals given were designed to be representative of the types of signal that may be used in the future to manage both high renewable generation ... and also test the potential to use high price signals to reduce stress on local distribution grids during periods of stress"

## Motivation / Problem Statement
I have always been fascinated by energy consumption, starting back to the [energy dis-aggregation task](https://web.stanford.edu/group/peec/cgi-bin/docs/events/2011/becc/presentations/3%20Disaggregation%20The%20Holy%20Grail%20-%20Carrie%20Armel.pdf) that I helped do some research in during [my undergrad](https://aaai.org/ojs/index.php/AAAI/article/view/3872). It would be interesting to try similar work on this data. However, I will keep the project simple for now and focus on understanding the impacts of dynamic pricing on energy consumption amongst various demographic groups. Do they respond differently? In a positive way towards their objectives? (e.g. reducing load at peak times). Does everyone?

## Terms of use
Republishing is not prohibited by data.london.gov

## Ethical Objections
I will be undergoing analyses that ties into demographics of the housing populations there-in. Any results from this analyses may be misinterpreted to mean that particular income classes or other demographics are responsible for wasteful energy usage. Even if this were true, it would likely be explained by another factor, and would unfairly tarnish the groups being studied. Consequently, I aim to be very precise in the discoveries of my analyses and put disclaimers where appropriate to make sure over-reaching statements / conclusions are drawn. However, despite this, some people like to take only part of the facts, and there is little one can do to prevent this if they purposefully ignore your comments.

## Unknowns and dependencies
I am relying on my machine to be able to handle the large size of this data set (10GB when unzipped). If it can't, I will have to do some random sampling or other filtering which needs to be carefully done so as not to not fairly represent all populations. Furthermore, I need to do a few joins on the data given to address all questions I am interested in, which adds complexity to the data munging part of this project.

## Background
The following bullets highlights related and previous work done in the past and general observations on the type of work done
- https://data.london.gov.uk/blog/electricity-consumption-in-a-sample-of-london-households/
  - This comes from the same people who published the data set. They ran simple analyses using tableau on energy consumption over time of the various types of dynamic pricing algorithms. Mainly, the difference between high, avg, and low rates.
- https://www.researchgate.net/profile/James_Schofield6/publication/293176172_Low_Carbon_London_project_Data_from_the_dynamic_time-of-use_electricity_pricing_trial_2013/links/56b6889d08ae5ad36059b61c.pdf
  - This is the official publication of the dataset which describes the fields of data, along with specifics of the data collection process, bias, anonymity, and more
- https://ieeexplore.ieee.org/abstract/document/8322199
  - This article focuses on the many different data sets that have been used in the smart meter field, and the challenges within them, including visualization.
  - According to this article, as of march 2018, there were only two refernces to this data!
  - As of 2019, this has gone to 13 references.
    - 7 in 2019 alone! Clearly this is an exploding data source of interest, smart meters are on the rise!
      - I think this may be off by one as according to google scholar, [this paper](https://www.sciencedirect.com/science/article/pii/S1050173818301117), which discusses a heart disease, supposedly references this data set.
__Summary of background__
There seems to be an increasing rate of exploration and usage of this dataset among others in the smart meter field. The work so far on this dataset on its own is minimal. Most research questions referencing this dataset are exploring multiple at once, often interested in creating probabilistic models for peak load times and volumes. This ties nicely into my research questions

## Research Questions
### Basics
- What are the differences between *dynamic* and *static* pricing households of similar demographics
  - I hypothesize that dynamic users with low tariffs will still act similar to their static counterparts, while high tariff users will act differently than their static counterparts. More concretely, within blocks of households that share similar demographics, they will show similar timing and total usage regardless of their pricing tariff __iff__ it is low tariff dynamic pricing rather than avg or high dynamic tariff pricing
- Can we create a model that can compute the next time steps worth of energy consumption? For example, knowing they utilized .5 kw/hr at 10am, what will they consume at 10:30am? Then continuing this iterative process, can we accurately model the energy over time?
  - In particular, can we do this only with the signal itself, and not the demographic information provided?
### Reach
- Can we create a model that predicts the next time steps worth of energy (similar to the basics pt2), but also utilize demographic information to create a more accurate model

## Methodology
- To address our first question, I plan on doing some basic visualizations to determine timing patterns similarities. For example, a scatter plot of avg consmption per thirty minutes over an average day of low tariff dynamic pricing. We can then compare this graphic to a similar group but with static pricing. Using boxplots, we can get an idea of how much variation aligns in these measures and see if they do or do not overlap with boxplots from our counterpart. I belive this to be a good first step as we would otherwise have to do a t-test for every 30 minute interval of the day, which would mean a total of 24*2=48 t-tests. Visualizing all these tests at once will be tricky. Using this scatterplot technique, I can easily visualize these results.
  - To get a more concrete result, I can use ANOVA over all gfroups to determine the statistical signifigance of these differences
    - I do want to note, that by doing so, I am worried that 30 minute intervals during periods of low activitiy amongst *all* groups will show no difference, and thus reduce the likelihood of finding significant findings. I am tempted to weight the relative importance of the difference by the volume of energy used.
- To address our second question, I plan on using SINDy, or Sparse Identification of Non-linear Dyanmics.
  - This method works by doing linear combinations of random mutations of all the signals we have and using $l_1$ loss functions to choose a sparse representation of our model. It has been used many times in various communities, including chemistry and physics (see references below).
  - The reason why this is a good method for solving our problem is that it can provide an easily interpretable equation that drives electric usage amongst various users in our population. Furthermore, it will not require and information on the consumer themslves.
  - One caveat is that it may not preform all too well, and that providing some information on the consumers, or fitting a model per type of consumer, might do much better. Only time will tell
- To address our reach goal, there are many tools at our disposal. Several papers have tackled demand prediction using deep neural networks along with various other tools. I will likely take a more simplistic approach, and attempt to fit a type of regression. Considering this is a reach goal I do not mind being vague on what methods to use for it.

### References
- J. Chem. (2019). Reactive SINDy: Discovering governing reactions from concentration data. AIP The journal of chemical physics. https://aip.scitation.org/doi/10.1063/1.5066099
- Mangan, N. M., Askham, T., Brunton, S. L., Kutz, J. N., & Proctor, J. L. (2019). Model selection for hybrid dynamical systems via sparse regression. Proceedings. Mathematical, physical, and engineering sciences, 475(2223), 20180534. doi:10.1098/rspa.2018.0534
