---
id: 2012
title: Using coalescence models to approximate interaction probabilities in weak selection
date: 2022-02-01T04:44:54+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=2012
permalink: /2021/02/01/antal-weak-selection
image: /wp-content/uploads/2022/02/antal.png
categories:
  - cooperation
---

To calculate the conditions under which selection favours cooperation, 
[Antal et al. (2009)](https://www.pnas.org/doi/pdf/10.1073/pnas.0902528106)
used interaction probabilities calculated from a coalescence model. However, a coalescence model
is a neutral model, it assumes no selective differences between types. So why can they assume _no
selective difference_ between types in a _selective model_? The purpose of this blog post is to explore the
explanation detailed in their SI.

First, a quick overview of the paper. The model involves the simultaneous evolution of two traits:
(1) the strategy in a one-shot Prisoner’s Dilemma, either Cooperate or Defect; and (2) a phenotypic
tag, modelled as an integer from $$-\infty$$ to $$\infty$$. Both the tag and strategy are inherited clonally with
a small chance of mutation, which means individuals who have the same tag are likely to have the
same strategy. The correlation between tag and strategy favours the evolution of cooperation, similar
to the Green Beard concept. If Cooperators only cooperate with other individuals who have the
same tag as themselves, that reduces their chances of being taken advantage of by Defectors. Before
this paper, most tag-based models had found that it was difficult to obtain cooperation for well-
mixed populations, suggesting that some spatial structure was needed. In this paper, however, they
investigate a well-mixed population, and discover a simple benefits/costs condition for cooperation to
evolve: $$\frac{b}{c} > 1 + \frac{2}{\sqrt{3}}$$.


They assume a Cooperator only cooperates with a matching-tag partner,
paying cost $$c$$ to provide a benefit $$b$$ to the partner;
otherwise, it behaves like a Defector.
The Defector contributes nothing;
it receives $$b$$ from a partner who cooperators and $$0$$ from a partner who defects.
Let $$m_i$$ be the number of Cooperators and $$n_i$$ be the total number of individuals
(Cooperators + Defectors) with tag $$i$$.
The average payoff to a Cooperator is the total payoff divided by the number of Cooperators

$$
    f_C = \frac{\sum_i m_i (b m_i - c n_i)}{\sum_i m_i},
$$

and similarly for Defectors

$$
    f_D = \frac{\sum_i (n_i - m_i) b m_i }{N - \sum_i m_i}.
$$

Selection favours cooperation if Cooperators have higher fitness than Defectors,
$$f_C > f_D$$, which is

$$
    b \sum_i m_i^2 - c \sum_i m_i n_i > \frac{(b-c)}{N} \sum_{ij} m_i m_j n_j.
    \label{single_s_condition}
    \tag{1}
$$

Eq. \ref{single_s_condition} is the equation for a single configuration of the
population $$s = (\mathbf{m}, \mathbf{n})$$.
In order to find the condition for evolution of cooperation overall,
we must average this condition over every possible population configuration $$s$$.
Let $$\pi(s)$$ be the probability that the population finds itself in configuration $$s$$.
We'll indicate the averaging by angle brackets, i.e.,

$$
    \langle \bullet \rangle = \sum_s \bullet \: \pi(s)
$$

Then the condition for the evolution of cooperation is

$$
    b \Bigg \langle \sum_i m_i^2 \Bigg \rangle - c \Bigg \langle \sum_i m_i n_i \Bigg \rangle > \frac{(b-c)}{N} \Bigg \langle \sum_{ij} m_i m_j n_j \Bigg \rangle.
    \tag{Ant.1}
    \label{Ant.1}
$$

The terms in the angle brackets look like they'd be proportional to probabilities:
the probability of drawing two cooperators with the same tag,
the probability of drawing a cooperator and any other with the same tag,
and a more complicated probability involving three types.

So far, so good.

However,
they say that they are "Averaging these quantities over every possible configuration of the population,
_weighted by their stationary probability under neutrality_" (emphasis added).
So, if we define every possible population configuration at the neutral-model steady state,
$$\pi^{(0)}(s)$$,
and indicate this average by a subscript 0, i.e.,

$$
    \langle \bullet \rangle_0 = \sum_s \bullet \: \pi^{(0)}(s)
$$

then, in fact, they are evaluating

$$
    b \Bigg \langle \sum_i m_i^2 \Bigg \rangle_0 - c \Bigg \langle \sum_i m_i n_i \Bigg \rangle_0 > \frac{(b-c)}{N} \Bigg \langle \sum_{ij} m_i m_j n_j \Bigg \rangle_0.
    \label{avg_at_ss}
    \tag{2}
$$

Why is it possible to replace the full averaging in Eq. \ref{Ant.1} with the averaging at the neutral steady state
in Eq. \ref{avg_at_ss}?
The answer is given in their SI.

In the SI in Section 3,
for a given population configuration $$s$$,
they derive the fitness of the Cooperator with tag $$i$$.
Start with the effective payoffs:

$$
    f_{C,i} = 1 + \delta (b m_i - c n_i)
$$

$$
    f_{D,i} = 1 + \delta b m_i
$$

Assume that every individual interacts with every individual once per generation.
Then, the fitness of the Cooperator

$$
\begin{align}
    w_{C,i}
    &= \frac{\text{payoff to Cooperator with tag }i}{\text{payoff to all Cooperators} + \text{payoff to all Defectors}} \\
    &= \frac{N f_{C,i}}{\sum_j m_j f_{C,j} + (n_j - m_j) f_{D,j}} \\
    &= \frac{1 + \delta(b m_i - c n_i)}{1 + \frac{\delta(b-c)}{N} \sum_j m_j n_j}
\end{align}
$$

For brevity, define $$A = b m_i - c n_i$$ and $$B = \frac{(b-c)}{N} \sum_j m_j n_j$$.
Do a Taylor expansion around $$a = 0$$

$$
\begin{align}
    w_{C,i}(\delta) &= w_{C,i}(a) + w_{C,i}'(a)(\delta-a) + \frac{w_{C,i}''(a)}{2} (\delta-a)^2 + \ldots \nonumber \\
    &= \frac{1+a A}{1+a B} + \left( \frac{A}{Ba + 1} - \frac{B(Aa + 1)}{(B a + 1)^2} \right) (\delta - a) + \mathcal(O)(\delta^2) \nonumber \\
    &= 1 + \delta(A-B) + \mathcal{O}(\delta^2) \nonumber \\
    &= 1 + \delta \left( bm_i -cn_i - \frac{b-c}{N} \sum_j m_j n_j \right) + \mathcal{O}(\delta^2)
    \tag{Ant.SI.30}
    \label{Ant.SI30}
\end{align}
$$

We can verify that, when selection $$\delta = 0$$, the Cooperator's fitness $$w_{C,i} = 1$$, as we'd hope.

For selection to favour Cooperators,
the average change in the proportion of Cooperators due to selection must be greater than zero, i.e.,

$$
    \langle \Delta p(s) \rangle > 0.
    \label{invasion_condition}
    \tag{3}
$$

For a given population configuration

$$
\begin{align}
    \Delta p(s)
    &= \frac{1}{N} \left( \text{number of Cooperator offspring born} - \text{number of Cooperator adults died} \right) \nonumber \\
    &= \frac{1}{N} \left( \sum_i m_i w_{C,i} - \sum_i m_i \right)
\end{align}
$$

We can again verify that, when selection $$\delta = 0$$, the change due to selection equals 0.
$$\Delta p(s)$$ has the Taylor expansion

$$
    \Delta p(s) = 0+ \frac{\delta}{N} \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0} + \mathcal{O}(\delta^2)
    \tag{Ant.SI.35}
    \label{AntSI.35}
$$

Recall we want to average over all possible configurations, that is, to find

$$
    \bigl\langle \Delta p(s) \bigr\rangle = \sum_s \pi(s) \Delta p(s)
    \label{how_to_average}
    \tag{4}
$$

The stationary probabilities can also be Taylor expanded

$$
    \pi(s) = \pi^{(0)}(s) + \delta \pi^{(1)}(s) + \mathcal{O}(\delta^2)
    \tag{Ant.SI.36}
    \label{AntSI.36}
$$

$$\pi^{(0)}(s)$$ is the stationary probability when $$\delta=0$$, which is the stationary probability at neutrality.
And $$\pi^{(1)}(s)$$ is some very complicated expression that we don't know about.

But the good news is that, if we substitute Eq. \ref{AntSI.35} and \ref{AntSI.36}
into Eq. \ref{how_to_average},
then the complicated $$\pi^{(1)}(s)$$ and higher terms end up multiplied by $$\delta^2$$ and higher terms,
and so when $$\delta$$ is very small (weak selection), those terms can be dropped:

$$
\begin{align}
    \bigl\langle \Delta p(s) \bigr\rangle
    &= \sum_s \pi(s) \Delta p(s)  \\
    & = \sum_s
    \left[ \pi^{(0)}(s) + \delta \pi^{(1)}(s) + \mathcal{O}(\delta^2) \right]
    \cdot
    \left[ \frac{\delta}{N} \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0} + \mathcal{O}(\delta^2) \right]
    \\
    %& = \sum_s
    %\pi^{(0)}(s) \frac{\delta}{N} \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0}
    %+ \pi^{(1)}(s) \frac{\delta^2}{N} \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0}
    %+ \ldots \\
    & = \sum_s
    \pi^{(0)}(s) \frac{\delta}{N} \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0}
    + \mathcal{O}(\delta^2) \\
    & \approx \sum_s \pi^{(0)}(s) \Delta p(s) \label{neut} \tag{5}
\end{align}
$$

Eq. \ref{neut} indicates an average taken over configurations at the neutral steady state, i.e.,

$$
    \bigl\langle \Delta p(s) \bigr\rangle
    \approx \bigl\langle \Delta p(s) \bigr \rangle_0
    = \frac{\delta}{N} \biggl\langle \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0} \biggr \rangle_0
$$

Let's evaluate that term inside the angle brackets

$$
\begin{align}
    w_{C,i} &= 1 + \delta \left( b m_i - c n_i - \frac{b-c}{N} \sum_j m_j n_j \right) + \mathcal{O}(\delta^2) \nonumber \\
    \frac{d w_{C,i}}{d\delta} &= b m_i - c n_i - \frac{b-c}{N} \sum_j m_j n_j + \mathcal{O}(\delta) \nonumber \\
    \left. \frac{d w_{C,i}}{d\delta} \right|_{\delta=0} &= b m_i - c n_i - \frac{b-c}{N} \sum_j m_j n_j \nonumber \\
    \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0}
    &= b \sum_i m_i^2 - c \sum_i m_i n_i - \frac{b-c}{N} \sum_{ij} m_i m_j n_j
    \label{eq99}
    \tag{6}
\end{align}
$$

Remember that, for selection to favour cooperators, we want our invasion condition $$\langle \Delta p(s) \rangle > 0$$ 
(Eq. \ref{invasion_condition}), i.e.,

$$
    \biggl\langle \sum_i m_i \left. \frac{d w_{C_i}}{d\delta} \right|_{\delta=0} \biggr \rangle_0 > 0
    \label{eq98}
    \tag{7}
$$

Substitute Eq. \ref{eq99} into the invasion condition Eq. \ref{eq98} and so some re-arranging

$$
    b \Bigg \langle \sum_i m_i^2 \Bigg \rangle_0 - c \Bigg \langle \sum_i m_i n_i \Bigg \rangle_0 > \frac{(b-c)}{N} \Bigg \langle \sum_{ij} m_i m_j n_j \Bigg \rangle_0
$$

which is the Eq. \ref{avg_at_ss} that they use.

In conclusion, the reason why they can replace the full population configuration with the configurations
at the neutral steady state is because of weak selection and the structure of the game.
Under weak selection, the effect of the game on fitness is scaled by $$\delta << 1$$.
The change in the proportion of Cooperators due to selection has no linear term ($$\delta^0$$).
Therefore, when the averaging is done,
the non-neutral terms in the population configurations distribution ($$\delta^1$$ and higher) are multiplied by $$\delta$$,
which gives them order $$\delta^2$$ and higher, and so they can be dropped.


<h3>References</h3>

Antal, T., Ohtsuki, H., Wakeley, J., Taylor, P. D. and Nowak, M. A. (2009). Evolution of cooperation by phenotypic similarity, Proceedings of the National Academy of Sciences 106(21): 8597–8600.
