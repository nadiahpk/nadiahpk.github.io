Claude estimate: roughly 10 minutes (9-12)

# Title slide (0:45)

There are many reasons why a student might skip their workshop, including reasons to do with equity.
Making solutions available isn't enough,
because that doesn't provide the *productive struggle* that builds self-efficacy.
Can we provide those active-learning opportunities some other way?

I took inspiration from point-and-click adventure games,
and the techniques game developers use.
Funnily enough, they're the same as the techniques we use in workshops:
feedback for wrong answers, scaffolding while respecting the players autonomy,
and *gradually* revealing hints to preserve that sense of achievement.

# 1a. What did we do? (2:00)

We created two interactive linear algebra worksheets, 
multipart questions on non-homogeneous systems and orthogonal projections.

The key design feature is branching paths. 
Students decide where to go next.

Hints are nested, to reveal gradually.

And when the student gets the answer wrong ---
here, I'm going to be a student who doesn't know how to do a Gaussian elimination ---
the response isn't "Wrong, try again", it's "We're going to learn how to do a GE".

We initially thought we'd create these in H5P, but we found it didn't have the 
flexibility and also couldn't display matrix equations properly.
So we used Tweego.
Its main benefit of Tweego is the input is plain text,
so you can use the editor of your choice --- it's faster ---
and you can use AI for reviewing and rapid restructuring ---
Claude knows Twee.

# 1b. What did we do? (1:15)

We also collected granular data on each student's interaction with the system.

Here's and examples of a student working through a question.
Red triangles are in-passage clicks -- hints and short-answer responses.
We can see exactly where they clicked and when.

You can see here this student moved quickly and confidently through the first three questions,
and then they got a bit stuck on Q4.
They took two quick peeks at the step-by-step guide and decided to try and answer the question 
by themselves.
They got it wrong, so they go back and they choose the step-by-step guide.
They spend about 5 minutes working through it, answering each of the intermediate questions,
until they got it right.
They rewarded themselves a 13 minute break before getting back to it and quickly finish 
the rest of the worksheet.

This granular data allows us to restrict our attention to those who truly engaged with the worksheets.

# 2a. Who did we reach? (0:50)

So let's zoom out-- who used the worksheets and when?

Remember that our goal is to provide active-learning opportunities for students who can't attend workshops.

Here is a timeline of the two weeks before the assignment was due.
The pink regions are in-person workshops,
and there are spikes of activity there.

As luck would have it, in the second week,
the Monday workshop was cancelled due to ANZAC Day-- and that's where the next major spike 
of activity happened.

When students weren't able to get to their workshop,
they used the interactive worksheet instead.

# 2b. Who did we reach? (1:00)

Let's take a closer look at users outside workshop hours. 

The first thing to notice is the proportion outside of workshop hours 
-- 40% in the first week, 85% in the second week.

The second thing is the hours worked.
Who's doing linear algebra at 1 in the morning?
Maybe a student who works at the casino to help his mum pay the bills.

When I more tightly the data some more to those who worked *exclusively*
outside the workshop hours and *only* deeply engaged,
I estimate we picked up about 45 students,
which is equivalent to about 2 or 3 in-person workshops.

And that was the point. That's why I did it.

# 3a. Did it work? (0:35)

Did it do them any good?

We got some qualitative feedback.
One student emailed to ask for more.
In person, I received a pretty positive response 

... "Better than Khan academy" (laugh) 
the obvious caveat here is that my students only want to say nice things to me ---
though they did give me one piece of critical feedback we'll get into soon.
And besides, we can look at their grades.

# 3b. Did it work? (3:45)

## Previous semester 

These are the assignment questions and the marks in equivalent questions in previous semesters.

We chose workshop questions that addressed the assignment in some way,
and my focus was on conceptual understanding-- explaining what the answer means, showing a Desmos graph,
so on.

For two questions, I've marked with an asterisk,
I also targeted easy marks lost due to missing explanations.
Now this could also reflect missing conceptual understanding,
but it's also a bit "hidden rules of the game", so I hit those pretty hard.

## Correctness improved on every question

This semester, marks improved on every question, all significant.

Now we should be careful because the questions are different,
a bigger matrix means more arithmetic errors.
Better understanding means errors but let's discount those...
So where does that leave the rest of them?

## Substantive errors

The rest were dominated by conceptual errors and missing explanations.

Conceptual error here folds in "didn't even attempt the question"-- 
we had a lot more attempts this year as well.

Now the obvious caveat here is cohort effect.
I can't rule this out. 
But I have 2 reasons why I'm hopeful.

First, the specificity of the missing-explanation response.
Q2c was: draw the right-angle symbol between projection and error vectors.
I saw some confused diagrams, but by god they had a right-angle symbol in there.

Missing explanation is a very easy thing to target.

In contrast, for Q1d, there was a particular trick I wanted them to use.
But I received feedback that part of the worksheet was confusing,
and that was reflected in the trace data as well.
And the marks reflected that -- no significant change in that behaviour.

So I'm cautiously optimistic that the interactive worksheet was the cause of improved outcomes,
and the engagement data shows it reached the cohort I wanted.

I'm also excited about capturing pedagogical intent.
We have some excellent worksheets with well thought out questions,
but there are structural factors that mean that, even for in-person workshops,
that pedagogical intent is not going to get transmitted.
And so this is a way to capture that pedagogical wisdom and get it to the students who need it.

I'd love to talk to anyone who's interested in contributing to where I will take this next.

# Threw out 

You'll notice conceptual error overshoots on Q1d, and that's basically because 
there were a few more arithmetic errors this semester.
