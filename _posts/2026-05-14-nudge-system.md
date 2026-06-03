---
id: 2039
title: Choose your own maths adventure - interactive online worksheets
date: 2026-05-14T01:44:54+00:00
author: nadiah_kristensen
layout: post
guid: http://nadiah.org/blog/?p=2039
permalink: /2025/05/14/nudge-system
image: /wp-content/uploads/2026/05/the_room.jpg
categories:
  - teaching
---

Students miss out on in-person workshops for all kinds of reasons, including work and caring responsibilities. 
It's not enough to supply worked solutions because that doesn't facilitate the *productive struggle* that deepens understanding and builds self-efficacy.

Thinking about this problem,
I started thinking about point-and-click adventure games-- they are good at facilitating productive struggle.
They let you try and fail, and they nudge you forward without handing the answer to you. 
They make you want to persist.
I wondered if we could do something like that.

{%
    include figure.html
    src="/wp-content/uploads/2026/05/the_room.jpg"
    caption="The Room - Fireproof Games"
%}

This semester,
I built two interactive linear algebra worksheets for MXB106: two weeks, two multipart questions.
I embedded them into Canvas, the learning management system used at QUT.
You can visit them here: [Week 8](https://nadiah.org/nudge/mxb106/nonhomogeneous_systems.html), 
[Week 9](https://nadiah.org/nudge/mxb106/orthogonality.html).

{%
    include figure.html
    src="/wp-content/uploads/2026/05/embedded_in_canvas.png"
    caption="Interactive linear algebra worksheets embedded into Canvas."
%}


The key design feature was branching paths: 
the student chooses their level of scaffolding and decides where to go next. 

Hints are nested, to reveal gradually, so students retain the satisfaction of solving the problem.

And when the student gets the answer wrong,
the response isn't "Wrong, try again", 
it's "We're going to learn this together", e.g., with a step-by-step guide.

<div style="display: flex; flex-wrap: wrap; gap: 16px; width: 100%; margin: 20px 0;">
  <iframe src="https://nadiah.org/nudge/mxb106/nonhomogeneous_systems.html" style="flex: 1; min-width: 300px; height: 500px; border: 3px solid #ccc;"></iframe>
  <iframe src="https://nadiah.org/nudge/mxb106/orthogonality.html" style="flex: 1; min-width: 300px; height: 500px; border: 3px solid #ccc;"></iframe>
</div>

I also collected detailed anonymised tracking data --- I know exactly which path each student took,
where they clicked, and when --- so I could watch exactly how it worked.

{%
    include figure.html
    src="/wp-content/uploads/2026/05/one_student_journey.png"
    caption="Detailed tracking data for one student. Red triangles are clicks on hints and within-page questions and answers. This student was progressing rapidly until part 4, where they got stuck. They took two quick peeks at the step-by-step guide, but decided to answer the question alone and got it wrong. They were then sent back and spent around 5 minutes progressing through the step-by-step guide until they got the answer right. They then rewarded themselves with a 13 minute break before rapidly finishing the rest of the worksheet."
%}

Remember my main goal was to reach students who are unable to attend in-person workshops.
As luck would have it, in the second week of the trial, the Monday workshop was cancelled due to ANZAC Day-- 
and that's where he had our second-largest spike of activity.
When students couldn't get to their workshop, they used the interactive online version instead.

{%
    include figure.html
    src="/wp-content/uploads/2026/05/timeline.svg"
    caption="The timeline of events leading up to the assignment showing interactions with the Week 8 and Week 9 worksheets. In-person workshop hours are shaded in red, and the first spike of activity occurs during the first workshop. In the second week, the Monday workshop was cancelled due to ANZAC Day (in yellow), and that was where the second spike of activity occurred. When students were unable to attend their in-person workshop, they used the online worksheet instead."
%}

With the detailed tracking data, I was able to focus in on students who fully engaged with the worksheets and worked outside workshop hours.
In the first week, 40% worked outside workshop hours; in the second week, 85% did.

I could also see the hours when they were working. We had some students doing linear algebra at 1 am in the morning.

When I tightened the data again to look at those working *exclusively* outside workshop hours and *deeply* engaged, 
I estimate we picked up about 45 students, which is equivalent to about 2 or 3 in-person workshops.

But did it work?

For this pilot trial, we had selected questions from the existing worksheets that addressed the upcoming assignment in some way.
Compared to previous years,
marks improved on every question (all statistically significant, BH p < 0.03) with an overall improvement of 12 percentage points.

{%
    include figure.html
    src="/wp-content/uploads/2026/05/assignment_results.png"
    caption="Marks improved on every question, all statistically significant, with an overall improvement of 12 percentage points."
%}

We also had some positive qualitative feedback.
One student emailed to request more worksheets,
and the in-person feedback was positive as well.

{%
    include figure.html
    src="/wp-content/uploads/2026/05/feedback.png"
%}

So it seems the online worksheets not only improved marks, students also found them valuable.

### Further reading

I presented talk today at the Faculty Learning & Teaching Colloquium about the worksheets.
A link to the presentation slides is [here](https://nadiah.org/nudge/presentation/).
