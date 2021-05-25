---
id: 779
title: Fixation probability of birth-death process
date: 2018-08-16T10:33:09+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=779
permalink: /2018/08/16/fixation-probability-of-birth-death-process/
categories:
  - cooperation
---
The goal is to understand where Eq. 2 of the [Supplementary section of Sigmund et al. (2010)](https://media.nature.com/original/nature-assets/nature/journal/v466/n7308/extref/nature09203-s1.pdf) came from.

We are considering a finite population within which individuals are pursuing different game-theoretic strategies. At each timestep, a pair of individuals is chosen at random, and they engage in a social learning process, where individual $$ i$$ will adopt the strategy of individual $$ j$$ according to a function that increases with difference in the payoff betweeen the two strategies $$ P_j - P_i $$,

$$
\frac{1}{1+\exp( -s (P_j-P_i) )}
$$

where $$ 0 \leq s < \infty $$ is the imitation strength parameter.

Let's say that we have a population of size $$ M$$, and there are two types of strategies being pursued by individuals in the population: strategy $$ l$$ and strategy $$ k$$. Then we can calculate the probability that one of the $$ X_l$$ players with strategy $$ l$$ imitates one of the $$ X_k = M - X_l$$ players with strategy $$ k$$ as  
$$ T_{lk}(X_l) = \frac{X_l}{M} \frac{M-X_l}{M} \frac{1}{1+\exp( -s (P_k-P_l) )} $$

The particular scenario we're interested in is the invasion and fixation of a mutant strategy into a homogenous population. We are considering a population in which all individuals pursue strategy $$ k$$ except one mutant who pursues strategy $$ l$$. We are interested in answering the question: what is the probability that this mutant will overtake the population and go to fixation, so that all individuals will eventually have strategy $$ l$$? Here we are assuming that there will be no further mutations until fixation, i.e. the fixation occurs by the social learning process only.

The way to think about this is to consider the transitions of the population itself between different states, where the states are defined by the number of $$ l$$ strategists in the population. So we are asking: what is the probability that the population will go from state 1 to state M?

Let's call $$ x_i$$ the probability that a population with $$ i$$ individuals pursuing strategy $$ l$$ goes to fixation. (Here I have replaced their $$ X_l$$ notation with just an $$ i$$ as the latter makes for nicer subscripts).

First we know that:  

$$ x_0 = 0 $$

because if there are no $$ l$$-strategists, then they cannot be copied in the social learning process.

We also know that:  

$$ x_M = 1 $$  

because if all individuals are $$ l$$-strategists, then there is no alternative strategy that they can copy.

So both population states $$ i=0$$ and $$ i=M$$ are absorbing states. In between these absorbing states however, we can write the probility of fixation in terms of the other states  

$$ x_i = T_{lk}(i) x_{i-1} + (1 - T_{lk}(i) - T_{kl}(i)) x_{i} + T_{kl}(i) x_{i+1} $$  

What this equation is saying is that the probability of the $$ l$$ strategy going to fixation, when starting at state $$i$$, $$x_i$$, is equal to:

  1. the probability of the population transitioning from state $$ i$$ to $$ i-1$$, which is $$ T_{lk}(i)$$, multiplied by the probability of fixation when starting at state $$ x_{i-1}$$; plus
  2. the probability of the population remaining in state $$ i$$, which is $$ 1 - T_{lk}(i) - T_{kl}(i)$$, multiplied by the probability of fixation when starting at state $$ x_i$$; plus
  3. the probability of the population transitioning from state $$i$$ to $$i+1$$, which is $$T_{kl}(i)$$, multiplied by the probability of fixation when starting at state $$x_{i+1}$$.

To solve this recursive definition we define a new variable  
$$ y_i = x_i - x_{i-1}$$

Then we substitute the $$y_i$$ into the recursive definition and do some rearranging  
$$ x_i = T_{lk}(i) x_{i-1} + (1 - T_{lk}(i) - T_{kl}(i)) x_{i} + T_{kl}(i) x_{i+1} $$  
$$ T_{lk}(i) (x_i - x_{i-1}) = T_{kl}(i) (x_{i+1} - x_i) $$  
$$ T_{lk}(i) y_i = T_{kl}(i) y_{i+1} $$  
and if we define $$\gamma_i = T_{lk}(i) / T_{kl}(i) $$ then  
$$ \gamma_i y_i = y_{i+1} $$

We now obtain two useful facts with our $$y_i$$.

First, the sum of $$y_i$$  
$$  
\begin{align}  
\sum_{i=1}^M y_i &= x_1 - x_0 + x_2 - x_1 + \ldots + x_M - x_{M-1} \\  
&= x_M - x_0 \\  
&= 1  
\end{align}  
$$

Second, the recursive definition of $$y_i$$ means:

$$  
\begin{align}  
y_1 &= x_1 - x_0 = x_1 \\  
y_2 &= \gamma_1 y_1 = \gamma_1 x_1 \\  
y_3 &= \gamma_2 y_2 = \gamma_2 \gamma_1 x_1  
\end{align}  
$$

and so on. So altogether we have the second fact  
$$  
y_{q+1} = \begin{cases} x_1 & \text{if } q+1 = 1, \\  
x_1 \prod_{j=1}^q \gamma_j & \text{if } q+1 > 1  
\end{cases}  
$$

Now we can put those two facts together.

$$  
\begin{align}  
1 &= \sum_{i=1}^M y_i \\  
1 &= y_1 + \sum_{i=2}^M y_i \\  
1 &= y_1 + \sum_{q=1}^{M-1} y_{q+1} \\  
1 &= x_1 + x_1 \sum_{q=1}^{M-1} \prod_{j=1}^q \gamma_j \\  
x_1 &= \frac{1}{1 + \sum_{q=1}^{M-1} \prod_{j=1}^q \gamma_j}  
\end{align}  
$$

Now we can change the notation back to that used in Sigmund et al. (2010);  
$$ \rho_{kl} = \frac{1}{1 + \sum_{q=1}^{M-1} \prod_{X_l=1}^q \frac{T_{lk}(X_l)}{T_{kl}(X_l)}} $$

The final step is to observe that  
$$ \frac{T_{lk}(X_l)}{T_{kl}(X_l)} = \frac{ 1+\exp( s (P_k-P_l) )}{1+\exp( -s (P_k-P_l) )} = \exp( s (P_k-P_l) ) $$  
which gives their Eq. 2:  
$$ \rho_{kl} = \frac{1}{1 + \sum_{q=1}^{M-1} \exp( s \sum_{X_l=1}^q (P_k-P_l) )} $$

-

Useful further reading: 

Chapters 6 and 7 of [Nowak, M.A., 2006. Evolutionary dynamics. Harvard University Press](https://www.amazon.com/Evolutionary-Dynamics-Martin-Nowak-ebook/dp/B00J97FFRI).

The Wikipedia page for [Moran Processes](https://en.wikipedia.org/wiki/Moran_process).
