---
id: 2041
title: Reduce the order of relatedness coefficients needed for many-player nonlinear games
date: 2026-03-19T04:44:54+00:00
author: nadiah_kristensen
layout: post
guid: http://nadiah.org/blog/?p=2041
permalink: /2025/03/19/degree-theorem-sketch
categories:
  - cooperation
---

In [a recent paper](https://nadiah.org/wp-content/uploads/2025/03/Kristensen25-Many_strategy_group_games_with_relatives_and_coordinated_cooperation.pdf)
(Kristensen, Chisholm, & Ohtsuki 2025),
we developed the mathematical tools needed to describe the evolution of discrete strategies 
in a many-player game with a nonlinear benefits function and relatedness between the players.
The key difficulty with this scenario is that one must account for the higher-order genetic associations 
beyond dyadic relatedness (Hamilton's $$r$$).
For example,
in a two-player game or many-player linear game, one need only account for the probability that two individuals sampled from the group are identical by descent (IBD),
but in many-player nonlinear games, 
one must account for larger samples and other IBD subset relationships, e.g., the probability that if 5 individuals are sampled, two are IBD.

In the appendix, we left an idea that Hisashi Ohtsuki had as a conjecture:
if the $$n$$-player game payoffs can be written as polynomial functions of the nonfocal strategy counts with degree $$\nu - 1$$
where $$\nu < n$$,
then the $$n$$-player game payoffs can be written as a sum of $$\nu$$-player game payoffs.
You can see he already thought about this idea in Ohtsuki (2014),
though there he had only the 2-strategy case, whereas here we deal with the many-strategy case.

The ability to write $$n$$-player payoffs as a sum of $$\nu$$-player payoffs 
is significant because it reduces the number of 
relatedness coefficients needed to parameterise the model:
the maximum order of relatedness coefficients needed reduces from $$n$$ to $$\nu$$.
We provided a worked example of how this works in Supplement C,
which generalises the more familiar case of the linear game.
The payoffs of a linear PGG can be written as polynomials of degree $$d=1$$ 
and can be written as a sum of games between two players;
so regardless of how large the group is,
it can be parameterised with only the relatedness coefficients up to order 2 (i.e., dyadic $$r$$).

In this blog post,
I offer a sketch of a proof of Hisashi's idea.

### Reframing the problem as a linear algebra problem

We consider a focal individual 
in an $$n$$-player game with $$m$$ strategies.
Denote the nonfocal player strategy composition 
$$\boldsymbol{g} = (g_1, \ldots, g_m)$$ 
where $$g_j$$ counts the number of nonfocal players pursuing strategy $$j$$
and $$\lvert g \rvert = \sum_j g_j = n-1$$.
In our previous paper, 
we denoted the nonfocal strategy composition by $$\boldsymbol{g}_{\text{nf}}$$,
but I am dropping the `nf' subscript here for brevity.

Because $$g_m = n - 1 - \sum_{j=1}^{m-1} g_j$$,
each $$\boldsymbol{g}$$ can be uniquely defined 
by its first $$m-1$$ elements.
Therefore,
the total number of possible nonfocal strategy compositions $$\boldsymbol{g}$$
is

$$
    T_n = \frac{(n+m-2)!}{(n-1)!(m-1)!} = \binom{n + m -2}{n-1}
    \label{Eq:T_n}
    \tag{1}
$$

For each focal-player strategy $$x$$,
given that
there are $$T_n$$ scenarios the focal player may find themselves in,
there are up to $$T_n$$ unique payoffs the focal player may receive.
Therefore, in general and for arbitrary payoffs,
a focal $$x$$-strategist's payoff 
can be written as a polynomial of degree $$n-1$$ 

$$
  \pi_{n}(x, \boldsymbol{g})
  = \sum_{\substack{\boldsymbol{k} \geq \boldsymbol{0} \\\ |\boldsymbol{k}| \leq n-1}} c_{x, \boldsymbol{k}} 
  \prod_{j=1}^{m-1} g_j^{k_j}
$$

This payoff polynomial has $$T_n$$ polynomial coefficients $$c_{x, \boldsymbol{k}}$$ 
with multi-indexes of the form
$$\boldsymbol{k} = (k_1, \ldots, k_{m-1})$$.

Define the degree of the $$x$$-strategist's payoff-polynomial as 

$$
    d_x = \text{max}(\{ \lvert \boldsymbol{k} \rvert \in \mathbb{Z}_{\geq 0} \mid c_{x, \boldsymbol{k}} \neq 0 \})
$$

and define the degree of the whole game

$$
    d = \text{max}(\{ d_x \in \mathbb{Z}_{\geq 0} \mid x \in \{ 1, \ldots, m \} \} )
$$

Let us now consider a game with degree $$d = \nu - 1 < n - 1$$,
such that every payoff can be written as a polynomial 

$$
  \pi_{n}(\boldsymbol{g}) 
  = \sum_{\substack{\boldsymbol{k} \geq \boldsymbol{0} \\\ |\boldsymbol{k}| \leq \nu-1}} c_{\boldsymbol{k}} 
  \prod_{j=1}^{m-1} g_j^{k_j}
  \label{Eq:general_payoff_polynomial}
    \tag{2}
$$

with $$T_{\nu} = \binom{\nu + m -2}{\nu-1}$$ coefficients.
Since the proof applies identically to each focal strategy $$x$$, 
I have dropped $$x$$ subscript for the remainder to keep the notation lighter. 

The payoff polynomial in Eq. \ref{Eq:general_payoff_polynomial}
can be written in matrix form 

$$
    \boldsymbol{\pi}_n = A \boldsymbol{c}
    \label{Eq:pi_n=Ac}
    \tag{3}
$$

where $$\boldsymbol{c}$$ is the $$T_{\nu} \times 1$$ column vector 
of polynomial coefficients $$c_{\boldsymbol{k}}$$,
and $$A$$ is a $$T_n \times T_{\nu}$$ matrix with elements

$$
    A_{\boldsymbol{g}, \boldsymbol{k}} = \prod_{j=1}^{m-1} g_j^{k_j}
    \label{Eq:A_elements}
    \tag{4}
$$

{% include content_highlight_grey.html content="
**Example 1.** Consider 
a group of size $$n = 4$$
playing a game with $$m = 3$$ strategies,
and consider a focal $$x$$-strategist
with the payoff polynomial 

$$
  \pi_{4}(\boldsymbol{g}) 
    = 3 g_{1}^2 + 4 g_{1} g_{2} - 3 g_{1} + 5 g_{2}^2 + 3 g_{2} + 9 
$$

The payoff polynomial has degree $$\nu - 1 = 2$$
with $$T_3 = 6$$ coefficients,
and the coefficients have
multi-indexes of the form $$\boldsymbol{k} = (k_1, k_2)$$ with the restriction 
$$\lvert \boldsymbol{k} \rvert \leq \nu-1 = 2$$.
The indexed coefficients correspond to the coefficients above as follows

$$
  \pi_{4}(\boldsymbol{g}) 
    = \underbrace{c_{(2, 0)}}_{3} g_{1}^2 
     + \underbrace{c_{(1, 1)}}_{4} g_{1} g_{2} 
     + \underbrace{c_{(1, 0)}}_{-3} g_{1} 
     + \underbrace{c_{(0, 2)}}_{5} g_{2}^2
     + \underbrace{c_{(0, 1)}}_{3} g_{2} 
     + \underbrace{c_{(0, 0)}}_{9} \\
$$

There are $$T_4 = 10$$ possible strategy compositions among the nonfocal players

$$
    \boldsymbol{g} \in \left\{ (3, 0, 0), (2, 1, 0), (2, 0, 1), (1, 2, 0),
    \ldots, (0, 1, 2), (0, 0, 3)\right\}
$$

Let us order the rows of $$A$$ and $$\boldsymbol{\pi}_4$$,
which correspond to different values of $$\boldsymbol{g}$$,
and the columns of $$A$$ and rows of $$\boldsymbol{c}$$, 
which correspond to multi-indexes $$\boldsymbol{k}$$,
in reverse lexicographical order. 
So the rows of $$A$$ from top to bottom are $$\boldsymbol{g}$$ equals:

$$
      (3,0,0), (2,1,0), (2,0,1), (1,2,0), (1,1,1), (1,0,2), (0,3,0), (0,2,1), (0,1,2), (0,0,3)
$$

And the columns of $$A$$ from left to right are $$\boldsymbol{k}$$ equals:

$$
      (2, 0), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)
$$

The focal payoffs can be calculated in matrix form 

$$
    \boldsymbol{\pi}_4 =
    \underbrace{
  \begin{bmatrix}
      9 & 0 & 3 & 0 & 0 & 1 \\
      4 & 2 & 2 & 1 & 1 & 1 \\
      4 & 0 & 2 & 0 & 0 & 1 \\
      1 & 2 & 1 & 4 & 2 & 1 \\
      1 & 1 & 1 & 1 & 1 & 1 \\
      1 & 0 & 1 & 0 & 0 & 1 \\
      0 & 0 & 0 & 9 & 3 & 1 \\
      0 & 0 & 0 & 4 & 2 & 1 \\
      0 & 0 & 0 & 1 & 1 & 1 \\
      0 & 0 & 0 & 0 & 0 & 1 \\
  \end{bmatrix}
    }_{A}
    \underbrace{
  \begin{bmatrix}
    3 \\ 4 \\ - 3 \\ 5 \\ 3 \\ 9 
  \end{bmatrix}
    }_{\boldsymbol{c}}
    = 
  \begin{bmatrix}
    27 \\ 31 \\ 15 \\ 43 \\ 21 \\  9 \\ 63 \\ 35 \\ 17 \\  9
  \end{bmatrix}
$$
" %}

We now consider the situation where,
instead of the focal playing all $$n-1$$ nonfocal individuals in a single $$n$$-player encounter,
the focal plays a $$\nu$$-player game with every $$\nu-1$$ subset of nonfocals
in $$\binom{n-1}{\nu-1}$$ separate encounters.

In the full $$n$$-player game,
the nonfocal strategy composition is $$\boldsymbol{g}$$ with 
$$\lvert \boldsymbol{g}\rvert = n - 1$$.
Denote the nonfocal strategy composition in a subgroup encounter by $$\boldsymbol{\gamma}$$.
Then the set of nonfocal subgroup strategy compositions encountered is

$$
  \Gamma_{\nu}(\boldsymbol{g}) =
    \left\{ 
      \boldsymbol{\gamma} \in \mathbb{Z}_{\geq 0}^m \;\middle|\; 
      \lvert \boldsymbol{\gamma} \rvert = \nu-1 \text{ and } \gamma_j \leq g_j \;\forall\, j \right\}
$$

An encounter with $$\boldsymbol{\gamma} \in \Gamma_{\nu}(\boldsymbol{g})$$ 
occurs with multiplicity given by the multivariate hypergeometric coefficient

$$
  B_{\boldsymbol{g}, \boldsymbol{\gamma}} = \prod_{i=1}^{m} \binom{g_i}{\gamma_i}
  \label{Eq:B_elements}
    \tag{5}
$$

{% include content_highlight_grey.html content="
**Example 2.** Continuing with Example 1 ($$n = 4$$, $$m=3$$),
consider a focal individual 
who plays a game with $$3$$ nonfocal individuals $$a$$, $$b$$, and $$c$$,
with strategies 1, 2, and 2, respectively.
The multiset of nonfocal strategies is $$[1, 2, 2]$$,
and the nonfocal strategy composition is $$\boldsymbol{g} = (1, 2, 0)$$.

If the focal individual were to instead play a game with every 
subset of $$2$$ nonfocal individuals,
then it would play once with each pair: $$\{a, b\}$$, $$\{a, c\}$$, and $$\{b, c\}$$.
The multisets of the nonfocal strategies would be 
$$[1, 2]$$,
$$[1, 2]$$,
and
$$[2, 2]$$, respectively;
and the nonfocal strategy compositions would be
$$\boldsymbol{\gamma} = (1, 1, 0)$$,
$$\boldsymbol{\gamma} = (1, 1, 0)$$,
and
$$\boldsymbol{\gamma} = (0, 2, 0)$$,
respectively.
" %}

Denote the payoffs in the $$\nu$$-player game by $$\pi_{\nu}(\boldsymbol{\gamma})$$.
We wish to prove that,
if every payoff in the $$n$$-player game can be written as a polynomial 
of degree $$\nu-1$$ (Eq. \ref{Eq:general_payoff_polynomial}),
then the $$n$$-player payoff can also be written as the sum of payoffs in some $$\nu$$-player game 

$$
    \pi_n(\boldsymbol{g}) = 
    \sum_{\boldsymbol{\gamma} \in \Gamma_{\nu}(\boldsymbol{g})}
    B_{\boldsymbol{g}, \boldsymbol{\gamma}} \; \pi_{\nu}(\boldsymbol{\gamma})
    \label{Eq:payoff_as_sum}
    \tag{6}
$$

Eq. \ref{Eq:payoff_as_sum} can be written in matrix form as

$$
    \boldsymbol{\pi}_n = B \boldsymbol{\pi}_{\nu}
    \label{Eq:pi_n=B pi_nu}
    \tag{7}
$$

where $$B$$ is a $$T_n \times T_{\nu}$$ matrix with elements given by Eq. \ref{Eq:B_elements},
and $$\boldsymbol{\pi}_{\nu}$$ is the $$T_{\nu} \times 1$$ column vector of payoffs 
in the $$\nu$$-player game.

{% include content_highlight_grey.html content="
**Example 3.** The payoffs to the focal $$x$$-strategist in the 4-player game 
from Example 1 can be written as a sum of $$3$$-player game payoffs

$$
    \pi_3((2, 0, 0)) = 9, \qquad
    \pi_3((1, 1, 0)) = 11, \qquad
    \pi_3((1, 0, 1)) = 3, 
$$

$$
    \pi_3((0, 2, 0)) = 21, \qquad
    \pi_3((0, 1, 1)) = 7, \qquad
    \pi_3((0, 0, 2)) = 3 
$$

Let us order the rows of $$B$$ and $$\boldsymbol{\pi}_4$$,
which correspond to different values of $$\boldsymbol{g}$$,
and the columns of $$B$$ and rows of $$\boldsymbol{\pi}_3$$, 
which correspond to different values of $$\boldsymbol{\gamma}$$,
in reverse lexicographical order. 
So the rows of $$B$$ from top to bottom are $$\boldsymbol{g}$$ equals:

$$
      (3,0,0), (2,1,0), (2,0,1), (1,2,0), (1,1,1), (1,0,2), (0,3,0), (0,2,1), (0,1,2), (0,0,3)
$$

And the columns of $$B$$ from left to right are $$\boldsymbol{\gamma}$$ equals:

$$
      (2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 2, 0), (0, 1, 1), (0, 0, 2)
$$

In matrix form, the 4-player game payoffs can be calculated

$$
  \boldsymbol{\pi}_{4} =
  \underbrace{
  \begin{bmatrix}
      3 & 0 & 0 & 0 & 0 & 0 \\
      1 & 2 & 0 & 0 & 0 & 0 \\
      1 & 0 & 2 & 0 & 0 & 0 \\
      0 & 2 & 0 & 1 & 0 & 0 \\
      0 & 1 & 1 & 0 & 1 & 0 \\
      0 & 0 & 2 & 0 & 0 & 1 \\
      0 & 0 & 0 & 3 & 0 & 0 \\
      0 & 0 & 0 & 1 & 2 & 0 \\
      0 & 0 & 0 & 0 & 2 & 1 \\
      0 & 0 & 0 & 0 & 0 & 3 
  \end{bmatrix}
    }_{B}
  \underbrace{
    \begin{bmatrix} 9 \\ 11 \\ 3 \\ 21 \\ 7 \\ 3 \end{bmatrix}
  }_{\boldsymbol{\pi}_{3}}
    = \begin{bmatrix} 27 \\ 31 \\ 15 \\ 43 \\ 21 \\ 9 \\ 63 \\ 35 \\ 17 \\ 9 \end{bmatrix}
$$
" %}

### Proof sketch

#### Theorem

{% include content_highlight.html content="
Consider an $$n$$-player game with $$m$$ strategies in which every focal $$x$$-strategist's payoff $$\pi_n(x, \boldsymbol{g})$$ 
can be written as a polynomial function of the nonfocal strategy counts $$\boldsymbol{g}$$ with degree $$\nu - 1$$.
Then there exists a $$\nu$$-player game with payoffs $$\pi_\nu(x, \boldsymbol{\gamma})$$ such that

$$
    \pi_n(x, \boldsymbol{g}) = \sum_{\boldsymbol{\gamma} \in \Gamma_\nu(\boldsymbol{g})} B_{\boldsymbol{g}, \boldsymbol{\gamma}} \; \pi_\nu(x, \boldsymbol{\gamma})
$$

for all focal strategies $$x$$ and nonfocal compositions $$\boldsymbol{g}$$.
" %}

#### Overview of the proof

We wish to show that,
if $$\boldsymbol{\pi}_n = A \boldsymbol{c}$$,
then $$\boldsymbol{\pi}_n = B \boldsymbol{\pi}_{\nu}$$ has a solution.
This is also a columnspace containment problem:
we wish to show that
$$\boldsymbol{\pi}_n \in \text{col}(A) \implies \boldsymbol{\pi}_n \in \text{col}(B)$$,
or $$\text{col}(A) \subseteq \text{col}(B)$$.
We will prove it directly through factorisation.
We will find a matrix $$C$$ such that

$$
    \boldsymbol{\pi}_n = A \boldsymbol{c} = 
    B \underbrace{C \boldsymbol{c}}_{\boldsymbol{\pi}_{\nu}}
$$

#### Proof sketch

We wish to relate columns of $$A$$ with elements of the form $$\prod g_j^{k_j}$$ 
to columns of $$B$$ with elements of the form $$\prod \binom{g_j}{\gamma_j}$$.
The monomials in $$A$$ can be expressed as a sum of falling factorials

$$
  g_j^{k_j} = \sum_{r=0}^{k_j} S(k_j, r)\, r!\, \binom{g_j}{r}
    \tag{8}
$$

where $$S$$ are Stirling numbers of the second kind.
Therefore,
each element of $$A$$

$$
\begin{align}
    A_{\boldsymbol{g}, \boldsymbol{k}} 
  &= \prod_{j=1}^{m-1} g_j^{k_j} \nonumber \\
  & = \prod_{j=1}^{m-1} \left(\sum_{r_j=0}^{k_j} S(k_j, r_j)\, r_j!\, \binom{g_j}{r_j}\right) \nonumber \\
  &= \sum_{r_1=0}^{k_1} \sum_{r_2=0}^{k_2} \cdots \sum_{r_{m-1}=0}^{k_{m-1}} \prod_{j=1}^{m-1} S(k_j, r_j)\, r_j!\, \binom{g_j}{r_j} \nonumber \\
  &= \sum_{\boldsymbol{r} \leq \boldsymbol{k}}
    \left(\prod_{j=1}^{m-1} S(k_j, r_j)\, r_j!\right)
    \prod_{j=1}^{m-1}\binom{g_j}{r_j}
    \label{eq:monomial_stirling}
    \tag{9}
\end{align}
$$

where $$\boldsymbol{k} = (k_1, \ldots, k_{m-1})$$, $$\boldsymbol{r} = (r_1, \ldots, r_{m-1})$$,
and $$\boldsymbol{r} \leq \boldsymbol{k}$$ means $$0 \leq r_j \leq k_j$$ for every $$j$$.

We're aiming to get a term on the right-hand side that looks like 
$$\prod_{i=1}^m \binom{g_i}{\gamma_i}$$,
and we have two issues to deal with.
First, 
the product in Eq. \ref{eq:monomial_stirling} only goes to $$m-1$$ not $$m$$.
We can resolve this by defining $$r_m \equiv 0$$,
which allows us to extend the product to $$\prod_{j=1}^{m}\binom{g_j}{r_j}$$
by introducing only a $$\binom{g_m}{0} = 1$$ term that does not change the result.


The second issue is that $$\prod \binom{g_j}{r_j}$$ describes choosing $$|\boldsymbol{r}| = s$$ players,
but we want to relate that to $$\prod \binom{g_j}{\gamma_j}$$ that chooses $$\lvert \boldsymbol{\gamma} \rvert = \nu-1$$ players,
so there is a `gap' of $$\nu - 1 - s$$ that we need to bridge.
We can resolve this by treating the $$\boldsymbol{r}$$ as fixed,
and considering all possible $$\boldsymbol{\ell}$$ additional players we could choose 
that complete the choice to obtain a valid $$\boldsymbol{\gamma}$$.
Using the generalisation of Vandermonde's identity allows us to distribute the 
remaining $$\nu - 1 - s$$ choices across the $$m$$ components of the remaining $$\boldsymbol{g} - \boldsymbol{r}$$
(see Example 4 for a concrete illustration).

The generalisation of Vandermonde's identity is

$$
  { a_1+\dots +a_p \choose c }= \sum_{b_1+\cdots +b_p = c} \: \prod_{j=1}^p {a_j\choose b_j} 
$$

We know $$\lvert \boldsymbol{g} \rvert = n - 1$$
and $$\lvert \boldsymbol{\gamma} \rvert = \nu - 1$$.
- Define $$s \equiv \lvert \boldsymbol{r} \rvert$$ 
- Define $$\ell_j \equiv \gamma_j - r_j$$ 
    with the constraint $$\ell_j \geq 0$$ for all $$j$$,
    which also gives $$\lvert \boldsymbol{\ell} \rvert = \nu - 1 - s$$.

Setting $$a_j = g_j - r_j$$ and noting $$\sum_j (g_j - r_j) = n - 1 - s$$,
Vandermonde's identity gives

$$
  \binom{n-1-s}{\nu-1-s}
  = 
  \sum_{\substack{\boldsymbol{\ell} \geq 0 \\\ |\boldsymbol{\ell}| = \nu-1-s}}
  \prod_{j=1}^m \binom{g_j - r_j}{\ell_j}
  \label{Eq:post_vander}
    \tag{10}
$$

Multiply both sides of Eq. \ref{Eq:post_vander}
by $$\prod_j \binom{g_j}{r_j}$$ to obtain

$$
  \binom{n-1-s}{\nu-1-s} 
  \prod_{j=1}^m \binom{g_j}{r_j}
  = \sum_{\substack{\boldsymbol{\ell} \geq 0 \\\ |\boldsymbol{\ell}| = \nu-1-s}}
  \prod_{j=1}^m \binom{g_j - r_j}{\ell_j} \binom{g_j}{r_j}
$$

Each factor in the product has the form $$\binom{g_j - r_j}{\ell_j} \binom{g_j}{r_j}$$.
Applying the identity $$\binom{a-b}{c-b}\binom{a}{b} = \binom{a}{c}\binom{c}{b}$$
with $$a = g_j$$, $$b = r_j$$, and $$c = r_j + \ell_j$$ gives

$$
  \binom{n-1-s}{\nu-1-s} 
  \prod_{j=1}^m \binom{g_j}{r_j}
  = \sum_{\substack{\boldsymbol{\ell} \geq 0 \\\ |\boldsymbol{\ell}| = \nu-1-s}}
  \prod_{j=1}^m \binom{g_j}{r_j + \ell_j} \binom{r_j + \ell_j}{r_j}
  \label{Eq:no_gammas_yet}
  \tag{11}
$$

Reverse the substitutions made to return Eq. \ref{Eq:no_gammas_yet}
to an expression in terms of $$\boldsymbol{\gamma}$$
- Definition $$\ell_j \equiv \gamma_j - r_j \implies r_j + \ell_j = \gamma_j$$
- Constraint $$\boldsymbol{\ell} \geq 0 \implies \boldsymbol{\gamma} \geq \boldsymbol{r}$$ 
- Substitution: $$\lvert \boldsymbol{\ell} \rvert = \nu - 1 - s = \lvert \boldsymbol{\gamma} \rvert - s
      \rightarrow \lvert \boldsymbol{\gamma} \rvert = \nu - 1$$.

Then rearrange

$$
  \prod_{j=1}^m \binom{g_j}{r_j}
  = 
  \frac{1}{\binom{n-1-s}{\nu-1-s}}
  \sum_{\substack{\boldsymbol{\gamma} \geq \boldsymbol{r} \\\ |\boldsymbol{\gamma}| = \nu-1}}
  \prod_{j=1}^m \binom{\gamma_j}{r_j}
  \prod_{j=1}^m \binom{g_j}{\gamma_j}
  \label{Eq:second_part}
    \tag{12}
$$

Note that $$\binom{g_j}{\gamma_j} = 0$$ whenever $$\gamma_j > g_j$$, so the sum is effectively restricted to $$\boldsymbol{\gamma} \in \Gamma_\nu(\boldsymbol{g})$$.

{% include content_highlight_grey.html content="
**Example 4.** Continuing with Examples 1 and 3 ($$n = 4$$, $$m = 3$$, $$\nu = 3$$),
consider the situation where $$\boldsymbol{g} = (2, 1, 0)$$ 
and we are considering the sum term with 
$$\boldsymbol{r} = (1, 0, 0)$$.
We have

$$
    \prod_{j=1}^{3} \binom{g_j}{r_j}
    = \binom{2}{1}\binom{1}{0}\binom{0}{0} = 2
$$

This product selects $$s = \lvert \boldsymbol{r} \rvert = 1$$ player from the nonfocals,
but we need to match it with a scenario that selects $$\lvert \boldsymbol{\gamma} \rvert = \nu - 1 = 2$$.
The gap is $$\nu - 1 - s = 1$$,
so we must select one more player from the remaining pool
$$\boldsymbol{g} - \boldsymbol{r} = (1, 1, 0)$$.

**Vandermonde step.**
There are two possibilities to select one more player,
and each completes a
$$\boldsymbol{\gamma} = \boldsymbol{r} + \boldsymbol{\ell}$$ 
with $$\lvert \boldsymbol{\gamma} \rvert = 2$$ as required

$$
\begin{align*}
    \boldsymbol{\ell} = (1, 0, 0) 
        & \text{ completes } \boldsymbol{\gamma} = (2, 0, 0) \\
    \boldsymbol{\ell} = (0, 1, 0) 
        & \text{ completes } \boldsymbol{\gamma} = (1, 1, 0)
\end{align*}
$$

These completions are all $$\boldsymbol{\ell} \geq \boldsymbol{0}$$
with $$\lvert \boldsymbol{\ell} \rvert = 1$$
and $$\boldsymbol{\ell} \leq \boldsymbol{g} - \boldsymbol{r} = (1, 1, 0)$$.

We can verify Vandermonde's identity (Eq. \ref{Eq:post_vander}) here directly

$$
        \underbrace{
            \binom{1}{1}\binom{1}{0}\binom{0}{0}
        }_{\boldsymbol{\ell} = (1,0,0)}
    +
        \underbrace{
            \binom{1}{0}\binom{1}{1}\binom{0}{0}
        }_{\boldsymbol{\ell} = (0,1,0)}
    = 1 + 1 = 2
    = \binom{n-1-s}{\nu-1-s} = \binom{2}{1}
$$

**Binomial identity step.**
After multiplying both sides by $$\prod_j \binom{g_j}{r_j}$$,
each term in the sum is a product of terms of the form
$$\binom{g_j}{r_j} \binom{g_j - r_j}{\ell_j}$$.
Applying the identity 
$$\binom{a}{b} \binom{a-b}{c-b} = \binom{c}{b} \binom{a}{c}$$
converts
$$\binom{g_j}{r_j} \binom{g_j - r_j}{\ell_j}$$ terms 
to $$\binom{g_j}{\gamma_j} \binom{\gamma_j}{r_j}$$ terms.

For $$\boldsymbol{\ell} = (1, 0, 0)$$
that completes $$\boldsymbol{\gamma} = (2, 0, 0)$$

$$
    \underbrace{
        \binom{2}{1} \binom{1}{1}
    }_{j=1}
    \underbrace{
        \binom{1}{0} \binom{1}{0}
    }_{j=2}
    \underbrace{
        \binom{0}{0} \binom{0}{0}
    }_{j=3}
    \;=\;
    \underbrace{
        \binom{2}{2} \binom{2}{1}
    }_{j=1}
    \underbrace{
        \binom{1}{0} \binom{0}{0}
    }_{j=2}
    \underbrace{
        \binom{0}{0} \binom{0}{0}
    }_{j=3}
$$

and similarly for $$\boldsymbol{\ell} = (0, 1, 0)$$
that completes $$\boldsymbol{\gamma} = (1, 1, 0)$$

$$
    \underbrace{
        \binom{2}{1} \binom{1}{0}
    }_{j=1}
    \underbrace{
        \binom{1}{0} \binom{1}{1}
    }_{j=2}
    \underbrace{
        \binom{0}{0} \binom{0}{0}
    }_{j=3}
    \;=\;
    \underbrace{
        \binom{2}{1} \binom{1}{1}
    }_{j=1}
    \underbrace{
        \binom{1}{1} \binom{1}{0}
    }_{j=2}
    \underbrace{
        \binom{0}{0} \binom{0}{0}
    }_{j=3}
$$

Grouping the $$\binom{g_j}{\gamma_j}$$ terms 
and $$\binom{\gamma_j}{r_j}$$ terms together and rearranging (Eq. \ref{Eq:second_part})

$$
\begin{align*}
    \prod_{j=1}^3 \binom{g_j}{r_j}
    &= \frac{1}{\binom{2}{1}}
    \bigg[
        \underbrace{\binom{2}{2}\binom{1}{0}\binom{0}{0}}_{
            B_{\boldsymbol{g},(2,0,0)} \,=\, 1}
        \cdot
        \underbrace{\binom{2}{1}\binom{0}{0}\binom{0}{0}}_{\text{into } C}
        \;+\;
        \underbrace{\binom{2}{1}\binom{1}{1}\binom{0}{0}}_{
            B_{\boldsymbol{g},(1,1,0)} \,=\, 2}
        \cdot
        \underbrace{\binom{1}{1}\binom{1}{0}\binom{0}{0}}_{\text{into } C}
    \bigg] \\
    &= \frac{1}{2}\big[1 \cdot 2 + 2 \cdot 1\big] 
\end{align*}
$$

which matches our first calculation.
Importantly, the $$B_{\boldsymbol{g},\boldsymbol{\gamma}}$$ terms match the entries of $$B$$ from Example 3
(row 2 columns 1 and 2) illustrating how this procedure obtains the matrix factorisation $$A = BC$$.
" %}

We can now obtain an explicit matrix $$C$$.
Substituting Eq. \ref{Eq:second_part} into Eq. \ref{eq:monomial_stirling}

$$
\begin{align*}
    \underbrace{\prod_{j=1}^{m-1} g_j^{k_j}}_{A_{\boldsymbol{g}, \boldsymbol{k}}}
  &= \sum_{\boldsymbol{r} \leq \boldsymbol{k}}
    \frac{1}{\binom{n-1- \lvert \boldsymbol{r} \rvert}{\nu-1- \lvert \boldsymbol{r} \rvert}}
    \left(\prod_{j=1}^{m-1} S(k_j, r_j)\, r_j!\right)
  \sum_{\substack{\boldsymbol{\gamma} \geq \boldsymbol{r} \\\ |\boldsymbol{\gamma}| = \nu-1}}
  \prod_{j=1}^m \binom{\gamma_j}{r_j}
  \prod_{j=1}^m \binom{g_j}{\gamma_j} \\
  &= \sum_{\lvert \boldsymbol{\gamma} \rvert = \nu-1}
  \underbrace{\prod_{j=1}^m \binom{g_j}{\gamma_j}}_{B_{\boldsymbol{g},\boldsymbol{\gamma}}}
  \:
  \underbrace{
  \sum_{\substack{\boldsymbol{r} \leq \boldsymbol{k} \\ \boldsymbol{r} \leq \boldsymbol{\gamma}}}
    \frac{1}{\binom{n-1- \lvert \boldsymbol{r} \rvert}{\nu-1- \lvert \boldsymbol{r} \rvert}}
    \left(\prod_{j=1}^{m-1} S(k_j, r_j)\, r_j!\right)
  \prod_{j=1}^m \binom{\gamma_j}{r_j}
}_{C_{\boldsymbol{\gamma}, \boldsymbol{k}}}
\end{align*}
$$

which is a matrix product.

We can tidy the expression for $$C_{\gamma, k}$$ using the following:
- Recall $$r_m \equiv 0$$, 
  so $$\binom{\gamma_m}{r_m} = \binom{\gamma_m}{0} = 1$$,
  and the $$\prod_{j=1}^m \binom{\gamma_j}{r_j}$$ term can be truncated and
  brought into the Stirling product.
- By defining $$h_j \equiv \text{min}(k_j, \gamma_j)$$
  and $$\boldsymbol{h} = (h_1, \ldots, h_{m-1})$$,
      the two conditions $$\boldsymbol{r} \leq \boldsymbol{k}$$ 
    and $$\boldsymbol{r} \leq \boldsymbol{\gamma}$$ can be merged into 
    $$\boldsymbol{r} \leq \boldsymbol{h}$$.
- The denominator can be simplified with
      $$\binom{n-1- \lvert \boldsymbol{r} \rvert}{\nu-1- \lvert \boldsymbol{r} \rvert} = \binom{n-1- \lvert \boldsymbol{r} \rvert}{n - \nu}$$.
- The falling factorial of $$\gamma_j$$ can be written more compactly 
  $$r_j! \binom{\gamma_j}{r_j} = (\gamma_j)_{r_j}$$.

Thus, $$C$$ is a $$T_{\nu} \times T_{\nu}$$ matrix with elements

$$
  C_{\gamma, k} 
  = \sum_{\boldsymbol{r} \leq \boldsymbol{h}}
    \frac{
        1
    }{ 
      \binom{n-1- \lvert \boldsymbol{r} \rvert}{n - \nu}
    } 
    \prod_{j=1}^{m-1} 
      S(k_j, r_j)\, (\gamma_j)_{r_j}
$$

### Computationally efficient way to obtain payoffs in the subgroup game

For computation purposes,
we can group $$s = \lvert \boldsymbol{r} \rvert$$ terms

$$
  C_{\gamma, k} 
  = \sum_{s=0}^{\lvert \boldsymbol{h} \rvert}
    \frac{
      F_s
    }{ 
      \binom{n-1- s}{n - \nu}
    } 
$$

where $$F_s$$ is a convolution

$$
  F_s = 
    \sum_{\substack{\boldsymbol{r} \leq \boldsymbol{h} \\ \lvert \boldsymbol{r} \rvert = s}}
    \prod_{j=1}^{m-1} 
      S(k_j, r_j)\, (\gamma_j)_{r_j}
$$

Define polynomials

$$
  P_j(z) = 
    \sum_{r_j = 0}^{h_j} S(k_j, r_j)\, (\gamma_j)_{r_j} \, z^{r_j}
$$

Then $$F_s$$ is the $$z^s$$ coefficient of their product

$$
  F_s = [z^s] \prod_{j=1}^{m-1} P_j(z)
$$

{% include content_highlight_grey.html content="
**Example 5.** The payoffs to the focal $$x$$-strategist in the 4-player game 
from Example 1 can be written as a sum of $$3$$-player game payoffs,
and those payoffs can be calculated using $$C$$ and $$\boldsymbol{c}$$.

Let us order the rows of $$C$$ and $$\boldsymbol{\pi}_3$$,
which correspond to different values of $$\boldsymbol{\gamma}$$,
and the columns of $$C$$ and rows of $$\boldsymbol{c}$$, 
which correspond to different values of $$\boldsymbol{k}$$,
in reverse lexicographical order. 
So the rows of $$C$$ from top to bottom are $$\boldsymbol{\gamma}$$ equals:

$$
      (2,0,0), (1,1,0), (1,0,1), (0,2,0), (0,1,1), (0,0,2)
$$

And the columns of $$C$$ from left to right are $$\boldsymbol{k}$$ equals

$$
      (2, 0), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)
$$

In matrix form, the 3-player game payoffs can be calculated

$$
  \boldsymbol{\pi}_{3} =
  \underbrace{
  \begin{bmatrix}
       3 & 0 & 1 & 0 & 0 & 1/3 \\
       1/2 & 1 & 1/2 & 1/2 & 1/2 & 1/3 \\
       1/2 & 0 & 1/2 & 0 & 0 & 1/3 \\
       0 & 0 & 0 & 3 & 1 & 1/3 \\
       0 & 0 & 0 & 1/2 & 1/2 & 1/3 \\
       0 & 0 & 0 & 0 & 0 & 1/3 
  \end{bmatrix}
  }_{C}
    \underbrace{
  \begin{bmatrix}
    3 \\ 4 \\ - 3 \\ 5 \\ 3 \\ 9 
  \end{bmatrix}
    }_{\boldsymbol{c}}
  =
    \begin{bmatrix} 9 \\ 11 \\ 3 \\ 21 \\ 7 \\ 3 \end{bmatrix}
$$
" %}

The script below produces the example.

```python
# Example: A four-player game that is an aggregation of three-player games
#
# -- 

import itertools as it
from math import prod, factorial
from scipy.special import comb, stirling2
import numpy as np
import time


def bounded_compositions(n, m):
    """
    Yield all tuples of length m-1 with non-negative integer entries
    summing to at most n-1.
    """
    S = n - 1  # max sum
    p = m  # m-1 real parts + 1 slack part
    for c in it.combinations(range(S + p - 1), p - 1):
        # Recover parts from the combination of "divider" positions
        parts = tuple(c[i] - c[i - 1] - 1 if i > 0 else c[0] for i in range(p - 1))
        # parts has length m-1 (we drop the implicit slack variable)
        yield parts


# ----

# generate worked example
# ===

# parameters
# ---

# nbr players in the full game
n = 4

# nbr players in the smaller game
nu = 3

# nbr strategies
m = 3

# I will need to hardcode in here the actual coefficients
k_2_coeff = {
    (3, 0): 0,
    (2, 1): 0,
    (2, 0): 3,
    (1, 2): 0,
    (1, 1): 4,
    (1, 0): -3,
    (0, 3): 0,
    (0, 2): 5,
    (0, 1): 3,
    (0, 0): 9,
}

# list all non-focal strategy distributions for n-player game
# and all corresponding non-focal strategy distributions for nu-player game
# with the multiplicity of each nu-player game
# ---

# all non-focal strategy compositions for n-player game
all_outcomes = list(it.combinations_with_replacement(range(m), n - 1))
gs = [
    tuple([outcome.count(s) for s in range(m)]) for outcome in all_outcomes
]

# all non-focal strategy compositions for nu-player game
all_outcomes = list(it.combinations_with_replacement(range(m), nu - 1))
gammas = [
    tuple([outcome.count(s) for s in range(m)]) for outcome in all_outcomes
]

# for each full game, find the relevant subgames and their multiplicity
g_2_gammas = {g: list() for g in gs}
for g in gs:
    # identify relevant subgames
    for gamma in gammas:
        if all(
            [
                gamma_i <= g_i
                for gamma_i, g_i in zip(gamma, g)
            ]
        ):
            # append to dictionary
            g_2_gammas[g].append(gamma)

# useful dictionaries and indexing
idx_2_g = dict(enumerate(gs))
idx_2_gamma = dict(enumerate(gammas))
gamma_2_idx = {
    gamma: idx for idx, gamma in enumerate(gammas)
}

nbr_gs = len(gs)
nbr_gammas = len(gammas)

# calculate the payoff to focal in n-player game
# ---

g_2_pay = [
    sum(
        coeff * prod(g_j**pwr_j for g_j, pwr_j in zip(g[:-1], k))
        for k, coeff in k_2_coeff.items()
    )
    for g in gs
]

# write out the matrix A that was used for that calculation
# ---

# create an index of non-zero coefficients
ks = [k for k, coeff in k_2_coeff.items() if coeff != 0]
idx_2_k = dict(enumerate(ks))

A = np.zeros((nbr_gs, len(ks)), dtype=int)
for row, g in idx_2_g.items():
    for col, k in idx_2_k.items():
        A[row, col] = prod(g_j**pwr_j for g_j, pwr_j in zip(g[:-1], k))

# check the matrix multiplication gives the correct payoffs
coeff_vect = np.array([k_2_coeff[k] for k in ks])
pays = A @ coeff_vect

# -- correct payoffs


# create the matrix B that is used to solve the payoffs in the nu-player game
# ---

B = np.zeros((nbr_gs, nbr_gammas), dtype=int)
for row, g in idx_2_g.items():
    for gamma in g_2_gammas[g]:
        col = gamma_2_idx[gamma]
        B[row, col] = prod(
            [
                comb(g_i, gamma_i, exact=True)
                for g_i, gamma_i in zip(g, gamma)
            ]
        )
# -- gives the correct B that I found by hand


# Get C
# ===

t0 = time.time()
nbr_ks = len(ks)
C = np.zeros((nbr_gammas, nbr_ks))

for col, k in enumerate(ks):

    for row, gamma in enumerate(gammas):
        
        h = [min((k_i, gamma_i)) for k_i, gamma_i in zip(k, gamma[:-1])]
        rs = list(it.product(*[range(hi + 1) for hi in h]))
        
        c = 0
        for r in rs:

            # binomial fraction term
            sum_r = sum(r)
            bin_denom = comb(n - 1 - sum_r, n - nu, exact=True)

            # stirling product term
            stir_term = prod(
                    stirling2(k[j], r[j], exact=True) * factorial(r[j]) for j in range(m - 1)
            )
            
            # product term (omit last bc it's just 1)
            prod_term = prod(comb(gamma[j], r[j], exact=True) for j in range(m-1))
            
            # add to relevant coefficient
            c += stir_term * prod_term / bin_denom

        # store 
        C[row, col] = c

print("Verify A = BC")
print("A = ")
print(A)
print("BC = ")
print(B @ C)
print(f"time taken: {time.time() - t0}")


# Get C using convolution approach
# ===

t0 = time.time()
nbr_ks = len(ks)
C = np.zeros((nbr_gammas, nbr_ks)) 

for col, k in enumerate(ks):

    for row, gamma in enumerate(gammas):

        # list of lists of polynomial coefficients, rows are poly_j and cols are r-value (power)
        coeffsV = list()
        for j in range(m-1):
            h_j = min((k[j], gamma[j]))
            coeffs = [
                stirling2(k[j], r, exact=True)
                * factorial(r)
                * comb(gamma[j], r, exact=True)
                for r in range(h_j + 1)
            ]
            coeffsV.append(coeffs)
            
        # perform the convolution, get coefficient of product of polynomials
        product_coeffs = [1]
        for coeffs in coeffsV:
            product_coeffs = np.convolve(product_coeffs, coeffs)
        
        # store 
        C[row, col] = sum(
            product_coeff / comb(n - 1 - s, n - nu, exact=True)
            for s, product_coeff in enumerate(product_coeffs)
        )

print("Verify A = BC")
print("A = ")
print(A)
print("BC = ")
print(B @ C)
print(f"time taken: {time.time() - t0}")


# Use C to get the payoffs in the three-player games
# ===

# pi_3 = C c
pays_nu = C @ coeff_vect
print("\nVerify the payoffs in the three-player game:")
print(pays_nu)
# -- correct
```

### References

Kristensen, N.P., Chisholm, R.A., and Ohtsuki, H. (2025) Many-strategy games in groups with relatives and the evolution of coordinated cooperation, *J. Theor. Biol.*, **605**:112089

Ohtsuki, H., 2014. Evolutionary dynamics of n-player games played by relatives. *Philos. Trans. R. Soc. B*, **369** (1642):20130359.
