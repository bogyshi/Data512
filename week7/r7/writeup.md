# Data 512 week 7 reading
Readings
- Read and reflect: Kocielnik, R., Amershi, S., & Bennett, P. N. (2019). Will You Accept an Imperfect AI? Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems - CHI ’19, 1–14. https://doi.org/10.1145/3290605.3300641

# Notes:

Good background on expectation research in marketing and sales, but not with software. What about consumer spirits and markets? I feel like this is a relatable subject.

With our test setup so far, I am curious if there is some impact on not being in a natural environment for these emails and scheduling asks. E.g. Maybe expectations and satisfaction are quite different in a controlled lab environment than in the wild, but thats with all hypothesis testing.

"We further coded these messages
among two independent coders and selected only the emails
for which both coders agreed on the label." ??s

"Given our RQ2 and RQ3, we wanted an AI component that
will perform below expectations of most end-users. AI per-
forming at a level disappointing for most users enables test-
ing the effectiveness of the expectation adjustment tech-
niques"
This raises an interesting question. If we only expect to measure user satisfaction of a product that is below our expectations to begin with, does that mean this research only applies to models that are post-fact below expectations? Naturally we cant gauge expectations of novel ML algorithms without introducing it into the wild for a while. To some extent its relative along with the cost of doing business. Meaning, even if a model performs really well relative to others, or its the first of its kind, low performance will cause users to likely not use it if the overall low performance is still a problem.

"
A total number of 150 partici-
pants from US only aged 18+ was recruited (25 per condition).
We used a standard recruitment supported by our crowd-
sourcing platform posting short information about the task,
the expected time required, and the payment. Each partici-
pant was allowed to complete the Study only once. The Study
has been approved by internal IRB and took on average 5:21
min (SD : 3.45 min). Participants were compensated $1.35
per task."
Some bias is likely to come up here. But glad to se the turkers are getting paid well.

"Hence the
questions aimed at covering detections of true positives and
true negatives (the two items were moderately correlated
r s = .55)." No p-value?


They do address bias somewhat

However, some of these questions are not completely reliable. For example, asking a user if they know how many times they interact with AI and how tech savy they are can be quite misleading. sometimes we dont even know we are interacting with AI (ex uber). However, perhaps its not too important that the user is well educated in what AI is and is not.


"
In particular
a number of aspects should be considered, such as workload,
both mental (e.g., ignoring incorrect suggestions, scanning
multiple suggestions) and physical (e.g., having to execute
a task manually or reverse an incorrect system action), as
well as criticality of consequences of following an incorrect
AI suggestion (e.g., not scheduling meeting, making an un-
solicited purchase)."
This observation I would hope is well known in the ML / data scientist community.

# Reflection

## How does this reading inform your understanding of human centered data science?

There needs to be careful study of the impact false positive and false negative rates can influence a users perception of technologies I built and the AI system as a whole. For example, if I create a tool that automatically tells you how much exercise you did within a day, users will be upset when what they considered an exercise was not recorded, and they would have to submit it themselves if they want to keep track of it. This impacts not only the perception of my tools, but also reflects the field as a whole. The more technologies available for the same service that fail to perform with the proper expectations, developers will be hard pressed to sell them on the same idea again even if it has improved. This goes well beyond recreational AI services, into fields where ML decision makers are put into play and need to be held to strict standards and have carefully tuned false positive and false negative rates.

The overall concept is something I would hope all data scientists already have in mind. When we create our tools, we need to make sure they are fitting the actual business need at hand, even if it results in some lower metrics in accuracy or MSE.

## One question that came to mind.

Throughout the article, p-values were used quite a bit (even though it was missing it some spots), but significance was determined at the 0.1 and 0.05 level. At the same time, no bonferroni corrections were used. Now this isn't necessary to have some interesting results, however, i would hesitate that all their conclusions were statistically significant. Can we really conclude from their tests that this difference in means between groups shows that higher recall than precision benefits user acceptance of the email assistant? 
