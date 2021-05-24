---
id: 510
title: Moments for a bivariate beta distribution
date: 2017-09-14T01:39:56+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=510
permalink: /2017/09/14/moments-for-a-bivariate-beta-distribution/
image: /wp-content/uploads/2017/09/Olkin03-Figure_1.png
categories:
  - undiscovered_extinctions
---
A common choice for a probability distribution of a probability is the [beta distribution](https://en.wikipedia.org/wiki/Beta_distribution). It has the required support between 0 and 1, and with its two parameters we can obtain a pretty wide qualitative range for the probability density function.

What should we do if we want to create correlated probabilities? We might look for some kind of multivariate generalisation of the beta distribution, one that can describe pretty flexible correlation between the variables.

The generalised Dirichlet distribution allows us to describe correlated probabilities, however it has some restrictions on the support of the joint probability density function that we might not want. Briefly, the intuition of the generalised Dirichlet is to describe a step-wise process like randomly breaking fixed number of pieces off a stick, where the position of the break in the remaining proportion of the stick is drawn from an independent beta distribution ('neutral'), however the end result is that the proportions of the broken stick pieces are correlated (Connor and Mosimann, 1969). However this imposes the restriction that the proportions must sum to 1 (i.e. the length of the 'stick').

[Olkin and Liu (2003)](http://www.sciencedirect.com/science/article/pii/S0167715203000488) have a very nice paper where they introduce the bivariate beta distribution, which doesn't have this restriction. The intuition behind it is that there are two probabilities that share a "common factor", and each are also influenced by an independent "factor" that does not influence the other. For example, if we were interested in the probability of extinction and probability of detection of a particular species, then both of these probabilities might be influenced by the common factor of how restrictive the niche of the species is. In addition there are also factors describing attributes of each species that only influence the extinction probability, or only influence detection probability, alone.

Let $$ U, V, W $$ be independent gamma distributed variables with shape parameters $$a,b,c $$, respectively. Make $$W $$ the "common factor". Then we can define two probabilities  

$$ X = \frac{U}{U+W} $$  

$$ Y = \frac{V}{V+W} $$  

which turn out to be beta distributed with expected values  

$$ \mathbb{E}[X] = \frac{a}{a+c} $$  

$$ \mathbb{E}[Y] = \frac{b}{b+c}. $$

Olkin and Liu (2003) give Equation 2.2 for the moments of the distribution, however I think there might be a typo getting to the final line of the equation? I had a colleague check over it and he agrees; we think the equation might be

$$
    \mathbb{E}[X^kY^l] = \frac{ {\rm B}\left(a + c, b + l\right) {\rm B}\left(a + k, b + c\right) \,_3F_2\left(\begin{matrix} a + b + c,a + k,b + l \\ a + b + c + k,a + b + c + l \end{matrix} ; 1 \right) \Gamma\left(a + b + c\right)}{\Gamma\left(a\right) \Gamma\left(b\right) \Gamma\left(c\right)} 
$$

Unfortunately the hypergeometric term cannot be simplified. There is no general solution to the problem of simplifying $$ \,_3 F_2 () $$; it can only be simplified in certain restricted cases. Kim et al. (2010) and Lavoie et al. (1994) give a helpful overview of the problem and what is possible.

Figure 1 of Olkin and Liu (2003) shows a sampling of the shapes that the joint probability distribution can take. Unlike the generalised Dirichlet, the probability density is not restricted to the lower diagonal half of the space (i.e. not restricted to $$ X + Y < 1 $$ ).
{%
    include figure.html
    src="/wp-content/uploads/2017/09/Olkin03-Figure_1.png"
%}

**References**

Connor, R. J. and Mosimann, J. E. (1969). Concepts of independence for proportions with a generalization of the dirichlet distribution, Journal of the American Statistical Association 64(325): 194–206·

Kim, Y. S., Rakha, M. A. and Rathie, A. K. (2010). Extensions of certain classical summation theorems for the series 21, 32, and 43 with applications in ramanujan’s summations, International Journal of Mathematics and Mathematical Sciences 2010.

Lavoie, J., Grondin, F., Rathie, A. and Arora, K. (1994). Generalizations of Dixon’s theorem on the sum of a 3f2, Mathematics of Computation pp. 267–276.

Olkin, I. and Liu, R. (2003). A bivariate beta distribution, Statistics & Probability Letters 62(4): 407–412·
