---
id: 939
title: The Principle of Indifference is actually two principles in one
date: 2015-11-20T07:22:27+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=939
permalink: /2015/11/20/the-principle-of-indifference-is-actually-two-principles-in-one/
image: /wp-content/uploads/2019/03/jdnorton1_memed.jpg
categories:
  - qualitative_modelling
---
In a [previous post](https://nadiah.org/2015/05/20/qualitative-modelling-and-the-principle-of-indifference/), I wrote about the philosophical problems caused by the Principle of Indifference. The problems are illustrated with a variety of thought-experiments that create paradoxes, such as [Bertrand's paradox](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)). I also discussed how a problem in ecological modelling for conservation decision-making seems closely related to this philosophical problem.

When I realised this connection, it seemed to me that, in order to solve the ecological problem, I would need to solve the philosophical problem first. Reading the philosophy literature, however, I realised that solving the philosophical problem would not be so simple. As Shackel (2007) sums it up, the Bertrand paradox remains unresolved, and "continues to stand in refutation of the principle of indifference". But I just couldn't let the Principle go. For starters, the Principle works so well in canonical examples, such as the role of a die. Plus the idea that one should not distinguish between indistinguishable outcomes seems tautologically true. Perhaps there was another way of viewing these refutations? 

When I thought about other famous philosophical paradoxes, it seemed to me that the point of them was not to say that an idea is completely without merit, but to teach us something about the limits of that idea. For example, as far as I know, no one has solved the [Sorites Paradox](https://en.wikipedia.org/wiki/Sorites_paradox) or the [Ship of Theseus](https://en.wikipedia.org/wiki/Ship_of_Theseus) either, but that doesn't mean that we can't talk about \`heaps' or things in general in a sensible and useful way. Rather, the point seems to be that there is a limit to what we can achieve with a qualitative predicate or a concept of identity, and the paradox alerts us to the kinds of scenarios where we might end up pushing the concept too far.

{%
    include figure.html
    src="/wp-content/uploads/2019/03/jdnorton1_memed.jpg"
    caption="John D. Norton, University of Pittsburgh, <a href='https://knowyourmeme.com/memes/matrix-morpheus)'>who might also be Morpheus from The Matrix</a>"
%}

The real breakthrough came when I stumbled across the papers of [John Norton](http://www.pitt.edu/~jdnorton/jdnorton.html) at Uni of Pittsburgh, and I realised that the three-valued system that he discussed in one of his papers (below) sounded very similar to [an approach that I was playing with at the time](https://nadiah.org/2015/06/17/valueerror-expected-a-dnf-expression-when-trying-espresso_exprs-example-from-pyeda-docs/).

He's also a very kind person who generously agreed to Skype with me, look over my manuscript, and write long emails to me explaining his ideas.

The first key insight that he shared with me is that the Principle of Indifference, as it's commonly applied, is actually _two ideas in one_. The first idea is that, if we have no grounds for distinguishing possible scenarios, then we should favour them equally. The second idea is that the extent of favouring can be represented by a probability.

The second key insight is that the paradoxes are ultimately caused by a lack of background information. In canonical examples like the roll of a die, we have background information about dice and how they work, so we immediately know that the relevant outcome space is the faces 1..6, and we can assign equal probabilities 1/6 to each. However, imagine a situation in which we had absolutely no idea how dice work, and we had to apply the Principle of Indifference. We could assign equal probabilities to 6 and not-6, or 5 and not-5, and so on. But no single probability distribution can capture all of these indifferences, because $$ P(6) = P(\text{not-6}) $$ precludes $$ P(5) = P(\text{not-5}) $$, and so on.

The problem with a lack of background information is that it prevents us from choosing an outcome space upon which to apply the Principle of Indifference. There are always multiple ways to describe the outcome space, and in cases where we have very little background information, we have no means to privilege one description as the correct one.

Norton (2008) has argued that a resolution to the problems above cannot discard the first of the two ideas in the principle: that outcomes over which we are indifferent must be treated the same. This is just a truism of evidence. Therefore the resolution must be to discard the second idea - that favoring is always to be represented by probabilities - and seek other, more flexible representations.

An example of a more flexible representation is given in Norton (2010a, b), where he shows that if we replace probability with a three-valued representation - such that an outcome is either (1) possible, (2) necessary, or (3) impossible - then the paradoxes no longer occur. The challenge then is whether or not anything useful can be gleaned from such an impoverished representation.

**References**

Shackel, N. (2007). Bertrand’s Paradox and the Principle of Indifference, Philosophy of Science 74(2): 150–175.

Norton, J. D. (2008). Ignorance and indifference, Philosophy of Science 75(1): 45–68.

Norton, J. D. (2010a). Cosmic confusions: not supporting versus supporting not-, Philosophy of Science 77(4): 501–523.

Norton, J. D. (2010b). There are no universal rules for induction, Philosophy of Science 77(5): 765–777. 
