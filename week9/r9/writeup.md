# Data 512 week 9 reading
Readings
- Read and reflect: Passi, S., & Jackson, S. J. (2018). Trust in Data Science: Collaboration, Translation, and Accountability in Corporate Data Science Projects. Proceedings of the ACM on Human-Computer Interaction, 2(CSCW), 1–28. https://doi.org/10.1145/3274405

pay attention to research methodology
first 6 pages are tough, case studies are super interesting
do case studies resonate, do they reflect experience and challenges?
# Notes:

“[The] idea of data-led objective discoveries entirely discounts the role of interpretive
frameworks in making sense of data which [are] a necessary and inevitable part of interacting
with the world, people and phenomena” [69:320]
common note in all our discussions so far

...show how “working solutions” to problems of credibility in early
experimental science were found in the social perception of gentlemen as “reliable truth-tellers.”
interesting start

so looks like throughout time, a need for reproducability was needed to be believed, or at least multiple groups had to solve a problem and come to roughly the same conclusion. The major change over time was an increased need for some visual result to demonstrate. So it went from word of mouth, to pictures, to numbers today. but they compound, so today is word of mouth, pictures, and numbers

They describe six orders of worth – civic,
market, industrial, domestic, fame, and inspiration – within which “justifiable agreements” are
achieved in social and professional practices.
So within each of these seven, we have perhaps different standards and processes to determine the  value of something, which impacts our ability to trust it? Id argue there are things that arent valuable that we still trust? E.g. most of us trust gravity

A model configured for specificity does not focus on maximizing the number or
accuracy of its correct predictions but on minimizing the number of its incorrect predictions. The
aim was to ensure that healthy customers were not incorrectly identified as likely-to-churn.
This is just precision im pretty sure

Only two credit score ranges were now important: below-500 and above-500. The solution
to the matching problem (which leads are likely to get financed by a lender) was now a classification
task (which leads have a credit score of over 500).
This makes me think of our talk last week, this is one of those jumps we might see with the GAM. Could this mean this is potenitally the wrong paproach? Or could we find the true ideal credit score some other time?


For example, in a different project, we saw that a model whose results completely mirrored
existing insights was deemed a failure by business personnel who argued that the model “lacked
business intelligence” because it furnished “no new information.”
I think this might happen a lot in reality

auditing and story telling are important to D.S. big time

With current calls for more open documentation, corporate
organizations need to document not only algorithmic functions and data variables, but also data
decisions, model choices, and interim results.
we talked about this after reading a paper on the oracle based questions to highlight what tools D.S. needs to create more reproducible research, like an ability to have easier version control and searching of methods in notebooks

Limitations and future work addressed some great questions I still have and continue to think about, such as who gets the final say (my opinion/experience is business execs). Are we allowed to fail?

# Reflection

## How does this reading inform your understanding of human centered data science?

The perspective offered great insights into the thoughts and processes behind various groups that interact with and within a data science team. I learned a bit more about the trust that needs to be established and maintained by data science teams. In both case studies, but in particular the neural network on loan buyer matches reflected a lot of my experiences while at microsoft. I think overall this article gave me a greater appreciation for the kinds of trust needed in the corporate environment. They may trust you, but they need to trust the model as well. Creating a narrative and showing the results of outputs (but good and bad) are necessary to develop these applications to great success.

## One question that came to mind.

At one point in this article they asked the data scientist if the results were in line with their intuition. They said yes. The point being not that they answered yes, but having an answer to this question is difficult. The business sense is not something I believe data scientists are meant to have to a great extent, which is why we have PMs and BAs. I would thus take this as an opportunity to ask how much business sense do we expect a data scientist to have? 
