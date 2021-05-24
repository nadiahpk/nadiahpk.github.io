---
id: 69
title: Invasibility and food web structure in assembly algorithms
date: 2006-05-04T04:44:54+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=69
permalink: /2006/05/04/invasibility-and-food-web-structure-in-assembly-algorithms/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "69"
categories:
  - food_webs
---
_The following is a small literature search I did during my post-doc at CSIRO. The goal was to find system-level food web attributes that are correlated with invasibility._

**System-level food web attributes**

It is worth doing a quick overview of what is meant by the "system-level food web attributes" mentioned in the objective. Using the early empirical food web literature, a group of authors noted commonalities in certain attributes across many different webs (Cohen, 1989; Briand & Cohen, 1984,1987). Attributes included: the fraction of species in each trophic type, the fraction of links between each trophic type, link density and predator-prey ratio. As more detailed and larger food webs were added to the literature, these attributes fell out of favour. Attributes that are more in vogue now are network theoretic measures, such as characteristic path length, clustering coefficient (Watts & Strogatz, 1998), and cumulative degree distribution (Strogatz, 2001). Other measures include new ways to measure trophic level and omnivory (Williams & Martinez, 2004), generality and vulnerability (Williams & Martinez, 2000), and diet discontinuity (Cattin et al., 2004).

**Predictions of assembly algorithms**

There is no food web assembly study that I know of that is aimed at identifying correlations between the attributes above and invasibility. Instances mentioning the two are as follows:

  * Drake (1990) report that the invasion resistant communities resulting from their algorithm possess "structural patterns were strikingly similar to the scale invariant metrics reported in documented food webs" citing the work of Briand and Cohen (previous section).
  * Pimm (1989) suggests that an unbalanced predator-prey ratio, including more predators than prey, should increase web invasibility.

There are four common invasibility themes in the food web assembly literature, the latter two potentially related to the third:

  1. Maturity: that the invasibility of the food web decreases, sometimes to zero, as the web is being built and the system ages
  2. Invasion order: that the order in which species invades affects which species are successful invaders, which is related to the observation of alternative community assemblages
  3. Interaction strength: general agreement that invasibility decreases with increasing interaction strength between the species
  4. Species richness: general agreement that invasibility decreases with increasing species richness

Moyle & Light (1996) and Williamson (1996, p. 184-185) have come up with similar lists.

In addition to the above, Williamson (1996, p. 184-185) drew two lessons from a review of food web assembly algorithms in which permanence was used as the stability constraint:

  1. Transient species were not found in the model (i.e. species that could invade but not establish), even though they are known from real data.
  2. Endpoints to invasion were typically small - around ten species.

The first point is merely a consequence of using permanence as a constraint. The permanence algorithms cited use a dissipative Lotka-Volterra scheme, which allows the permanence to be ensured by a simple testing of all transversal eigenvalues. In such a scheme, all successful invaders can establish, so by definition, there are no transient species. It is noted that the Webworld algorithm does not suffer from this constraint. The second point is also likely to a consequence of the formulation, as I have achieved much larger webs with my own permanence algorithm (unpublished manuscript). Certainly Webworld can be induced to produce large webs

**Maturity**

All food web assembly algorithms that I have found concur with Law & Morton's (1996) observation that invasibility decreases as the algorithm progresses. This is sometimes summarised as \`invasibility decreases with system maturity'. The concept of ecosystem maturity and its correlation with ecosystem function (particularly stability) has a long and sometimes dubious history (my thesis, Section 2.6). I find it best to interpret "maturity" as a code-word for a group of attributes that are often found in systems have remained in a natural state for an extended period of time. For example, Shea & Chesson (2002) reasons that less mature systems should be more invasible because they have "fewer species with broader niches", with "lower competitive abilities". Kokkoris et al. (1999) correlates maturity with interaction strength (see below). Several niche-models (different to the kind of food web building algorithm we are interested in) correlate maturity with how effectively the species exploit the available resource (Tilman, 2004). There is a large literature that can be exploited for further measures of maturity.

Perhaps the simplest explanation for the observed maturity versus invasion resistance relationship in models is that an older web has been \`tested' against more species in the pool. In cases where the web can go to a single endpoint (which often occurred in Law & Morton (1996)), it is a truism that invasibility increases with time. But even when this absolute end-point is excluded, as time progresses, less invasible states will remain extant for longer than less invasible states, by definition.

Does this tautological-sounding theoretical result have any empirical support? The most compelling that I have found is from Vermeij (1991). In that study and similar work by the same author (Vermeij, 1996), the consequences of large-scale species interchanges in palaeontological time, when geographic boundaries were removed, were studied. Vermeij (1991) observed that there was an asymmetrical exchange of species, and proposed that the level of "sophistication" of the previously-isolated community affected whether it would become a species donor or recipient. Vermeij (1996) states "species evolving in diverse continental and marine biotas may carry, and be adapted to, a larger array of pathogens and parasites than species from less "sophisticated" assemblages". This reasoning is reminiscent of the authors above.

This idea can become conflated with covarying attributes of maturity. For example Moyle & Light (1996) states

> The reason, in theory, why more complex systems are harder for new invaders to disrupt is that complex assemblages are the result of repeated invasions through evolutionary time (Vermeij, 1991). Repeated invasions result in increased biological resistance to further invasions because species accumulate that have been successful competitors or predators, as demonstrated by the success of their original invasions.

The idea that a web that has experienced many invasions is less invasible can be contrasted with Simberloff & Von Holle's (1999) concept of invasional meltdown (also Grosholz, 2005). This idea is that one invasion or several invasions disrupts the system in such a way that it becomes more invasible, and more vulnerable to the impacts of invasion.

The time-span in which invasions occur seems to be the determining factor as to whether the invasions have a positive or deleterious effect upon invasibility. Parker et al. (1999), for example, uses the wording "relentless and repeated invasion". It operates through two synergistic effects: (1) the cumulative number of attempted invasions destabilises the system, making invasion easier, and (2) the number of established invaders increases, precipitating further invasion. The consensus is that depleting the number of native species increases invasibility (Case, 1996; Moyle & Light, 1996), and that one local extinction can precipitate a cascade of extinctions (Lundberg et al., 2000), often with unpredictable results (Yodzis, 1988). However, several authors state that invasions can often have a beneficial effect on the system, increasing the diversity (Smith et al., 2004; Brown & Sax, 2004), and merely decreasing the abundance of native species rather than driving them extinct (Stachowicz & Tilman, 2005).

**Invasion order**

The search for generalisations about invasion resistant webs within a food web assembly framework is confounded by the fact that the framework itself allows chance and contingency to play a role in final web structure. Depending upon which invader enters the web first, the trajectory of the web can take completely different paths and terminate with different species assemblages (e.g. Law & Morton, 1996; Case, 1991; Drake, 1990). This prediction from the assembly models has been verified in microcosm and other empirical studies (observed by Moyle & Light (1996), Fukami (2004), and Drake (1991), with additional support from Strange et al. (1992), Alford & Wilbur (1985), and Diamond (1975)).

Gilpin & Case (1976) described the alternate steady states of a model system as "domains of attraction". It was observed and that the number of these increases exponentially with the number of species and the strength of interaction.

Despite the fact that this is one of the few novel hypothesis from assembly algorithms that has been verified empirically, the existence of multiple assembly end-points may depend upon the specific conditions under which the assembly takes place. Belyea & Lancaster (1999) observes that multiple simultaneous invasions or invasions that occur before the web has time to stabilise can disrupt the assembly rules. But conversely, Fukami (2004) observed that trajectories that crossed one another (i.e. through different historical trajectories arrived at the same species assemblage) could still arrive at different end-points "owing to transient community dynamics, even if historical effects eventually weaken to allow convergence".

Chase (2003) summarises the conditions under which multiple end-points are more likely to occur:

  * Larger microcosms.
  * Low immigration rates because
  1. early invaders have enough time to establish and preclude others through the priority effect,
  2. high dispersal means that one species will eventually overcome the other through random walk unless there is heterogeneity in the environment.

  * Less disturbance (Tilman 1995) because
  1. few species can persist in disturbance, so the number of end-points declines,
  2. early invaders don't have enough time to establish and preclude others (see also 'low immigration')
  3. species suited to disturbance are poor competitors due to trade-offs.

  * Larger regional species pool
  * Low or intermediate productivity

Interestingly, Chase (2003) cite some studies which show that the number of end-points can changed within the same system by changing some environmental variable.

These ideas are related to the issue of reassembling of food webs. Law & Morton (1996) found that some webs formed by their permanence food web assembly algorithm could not be taken apart and reassembled to their original form. They proposed that the cause of this was the absence of transient species - species that were necessary for the formation of the web, but in the process, had themselves gone extinct. This observation has been repeated by Lundberg et al. (2000) and Fowler & Lindström (2002).

**Interaction strength and diversity**

Case (1990) observed that invasibility decreased with increasing interaction strength and diversity in their model systems. They relate this to Gilpin & Case's (1976) idea of multiple domains of attraction. Using the case of two identical competitors as an example, they observe that there are two possible end-points to an invasion sequence. Further, the end-point reached will be that the first species into the system will succeed. They suggest that an "activation barrier" exists, such that in species rich, strongly connected systems, native species at equilibrium will be protected from competitively superior invaders provided that the invasion occurs at low initial numbers.

This reasoning is reminiscent of Diamond's (1975) observation on bird communities on islands. Diamond (1975) found that the permitted combinations of birds were governed by factors beyond that of mere pairwise competitive exclusion and habitat suitability ("incidence functions"). He proposed that the existing combinations were "companions in starvation": in the process of establishing themselves they reduced the resources to such a low level that even competitively superior species could not invade because there was insufficient remaining resource for small initial invader population to grow.

Invasibility decreases with maturity in food web assembly algorithms. Consequently, it can be difficult to separate the true determinants of invasibility from those that are covarying with maturity. Species richness increases with maturity, which is also thought to have a negative relationship with invasibility. However, interaction strength decreases, as large webs are more likely to be stable or permanent when interactions are weak (Chen & Cohen, 2001; May, 1972). This led Kokkoris et al. (1999) to say that, empirically, we will find weak interactions in food webs to be correlated with invasion resistance.

**Criticisms of the food web assembly approach**

Criticisms of the food web assembly approach can be divided into two broad categories. First, those who criticise the approach itself, suggesting that a species-level approach would be more fruitful. Second, those who criticise the details of the models used, such as the mathematical formulation and the assumptions made.

In Levine et al.'s (2003) review of the mechanisms mediating invader impact, many examples were given that were specific to the particular species involved. Even those impacts that operated on the whole-system level, for example, the invasion of a plant that increased earthworm density, were particular to the species involved. Shrader-Frechette (2001) suggested that a "bottom-up" explanation of invasion would be most fruitful, which would require "practical and precise knowledge of particular taxa". Similarly, Williamson (1996, p. 63) states that "[the] only predictors of invasion success that appear repeatedly in the studies discussed so far are propagule pressure, suitability of the habitat and previous success in other invasions", suggesting that the most useful way to understand invasibility is to consider the individual species themselves. Indeed Williamson (1996, p. 36) states that "[all] communities are more or less equally invasible" (c.f. Moyle & Light, 1996), and goes on to say that any generalisations about community-level attributes that affect invasibility will be outweighed by lower-level determinants.

Another manifestation of this argument comes from the recognition that invasions are idiosyncratic. For example, Lennon et al. (2003) sought to test if increased nutrient availability would facilitate invasion into a plankton system. In this case, the invasion of a single species was tested, and it was found that invasibility with respect to this species was negatively correlated with resource availability. However, rather than disproving the generalisation, I find that this work highlights the need to make a distinction between what affects invasibility \`in general' and what affects invasibility in a specific case.

The most common criticism of food web assembly algorithms is the mathematical form (often Lotka-Volterra), and particularly the assumption of equilibrium conditions (e.g. Meiners et al., 2004; Levine & D'Antonio, 1999). The permanence food web assembly algorithm finds its roots in the complexity-stability debate (May, 1973), and the use of stability (however it might be defined (Grimm et al., 1992)) as a constraint on ecological systems. This can be criticised for both philosophical (Egerton, 1973; Pimm, 1991) and methodological (Hastings, 1988; Paine, 1988) reasons.

Setting aside these criticisms, further issues remain. Levine & D'Antonio (1999) adds two further shortcomings. First, that the models can only be applicable to the neighbourhood scale, as it often assumed that all species in the web can potentially interact with the invader. Second, that the selection of invaders from the same species pool as the residents means that invaders with substantially different traits to the resident are not tested. It is noted that, in real webs, successful invaders usually are very different from any native.

Using the assembly algorithm of Drake (1990) as an example, Hewitt & Huxel (2002) identified four assumptions that were used that don't necessarily hold in real life. They were:

  1. The use of a finite species pool,
  2. Only one species invades at a time,
  3. Invading species arrive at low densities, and
  4. The use of Lotka-Volterra dynamics and eigenvalue analysis.

(I pause to note that the first and fourth assumptions are not made in the Webworld model, and that although the second and third are used, they are not necessary for the algorithm to work.) Hewitt & Huxel (2002) reimplemented the Drake (1990) algorithm relaxing the second and third assumption. It was found that

  * removing both assumptions prevented the system from reaching an uninvasible state (c.f. Law & Morton, 1996),
  * allowing invaders to enter at higher densities increased the invasibility of the system

Moyle & Light (1996) observed that much of the assembly literature focused upon biological attributes of the species, assuming that all members of the species pool were physiologically capable of persisting in the environment. However laboratory studies show that this is not always the case. The physical environment can be the overriding determinant in invasion success (Ross et al., 2001).

**Attributes related to invasibility in the empirical literature**

There is no empirical literature that I know of that is aimed at identifying correlations between the attributes above and invasibility. The closest is the following studies describing the structure of invaded webs:

  * Thompson & Townsend (2003) states that the food web structures from invaded webs documented in their empirical study have very similar structures to the native webs, despite large differences in species composition.
  * Woodward & Hildrew (2001) found that result of invasions in their study web
  1. increased mean chain length
  2. increased web complexity and omnivory
  3. maintained intervality and rigid circuitry
  4. increased link-density (21% increase in links for 6% increase in species number).

The most commonly cited system-level attribute affecting invasibility is diversity or species richness. In the following section, we focus upon those underlying causes for this relationship that could be tested in a food web building algorithm.

**Correlates of diversity affecting invasibility**

The traditional position has been that diversity decreases invasibility (Elton 1958), however, arguments do exist for a positive relationship between invasibility and diversity, and this has been supported by field work (Meiners et al. 2004, Hector, Dobson, Minns, Bazeley-White & Lawton 2001). 

Much of the confusion is a consequence of the other attributes that are correlated with species richness. We have already discussed food web assembly algorithms, in which species richness is positively related to invasion resistance. In the empirical literature, the most commonly cited covarying attribute is resource availability (Stachowicz, Fried, Osman & Whitlatch 2002) and the subsequent intensification of competition (Levine & D’Antonio 1999), which has been proposed as the fundamental underlying determinant (Davis, Grime & Thompson 2000) (however counterexamples exist (Spencer & Warren 1996)). There is a potential to investigate this by increasing the resource availability, and by measuring the interaction strength and similarity (which determines competition intensity) between species. 

Further attributes that could be measured in our food webs are as follows. For those attributes that would cause a positive relationship between invasibility and diversity:

  * The idea that diversity itself can create new resources (Palmer and Maur 1997): we could try to correlate the number of predator-free potential prey with invasibility.
  * High diversity increases the probability of the presence of species that inhibit invasion (Hector et al. 2001): we could test if the removal of certain species from the web increases invasibility more than others (c.f. Drury & Nisbet 1973)

For those attributes that would cause a negative relationship between invasibility and diversity:

  * Empty niche hypothesis (Simberloff 1995), which is also related to the observation that successful invaders tend to be less similar to the natives (Pimm 1989, Stachowicz & Tilman 2005, Tilman 2004, Mithen & Lawton 1986, Fargione, Brown & Tilman 2003). Although there is no explicit niche in the algorithm, the ‘empty niche’ could be approximated in a number of ways, including the number of trophic levels, and the variety of combinations of predator and prey. (But see Case (1996), who found that replacement species often had a very different niche to the original that they replaced).
  * That the number of interactions increases with species richness (Shurin 2000): this should imply a negative relationship between link-density and invasibility.

**References**

Alford, R. & Wilbur, H. (1985). Priority effects in experimental pond communities: Competition between Bufo and Rana, Ecology 66(4): 1097-1105. 

Belyea, L. & Lancaster, J. (1999). Assembly rules within a contingent ecology, Oikos 86(3): 402-416. 

Briand, F. & Cohen, J. E. (1984). Community food webs have scale-invariant structure, Nature 307: 264-267. 

Briand, F. & Cohen, J. E. (1987). Environmental correlates of food chain length, Science 238: 956-960. 

Brown, J. & Sax, D. (2004). An essay on some topics concerning invasive species, Austral Ecology 29: 530-536. 

Case, T. (1990). Invasion resistance arises in strongly interacting species-rich model competition communities, Proceedings of the National Academy of Sciences of the United States of America 87: 9610 - 9614. 

Case, T. (1991). Invasion resistance, species build-up and community collapse in metapopulation models with interspecies competition, Biological Journal of the Linnean Society 42: 239-266. 

Case, T. (1996). Global patterns in the establishment and distribution of exotic birds, Biological Conservation 78: 69-96. 

Cattin, M., Bersier, L., Banašek-Richter, C., Baltensperger, R. & Gabriel, J. (2004). Phylogenetic constraints and adaptation explain food-web structure, Nature 427: 835-839. 

Chase, J. (2003). Community assembly: When should history matter?, Oecologia 136: 489-498. 

Chen, X. & Cohen, J. E. (2001). Global stability, local stability and permanence in model food webs, Journal of Theoretical Biology 212: 223-235. 

Cohen, J. E. (1989). Food webs and community structure, Perspectives in ecological theory, Princeton University Press, Princeton, N.J., pp. 181-202. 

Davis, M., Grime, J. & Thompson, K. ( 2000). Fluctuating resources in plant communities: A general theory of invasibility, Journal of Ecology 88: 528-534. 

Diamond, J. (1975). Assembly of species communities, in M. Cody & J. Diamond (eds), Ecology and Evolution of Communities, The Belknap Press of Harvard University Press, pp. 342-444. 

Drake, J. (1990). The mechanics of community assembly and succession, Journal of Theoretical Biology 147: 213-233. 

Drake, J. (1991). Community-assembly mechanics and the structure of an experimental species ensemble, The American Naturalist 137(1): 1-26. 

Drury, W. H. & Nisbet, I. C. T. ( 1973). Succession, Journal of the Arnold Arboretum 54(3): 331-368. 

Egerton, F. N. (1973). Changing concepts of the balance of nature, Quarterly Review of Biology 48: 322-350. 

Elton, C. (1958). The ecology of invasions by animals and plants, Metheun, London. 

Fargione, J., Brown, C. & Tilman, D. (2003). Community assembly and invasion: An experimental test of neutral versus niche processes, Proceedings of the National Academy of Sciences of the United States of America 100(15): 8916-8920. 

Fowler, M. & Lindström, J. (2002). Extinctions in simple and complex communities, Oikos 99(3): 511-517. 

Fukami, T. (2004). Assembly history interacts with ecosystem size to influence species diversity, Ecology 85(12): 3234-3242. 

Gilpin, M. & Case, T. (1976). Multiple domains of attraction in competition communities, Nature 261: 40-42. 

Grimm, V., Schmidt, E. & Wissel, C. (1992). On the application of stability concepts in ecology, Ecological Modelling 63: 143-161. 

Grosholz, E. D. (2005). Recent biological invasion may hasten invasional meltdown by accelerating historical introductions, Proceedings of the National Academy of Sciences of the United States of America 102(4): 1088-1091. 

Hastings, A. (1988). Food web theory and stability, Ecology 69(6): 1665-1668. 

Hector, A., Dobson, K., Minns, A., Bazeley-White, E. & Lawton, J. (2001). Community diversity and invasion resistance: An experimental test in a grassland ecosystem and a review of comparable studies, Ecological Research 16: 819-831. 

Hewitt, C. & Huxel, G. (2002). Invasion success and community resistance in single and multiple species invasion models: Do the models support the conclusions?, Biological Invasions 4: 263-271. 

Kokkoris, G., Troumbis, A. & Lawton, J. (1999). Patterns of species interaction strength in assembled theoretical competition communities, Ecology Letters 2: 70-74. 

Law, R. & Morton, R. D. (1996). Permanence and the assembly of ecological communities, Ecology 77(3): 762-775. 

Lennon, J., Smith, V. & Dzialowski, A. (2003). Invasibility of plankton food webs along a trophic state gradient, Oikos 103: 191-203. 

Levine, J. & D'Antonio, C. (1999). Elton revisted: A review of evidence linking diversity and invasibility, Oikos 87: 15-26. 

Levine, J., Vilá, M., D'Antonio, C., Dukes, J., Grigules, K. & Lavorel, S. (2003). Mechanisms underlying the impacts of exotic plant invasions, Proceedings of the Royal Society of London Series B 270: 775-781. 

Lundberg, P., Ranta, E. & Kaitala, V. (2000). Species loss leads to community closuer, Ecology Letters 3: 465-468. 

May, R. M. (1972). Will a large complex system be stable?, Nature 238: 413-414. 

May, R. M. (1973). Stability and complexity in model ecosystems, Princeton University Press, Princeton, New Jersey. 

Meiners, S., Cadenasso, M. & Pickett, S. (2004). Beyond biodiversity: Individualistic controls of invasion in a self-assembled community, Ecology Letters 7: 121-126. 

Mithen, S. & Lawton, J. (1986). Food-web models that generate constant predator-prey ratios, Oecologia 69: 542-550. 

Moyle, P. & Light, T. (1996). Biological invasions of fresh water: Empirical rules and assembly theory, Biological Conservation 78: 149-161. 

Paine, R. T. (1988). Food webs: Road maps of interactions or grist for theoretical development?, Ecology 69(6): 1648-1654. 

Parker, I., Simberloff, D., Lonsdale, W., Goodell, K., Wonham, M., Kareiva, P., Williamson, M., Von Holle, B., Moyle, P., Byers, J. & Goldwasser, L. (1999). Impact: toward a framework for undertanding the ecological effects of invaders, Biological Invasions 1: 3-19. 

Pimm, S. (1989). Theories of predicting success and impact of introduced species, in D. J.A., H. Mooney, F. di Castri, R. Groves, F. Kruger, M. Rejmánek & M. Williamson (eds), Biological invasions: A global perspective, John Wiley and Sons, pp. 351-367. 

Pimm, S. L. (1991). The balance of nature?: Ecological issues in the conservation of species and communities, University of Chicago Press, Chicago. 

Ross, R., Lellis, W., Bennett, R. & Johnson, C. (2001). Landscape determinants of nonindigenous fish invasions, Biological Invasions 3: 347-361. 

Shea, K. & Chesson, P. (2002). Community ecology theory as a framework for biological invasions, Trends in Ecology and Evolution 17(4): 170-176. 

Shrader-Frechette, K. (2001). Non-indigenous species and ecological explanation, Biology and Philosophy 16: 507-519. 

Shurin, J. (2000). Dispersal limitation, invasion resistance, and the structure of pond zooplankton communities, Ecology 81(11): 3074-3086. 

Simberloff, D. & Von Holle, B. (1999). Positive interactions of nonindigenous species: invasional meltdown?, Biological Invasions 1: 21-32. 

Smith, S., Bell, G. & Bermingham, E. (2004). Cross-Cordillera exchange mediated by the Panama Canal increased the species richness of local freshwater fish assemblages, Proceedings of the Royal Society of London B 271: 1889-1896. 

Spencer, M. & Warren, P. (1996). The effects of energy input, immigration and habitat size on food web structure: A microcosm experiment, Oecologia 108: 764-770. 

Stachowicz, J., Fried, H., Osman, R. & Whitlatch, R. (2002). Biodiversity, invasion resistance, and marine ecosystem function, Ecology 83(9): 2575-2590. 

Stachowicz, J. & Tilman, D. (2005). Species invasions and the relationships between species diversity, community saturation and ecosystem functioning, in D. Sax, J. Stachowicz & S. Gaines (eds), Species Invasions, Sinauer Associates Inc., Sunderland, Massachusetts, pp. 41-64. 

Strange, E., Moyle, P. & Foin, T. (1992). Interactions between stochastic and deterministic processes in stream fish community assembly, Environmental Biology of Fishes 36: 1-15. 

Strogatz, S. (2001). Exploring complex networks, Nature 410: 268-276. 

Thompson, R. & Townsend, C. (2003). Impacts on stream food webs of native and exotic forest: An intercontinental comparison, Ecology 84(1): 145-161. 

Tilman, D. (2004). Niche tradeoffs, neutrality, and community structure: A stochastic theory of resource competition, invasion and community assembly, Proceedings of the National Academy of Sciences of the United States of America 101(30): 10854-10861. 

Vermeij, G. (1991). When biotas meet: Understanding biotic interchange, Science 253(5024): 1099-1104. 

Vermeij, G. (1996). An agenda for invasion biology, Biological Conservation 78: 3-9. 

Watts, D. & Strogatz, S. (1998). Collective dynamics of \`small-world' networks, Nature 393: 440-442. 

Williams, R. & Martinez, N. (2000). Simple rules yield complex foodwebs, Nature 404: 180-183. 

Williams, R. & Martinez, N. (2004). Limits to trophic levels and omnivory in complex food webs: Theory and data, The American Naturalist 163(3): 458-468. 

Williamson, M. (1996). Biological Invasions, Chapman & Hall, London. 

Woodward, G. & Hildrew, A. (2001). Invasion of a stream food web by a new top predator, Journal of Animal Ecology 70: 273-288. 

Yodzis, P. (1988). The indeterminacy of ecological interactions as percieved through perturbation experiments, Ecology 62(2): 508-515.
