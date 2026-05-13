# Title slide

There are many reasons why a student might not be able to attend an in-person or synchronous workshop,
including reasons to do with equity.
It's not enough to read the answer sheet because that's not going to create
the *productive* struggle that builds self-efficacy.
So how can we provide them with that active-learning opportunity anyway?

We took inspiration from point-and-click adventure games,
and the techniques that game developers use to keep the player going.
Funnily enough, they're similar to the techniques we use in workshops:
feedback for wrong answers, scaffolding while respecting the players autonomy,
and gradually revealed hints that preserve that sense of satisfaction.

The Room (Fireproof Games)

# 1. What did we do?

We created online interactive worksheets where students work through linear-algebra
problems.
The interactive worksheets have branching paths, 
hints they can reveal when they need them, and diagnostic feedback when they pick a wrong answer 
--- feedback that explains the specific misconception, not just 'try again'.

SLIDE
- left column:
    - Three callout labels: 
        1. "branching: choose your path", 
        2. "hints on demand", 
            - hint cascade (scaffolding without spoiling)
        3. "diagnostic feedback for specific wrong answers
            - Claude suggests highlighting diagnostic feedback, e.g., parta_incorrect answers"
    - Question prompt at top 
- right column 
    - top half - trace HTML
    - bottom half - timeline with ANZAC day
        - and we see students working outside the in-person workshop hours
    - message, I have both granular and aggregate data
    
Left column should be an embed of https://nadiah.org/nudge/mxb106/nonhomogeneous_systems.html 
Click first on reveal hints to show they're nested,
then click on wrong answer to see step-by-step guide.

Did they enjoy it? One emailed to ask for more, in person: 
re feedback - "you read my mind", "better than Khan academy" (laugh) 
The obvious caveat here is that my students would only want to say nice things to me,
so we can look at the data.

But we can also snoop and see what they actually did.
Here's one student working through, click hints, 
looking at the step-by-step guide, answering questions,
getting them wrong and going back.

# 2. Who did we reach?

left: in-workshop users, working on ANZAC day 
right: distribution outside workshop hours 

Point out that most of the workers on orthogonality are outside workshop hours 

Who is the student who is forced to work such late hours?
Do they have life circustances that prevent them from working during the day?

words: picked up about 40-50 students working entirely outside workshop hours 
-- equivalent to 2 or 3 in-person workshops worth

homog: 79 engaged, 38 self-study (19 reached third Q)
orthog: 67 engaged, 52 self-study (37 reached third Q)

This is who I wanted to reach. This is the point.

# 3. Did it work?

Did it do them any good?

We chose from the worksheets those questions that best supported success in the assignment.
TO DO - put in semester before that as well 

- Here are questions from Workbook 2
- Interactive worksheet targetted conceptual understand for every question
- For these two questions, also targetted students leaving off their explanation of their result, 
which is both conceptual but also a "hidden curriculum" type mistakes with an equity dimension
- Stretch goal: a "trick" to getting through one question quickly

Caveat: cohort effect. But two reasons:
First, the signal of the specific explanation I targetted-- including the right-angle symbol.
Anecdote.
Second, a failure on my part.

Q1d - xp, no effect
Q3a - GE, told how but didn't show. p didn't reach significance.

End with: "I'm cautiously hopeful that the worksheet contributed; 
the engagement data shows it reached the cohort most likely to need it." 

# Slide 3: 

After seeing the invite, he suggested:
- what we learned + what could scale 
    - Design lessons: the Q-E(i) CONTINUE-button issue you discovered, the step-by-step works-but-doesn't-quite-bridge pattern. This signals "I'm self-aware and iterative" — peers respect that.
    - What could scale: the manual / template idea, replication to other units, the AI integration angle (you wrote in your abstract that Twee's plain-text format integrates with generative AI tools — that's directly relevant to the  colloquium's listed AI topic).
    - Verbal close: "I'd love to talk to anyone interested in trying this for their unit, or in supporting where this goes next." That's an open invitation without being pushy. 

  The AI angle is worth a mention. Your abstract noted Twee's text-source format works well with generative AI tools. The colloquium has explicitly flagged AI as a discussion thread. A single sentence on slide 3 like "and the plain-text source integrates with AI tools — making worksheet authoring radically faster than HTML-based alternatives" is a value-add for this audience that wouldn't have been worth it for money people. Could land well.

Initially planned to use H5P "branching scenario",
but switched to building on Tweego instead. 
Tweego was initially designed for creating interactive online fiction --- choose your own adventure stories.
Benefits were 
- plain text files: much faster to work with than clicking a GUI and allows easy integration with AI tools
- greater design flexibility: nested reveal-text and how the branching works in general,
but also strip away visual noise and clutter
- ability to import tools that allow maths to render correctly 
- can import anything else H5P uses, such as images, videos, desmos graphs, etc.

# Threw out 


However, in-person or even synchronous online workshops aren't available to everyone,
and there are structural factors at play here which mean that, even synchronously,
the deeper pedagogical intent of these often very well designed worksheets questions gets lost.
