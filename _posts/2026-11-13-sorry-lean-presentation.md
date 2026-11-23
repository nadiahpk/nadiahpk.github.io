---
id: 2042
title: Presentation about Lean at Griffith
date: 2026-11-13T04:44:54+00:00
author: nadiah_kristensen
layout: post
guid: http://nadiah.org/blog/?p=2042
permalink: /2026/11/23/sorry-lean-presentation
image: /wp-content/uploads/2026/11/koala.jpg
categories:
  - coding
---

Today,
I gave an informal presentation to the applied maths group at Griffith University about 
[Lean](https://lean-lang.org/).

{%
    include figure.html
    src="/wp-content/uploads/2026/11/koala.jpg"
    caption="Here's a photo of a koala I saw at Nathan Campus earlier this year. It has a bit of a painterly quality to it because of how much I zoomed in."
%}

I started learning Lean a few months ago after [Carlo](https://carlo-hamalainen.net/) 
conducted an AI experiment with one of my [previously published papers](http://127.0.0.1:4000/wp-content/uploads/2025/03/Kristensen25-Many_strategy_group_games_with_relatives_and_coordinated_cooperation.pdf).
Carlo heard the news about the Navier-Stokes Millenium Problem
and was curious what AI+Lean could do,
so he took my paper plus a recent [proof sketch](https://nadiah.org/2025/03/19/degree-theorem-sketch)
and asked Claude to formalise it all in Lean.

Claude returned after a few hours with about 10,000 lines of Lean code.
The good news was that it found no serious errors in my work,
and now I apparently have all my proofs verified in Lean.
The bad news is that I don't understand Lean.

So since early October, 
I've been teaching myself using the Lean Community's textbook [Mathematics in Lean](https://avigad.github.io/mathematics_in_lean/).
This is a pretty great resource,
which alongside a textbook includes exercise templates and worked solutions.

The purpose of my presentation was to share what I've learnt so far about Lean.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_1.png"
    caption=""
%}

The first proof I ever wrote in Lean was a proof of the squeeze theorem,
which Alex Kontorovich started but left unfinished in 
[this introductory video](https://www.youtube.com/watch?v=I2zaPoj3G50).
This video was an excellent starting point for me,
even before starting the exercises in the textbook,
because it gave me a clear practical introduction to what Lean is and what it does.
I highly recommend it if you're brand new too.

The first time I completed the proof, I needed a *lot* of help from Claude.
I really recommend working with an AI "tutor",
which also allowed me to discuss some of the mindblowing ideas underlying Lean
(e.g., 
"A proposition is itself a type, and a proof of that proposition is an object of that type";
and "A theorem is a function that converts proofs into proofs").
As I worked through the textbook (I'm currently up to chapter 3),
I would intermittently return to the proof with new understanding and ideas to experiment with.

For the presentation,
I decided I too would demonstrate how Lean works by doing a live proof of the squeeze theorem.
However, 
I also structured it as though we're all students trying to figure out the proof in real time.
I chose this framing because I was curious if Lean could be used as a teaching tool.
In particular, Lean forces the student to step through the process 
in a rigorous way while providing immediate feedback.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_4.png"
    caption=""
%}

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_5_6.png"
    caption=""
%}

<h3>Finding the proof</h3>

We began by imagining what we might write on a scrap of paper:
a sketch of an example,
a quick summary of the definition of convergence and the theorem, 
and then some working on how to get $$\lvert b_n - L\rvert < \varepsilon$$ 
out of the convergence of $$a$$ and $$c$$ and the inequality condition.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_7.png"
    caption=""
%}

Keen-eyed readers will notice that I've made an omission here: I've forgotten 
all about $$N$$! Lean will force us to come back to this,
which I thought might have pedagogical value.

I used the definition of convergence as an opportunity to briefly introduce the syntax 
and the idea of a type.
I couldn't really do type theory justice,
but it was also useful to just pause here on a static slide 
so everyone could get used to the new syntax.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_8.png"
    caption=""
%}

Then I switched into Lean live to encode the theorem statement.
This was more time to absorb the syntax and now see how maths symbols are written.
I'm used NeoVim, but VSCode works in a similar way,
allowing the user to enter symbols by typing the LaTeX or `\` followed by some other 
shortcode.
```lean
theorem squeeze_theorem (a b c : ℕ → ℝ) (L : ℝ)
  (a_le_b : a ≤ b) (b_le_c : b ≤ c)
  (a_to_L : seq_converges_to a L)
  (c_to_L : seq_converges_to c L) :
  seq_converges_to b L := by
    sorry
```

After encoding the theorem statement,
I followed similar steps to Kontorovich in the video:
I used `unfold` to rewrite the goal as 
```
⊢ ∀ ε > 0, ∃ N, ∀ n > N, |b n - L| < ε
```
We talked about what it means to say "Take an arbitrary $$\varepsilon > 0$$",
and I showed how `intro` works.
```lean
    intro ε ε_pos
```

Then we hit the $$\exists N$$ part of the goal,
and I couldn't use `intro` here --- we're meant to do something else.
This was my pedagogical point.
If I am new to the concept of a constructive proof, 
for example, then getting stuck here is instructive;
it forces me to return to the problem and think again 
about just what it is that we're trying to prove.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_10_11.png"
    caption=""
%}

In this case --- to prove that $$N$$ exists --- we need to supply an $$N$$ that works.
In particular, 
we need to choose a value of $$N$$ that allows use to make use of 
$$a \rightarrow L$$ and $$c \rightarrow L$$,
as done in the proof sketch.

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_12_13.png"
    caption=""
%}


After a bit of discussion, we decided that we should choose $$N := \max(N_a, N_c)$$.

The `obtain` lines were an opportunity to show one way to work with a hypothesis.
To define $$N := \max(N_a, N_c)$$,
we need to extract the $$N_a$$ and $$N_c$$ (the witnesses) out of `a_to_L` and `c_to_L`.
I have in my hand an arbitrary $$\varepsilon > 0$$,
so I pass it to each hypothesis,
and they give me their witness-proof pairs:
```lean
    obtain ⟨Na, hNa⟩ := a_to_L ε ε_pos -- Na : ℕ; hNa : ∀ n > Na, |a n - L| < ε
    obtain ⟨Nc, hNc⟩ := c_to_L ε ε_pos -- Nc : ℕ; hNc : ∀ n > Nc, |c n - L| < ε
```
Now we I can define and supply our $$N$$
```lean
let N : ℕ := max Na Nc
use N 
```

We passed the $$\forall n > N$$ with `intro n n_gt_N` like before,
and then we were left with the goal: `|b n - L| < ε`.
Now was the opportunity to introduce MathLib.

In the proof sketch,
I jumped straight from $$\lvert b_n - L\rvert < \varepsilon$$ to the two inequalities.
Straightforward maths facts like that exist as theorems in Mathlib.
In this case, I want to make use of the theorem called `abs_lt`.
We checked its definition with `#check abs_lt`, 
and then we made use of it with `apply`:

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_15.png"
    caption=""
%}

```lean
    apply abs_lt.mpr
```


We can now split the goal into two subgoals, which I did with `refine` and bullet points.
I left a `sorry` for each subgoal, 
which I explained is like an "I owe you" to Lean that I will put the proof there later.
At this point,
the code looked like this:
```lean
#check abs_lt -- |a| < b ↔ -b < a ∧ a < b
theorem squeeze_theorem (a b c : ℕ → ℝ) (L : ℝ)
  (a_le_b : a ≤ b) (b_le_c : b ≤ c)
  (a_to_L : seq_converges_to a L)
  (c_to_L : seq_converges_to c L) :
  seq_converges_to b L := by
    unfold seq_converges_to
    intro ε ε_pos
    obtain ⟨Na, hNa⟩ := a_to_L ε ε_pos -- Na : ℕ; hNa : ∀ n > Na, |a n - L| < ε
    obtain ⟨Nc, hNc⟩ := c_to_L ε ε_pos -- Nc : ℕ; hNc : ∀ n > Nc, |c n - L| < ε
    -- the N that will work for both is N = max(Na, Nc)
    let N : ℕ := max Na Nc
    use N
    intro n n_gt_N
    -- SPLIT GOAL into two goals to prove
    apply abs_lt.mpr
    refine ⟨?_, ?_⟩
    · sorry -- ⊢ -ε < b n - L
    · sorry -- ⊢ b n - L < ε
```

To save time, I decided to demonstrate only the lefthand branch,
i.e., show that `-ε < b n - L`.
We recalled what our plan was from proof sketch:
combine $$-\varepsilon < a_n - L$$ (from $a \rightarrow L$)
with $$a_n \leq b_n$$ (given) to obtain $$-\varepsilon < b_n - L$$. 

The first fact, $$-\varepsilon < a_n - L$$, is inside the hypothesis `hNa`. 
To get to it, we need to step past $$n > N_a$$.
In other words,
we need to show that the `n` we have in our hands (from the line `intro n n_gt_N`)
satisfies $$n > N_a$$.
Indeed, that should be the case because that's why we chose $$N := \max(N_a, N_c)$$.

After a bit of pen and paper work, we see why $$n > N_a$$ is true,
and we can tell Lean by applying a transitivity theorem:

{%
    include figure.html
    src="/wp-content/uploads/2026/11/slide_16_17.png"
    caption=""
%}

Here was an opportunity to demonstrate another practical use of `sorry`.
I know that $$N \geq N_a$$ because it's the maximum,
but maybe I don't know what the name of that MathLib theorem is.
So I put in a placeholder `sorry` to return to later.
```lean
    have n_gt_Na : n > Na := by
      have N_ge_Na : N ≥ Na := by
        sorry
      exact Nat.lt_of_le_of_lt N_ge_Na n_gt_N
```

The Infoview told me the structure above worked,
so I returned to the `sorry`,
and I showed them the handy use of `apply?`.
When I replaced the `sorry` with `apply?`,
Lean told me exactly what I needed to complete that proof:
```
Try this:
  [apply] exact Nat.le_max_left Na Nc
```
So I copied and pasted `exact Nat.le_max_left Na Nc` in the place of `sorry`,
verified that it worked,
and we could move on.

With `n_gt_Na` ($$n > N_a$$) in hand,
we could now extract the fact $$-\varepsilon < a_n - L$$ from `hNa`. 
This provided another example some of the moves we'd just seen: the use of `have`,
using a hypothesis `hNa`, another use of `obtain`, and another use of `abs_lt` 
but this time in the forwards direction.
```lean
    have ha : |a n - L| < ε := by
      exact hNa n n_gt_Na
    obtain ⟨ha_left, ha_right⟩ := abs_lt.mp ha -- ha_left : -ε < a n - L
```

The proof sketch idea was to combine the $$-\varepsilon < a_n - L$$ above with
with $$a_n \leq b_n$$,
which I gave with one line:
```lean
    have a_le_b_n : a n ≤ b n := by exact a_le_b n
```
The explanation is that Mathlib defines $$\leq$$ on functions pointwise,
so `a ≤ b` means $$\forall n, a_n \leq b_n$$.
By supplying `n`, I obtain the inequality at the point `n`.

The final step was to combine $$-\varepsilon < a_n - L$$ with $$a_n \leq b_n$$ 
to obtain $$-\varepsilon < b_n - L$$.
This was an opportunity to explain that,
although we could do this step-by-step,
Lean also has tactics like `linarith` that can deal with routine operations.
I replaced the `sorry` in the first bullet with:
```lean
    refine ⟨?_, ?_⟩
    · linarith [ha_left, a_le_b_n] -- ⊢ -ε < b n - L
    · sorry -- ⊢ b n - L < ε
```
and the left-hand subgoal was completed.
I could have left out the `[ha_left, a_le_b_n]` part of that line
because `linarith` uses all hypotheses in its context,
but I thought it was helpful documentation.

<h3>From Lean code to human proof</h3>

The final thing I wanted to show with the audience was that 
formalising a proof in Lean can make it easier to write the manuscript version of 
a proof clearly and rigorously.
To do so, we can go through each line of our Lean code and translate it into English.

*Proof.*

```lean
    unfold seq_converges_to
    intro ε ε_pos
    -- ⊢ ∃ N, ∀ n > N, |b n - L| < ε
```

Let $$\varepsilon > 0$$. 
We must find $$N \in \mathbb{N}$$ such that $$\lvert b_n - L\rvert < \varepsilon$$ for all $$n > N$$.

```lean
    obtain ⟨Na, hNa⟩ := a_to_L ε ε_pos -- Na : ℕ; hNa : ∀ n > Na, |a n - L| < ε
    obtain ⟨Nc, hNc⟩ := c_to_L ε ε_pos -- Nc : ℕ; hNc : ∀ n > Nc, |c n - L| < ε
    -- the N that will work for both is N = max(Na, Nc)
    let N : ℕ := max Na Nc
    use N
```
**Choosing $$N$$**.
Since $$(a_n)$$ converges to $$L$$, there is some $$N_a \in \mathbb{N}$$ such that

$$
  \lvert a_n - L\rvert < \varepsilon \quad \text{for all } n > N_a.
  \tag{1}
$$

Similarly, since $$(c_n)$$ converges to $$L$$, there is some $$N_c \in \mathbb{N}$$ such that

$$
  \lvert c_n - L\rvert < \varepsilon \quad \text{for all } n > N_c.
  \tag{2}
$$

We need a single $$N$$ that works for both sequences, so we take

$$
  N := \max(N_a, N_c).
$$

```lean
    intro n n_gt_N
    have n_gt_Na : n > Na := by
      have N_ge_Na : N ≥ Na := by
        exact Nat.le_max_left Na Nc
      exact Nat.lt_of_le_of_lt N_ge_Na n_gt_N
```

**Checking that $$N$$ works.**
Let $$n > N$$. Since $$N = \max(N_a, N_c)$$, then $$N \geq N_a$$, and we have

$$
  n > N \geq N_a,
$$

so $$n > N_a$$. 

```lean
    have n_gt_Nc : n > Nc := by
      exact Nat.lt_of_le_of_lt (Nat.le_max_right Na Nc) n_gt_N
```

In the same way, $$n > N \geq N_c$$, so $$n > N_c$$.

```lean
    have ha : |a n - L| < ε := by
      exact hNa n n_gt_Na
```

Because $$n > N_a$$, inequality (1) gives $$\lvert a_n - L\rvert < \varepsilon$$. 

```lean
    obtain ⟨ha_left, ha_right⟩ := abs_lt.mp ha -- ha_left : -ε < a n - L
```

Recall that for real numbers $$x$$ and $$y$$,
$$\lvert x\rvert < y \iff -y < x \text{ and } x < y$$.
Applying this to $$\lvert a_n - L\rvert < \varepsilon$$, we get in particular

$$
  -\varepsilon < a_n - L. \tag{3}
$$

```lean
    have hc : |c n - L| < ε := by
      exact hNc n n_gt_Nc
    obtain ⟨hc_left, hc_right⟩ := abs_lt.mp hc -- hc_right : c n - L < ε
```

Likewise, because $$n > N_c$$, inequality (2) gives $$\lvert c_n - L\rvert < \varepsilon$$, and therefore

$$
  c_n - L < \varepsilon. \tag{4}
$$

```lean
    have a_le_b_n : a n ≤ b n := by exact a_le_b n
    have b_le_c_n : b n ≤ c n := by exact b_le_c n
    apply abs_lt.mpr
    refine ⟨?_, ?_⟩
    · linarith [ha_left, a_le_b_n] -- ⊢ -ε < b n - L
    · linarith [hc_right, b_le_c_n] -- ⊢ b n - L < ε
```

**Bounding $$b_n - L$$.**
Using the same characterisation of absolute value, showing $$\lvert b_n - L\rvert < \varepsilon$$ 
    is equivalent to showing that

$$
  -\varepsilon < b_n - L \quad \text{and} \quad b_n - L < \varepsilon.
$$

For the lower bound, combining $$-\varepsilon < a_n - L$$
    (3) with $$a_n \le b_n$$ gives

$$
  -\varepsilon < a_n - L \le b_n - L.
$$

For the upper bound, combining $$b_n \le c_n$$ with $$c_n - L < \varepsilon$$ 
    (4) gives

$$
  b_n - L \le c_n - L < \varepsilon.
$$

Together these give $$-\varepsilon < b_n - L < \varepsilon$$, that is, $$\lvert b_n - L\rvert < \varepsilon$$.

Since $$n > N$$ was arbitrary, $$\lvert b_n - L\rvert < \varepsilon$$ holds for all $$n > N$$. 
Since $$\varepsilon > 0$$ was arbitrary, $$(b_n)$$ converges to $$L$$.

<h3>Learning value?</h3>

I asked the audience members who were seeing Lean for the first time 
whether they thought this would be a good learning tool,
and the response was generally negative.
The consensus was that this was definitely not useful for undergrads,
particularly not for those with no coding experience.
We remembered what it was like when we ourselves were first learning how to code,
how even small syntax errors could cause hours of struggle and confusion.
Plus the the cognitive load of learning maths and this peculiar new language at the same time 
would just be too much.

Some audience members pointed out that the user has to be highly motivated 
to persist with this.
I agreed that I personally have a strong motivation to do this,
so that might be why I feel like I have been getting so much out of it.
They agreed there was a lot that could be learnt this way,
and in a great deal of depth,
but some proportion of students in every subject are not interested in that subject in particular,
it is simply a step on their way to where they want to go.
I agree that's valid, and this depth of learning is overkill for those students.

So perhaps it could be a useful pedagogical tool for an enthusiastic late-course student or for HDRs,
but it is probably a learning tool best suited for self-directed learning.


