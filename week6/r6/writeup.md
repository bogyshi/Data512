# Data 512 week 5 reading
Readings
- Baumer, E. P. S. (2017). Toward human-centered algorithm design. Big Data & Society.
- Amershi, S., Cakmak, M., Knox, W. B., & Kulesza, T. (2014). Power to the People: The Role of Humans in Interactive Machine Learning. AI Magazine, 35(4), 105.
# Notes:

## Power to the People
The Role of Humans in
Interactive Machine Learning

 NOTE, this goes against the common argument that studying users is pointless, as ML will do it better and humans will adapt properly, rather than fine tuning a system to human behaviors. EX, trying to improve predictive accuracy of system.

 When asked what they
were thinking while interacting with the system,
most users stated that they were focused on seein

This made me think of ROC curves, or other methods to represent what we were getting wrong without going through individual images.

Training humans to better provide labels is an interesting thought. I worry that we are training ourselves to think like the algorithm, which is not necessarily what we want to do.

learning system for image
classification (figure 5). Through a user study, the
authors demonstrated that a technique of presenting
users with only the best- and worst-matching exam-
ples enabled users to evaluate model quality more
quickly and, in turn, train significantly better models
than the standard technique

This is because humans arent as fast as machines. How many iterations of user labeling did each one have to go through? The more iterations on the machines end the better.

The study showed that both
intermittent approaches resulted in learning as fast
as the fully active approach, while being subjective-
ly preferred over fully active or fully passive
approaches.

Why dont they list the results here? Just curious, would make my life easier rather than diggin it up

## Toward human-centered algorithm design
When confined to a labora-
tory or scientific setting, results along these lines could
be seen as aberrant and interpreted as such. However,
when algorithms become incorporated into interactive,
public-facing systems, their results become interpreted
by people who likely have less knowledge of the tech-
nical implementation details of these algorithms.


Prior work has described the
idea of social imaginaries (Anderson, 1983; Castoriadis,
1975; Taylor, 2004). An individual person does not and
cannot know how every other individual in a society
behaves. Thus, people form social imaginaries, descrip-
tions of how they believe others within a culture and/or
our society behave.
I like this line above, havent hear it talked about it before.

Doesnt giving just the facts give us news? There is nothing subjective about number of people dieing. However, there is subjectivity in determining monetary penalties, future impacts ... So I guess it isnt so simple in how we may present just facts neutral news.

The participatory strategy. So this is interactive machine learning.


Moreover, a participatory approach could facilitate a dialectic exchange
among those who might interact with the system and
those who are designing and implementing it. Doing so
would help better understand the formation of, and
potentially how to intervene in the process of developing, computational imaginaries.

Instead, it may
prove more effective to cultivate what one might call
‘‘-shaped’’ people, ones who have a wide breadth of
knowledge but also deep expertise in multiple disparate
disciplines.
This is what everyone asks for in interviews these days, esp data science.

While an algorithm’s designers do not
necessarily need or want others to understand how it
works, they likely want to reach consensus on what it
means.
This is not always true.
# Reflection

## How does this reading inform your understanding of human centered data science?

My largest takeaway is that end-user or "humans" in general should be involved in our machine learning tasks. They can help us determine initial follies in the outputs and visualizations of our model. This is something constantly iterated in my past internship at microsoft, where we want a MVP that we can show to our clients or end users and get feedback if this is answering their questions or not. Obviously iteration is good, but there is a fine balance where we dont want to be constantly bothering the users or clients. I enjoyed the point in the second paper on social and computational imaginaries. Social imaginaries is something I have thought about, but never really had a word for it. Sounds a bit like stereotyping

## One question that came to mind.

Having users better understand the algorithm, or at least the results, may seem good at times. However, I think what is really exciting about ML and the results we get are the results we do not expect or like. These are the things that tell us something novel or new to explore. This makes me hesitate on some applications of humans in the ML process. ML algorithms are meant to be "unbiased", but can be fine tuned by humans to fit a different need. Im not sure if this is necessarily the wrong or right thing, but I think there needs to be some discussion on when human intervention and altering of ML algorithms is the "right" thing to do.
