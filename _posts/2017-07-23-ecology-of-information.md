---
id: 1375
title: Ecology of information
date: 2017-07-23T06:48:52+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=1375
permalink: /2017/07/23/ecology-of-information/
image: /wp-content/uploads/2017/07/ovenbird.jpg
categories:
  - evolutionary_ecology
tags: [featured]
---
_Collaborators: [Kenneth Schmidt](http://schmidtlab.weebly.com/), [Jacob Johansson](https://jacobjohansson.weebly.com/), [François Massol](http://www.cefe.cnrs.fr/dynamique-et-adaptation-des-populations-vegetales/francois-massol), [Niclas Jonzen](https://royalsocietypublishing.org/doi/full/10.1098/rsbl.2015.0444)._ 

{%
    include figure.html
    src="/wp-content/uploads/2017/07/ovenbird.jpg"
%}

Breeding birds subject to nest-predation will attempt to choose a high quality nesting site with a low density of predators. For example, when recordings of chipmunk calls are played in the forest, ovenbirds will nest away from where the recordings are playing ([Eureka Alert](https://www.eurekalert.org/pub_releases/2011-06/w-oeo062211.php)). Often models assume perfect information, so that sites are filled from highest to lowest quality, or in this case, from lowest predator density to highest density. However in reality, information about a potential nesting site must be determined by 'prospecting': a period of observation during which birds gather information about the site to reduce uncertainty. Given that ovenbirds listen for chipmunk calls in order to determine where to nest, this implies that some amount of _time_ must be spent determining territory quality.

The issue of prospecting time sets up a potential conflict: time spent surveying potential territories increases the probability that a bird will choose a high-quality (i.e. relatively predator-free) nesting site, however the longer a bird takes to make its decision, the more likely it is that other individuals will claim the good territories for themselves. 

In our recent work, we explored the behaviour of a model describing this trade-off. We assume that individuals choose between two types of breeding sites - 'good' and 'bad' - that differ in the risk of nest predation, and consider the evolution of timing of settlement into breeding sites. Specifically, the probability that a bird will choose a good territory increases with the amount of time that it spends prospecting at individual sites. However we also assumed that individuals pick sites sequentially, in the order given by their settlement date, following the principle of prior residency. This scenario corresponds to the classic probality-theory problem of selecting coloured and weighted balls from an urn without replacement. The [Wallenius non-central hypergeometric distribution](http://en.wikipedia.org/wiki/Wallenius'_noncentral_hypergeometric_distribution) (WNHD) describes the probability distribution for the number of sites available after a certain number of draws, which can be solved using various sophisticated [numerical methods](http://www.agner.org/random/theory/). 

We were able to combine techniques from adaptive dynamics (a mathematical framework for ecoevolutionary dynamics) with approximations of and numerical solutions to the WNHD to predict the settling time strategy that would be used by the birds under a variety of scenarios. We explored changes in nest predation, habitat composition, population vital rates, and availability of information. 

One interesting result was that, despite the complexity of the model and how much is involved in determining the evolutionarily selected settling-time strategy, due to a population-dynamic feedback between ability to discern good territories and population size, the individual's probability of obtaining a good territory is _unchanged_ by changes in settlement time (Eqn 11 Schmidt et al. 2014). Settling earlier only matters _relative_ to the settling times of one's competitors. Therefore while selection may favour individuals that pursue a settling-time strategy that is earlier than the rest of the group, once that strategy takes over and all individuals in the population are settling at that time, the advantage is lost and nullified by a population-size feedback. 

The population dynamic feedback also led to the paradoxical result that with greater spatial heterogeneity, less effort is placed on discerning good and bad sites. One might intuitively expect that the effort spent to collect information should be proportional to the value of that information (Patterson et al. 1980, Schaef and Mumme 2012). So one would expect that the greater the difference between territory qualities - the better the good territories are compared to the bad - then the greater the effort that will be spent on discerning them. However this is not the case; an increase in reproduction rate in the good territories also increases population size, which then increases competition for territories and thus the importance of settling early. The evolutionarily singular settling-time strategy was longest when the difference between good and bad territories was low. In this way, our intuition about information's value ('stimulus value' sensu Patterson et al. 1980) must be applied with caution. 

Much work has been done on the effects of climate change on the timing of life-history events. In birds, the focus has primarily been upon how breeding time correlates with the timing of food resources necessary for offspring (e.g. see my work on [migratory birds](/community-evolution-models/)). However nest predation is a major source of reproductive mortality, and predators may have their own phenology (e.g. chipmunk hibernation length) that could interact with reproduction and the settling-time strategy in complex ways. It is hoped that this study will provide the starting point for future work in this area. 

### Find out more:

  * You can download the full-Wallenius version of the model from Github: [settlement-time-game](https://github.com/nadiahpk/settlement-time-game)
  * Details of the model and our results are described in our paper: Schmidt, K.A., Johansson, J., **Kristensen, N.P.**, François, M., and Jonzen, N. (2015) Consequences of information use in breeding habitat selection on the evolution of settlement time, _Oikos_ **124**(1):69-80. 
  * A theoretical overview of phenology can be found in: Johansson, J., **Kristensen, N.P.**, Nilsson, J., and Jonzen, N. (2015) The eco-evolutionary consequences of interspecific phenological asynchrony: a theoretical perspective, _Oikos_ **124**(1):102-112.
