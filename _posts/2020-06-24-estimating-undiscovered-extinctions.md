---
id: 1371
title: Estimating undiscovered extinctions
date: 2020-06-24T06:40:30+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=1371
permalink: /2020/06/24/estimating-undiscovered-extinctions/
image: /wp-content/uploads/2020/06/orchid.png
categories:
  - undiscovered_extinctions
tags: [featured]
---
Have you ever wondered how many species were lost before we had
the chance to discover them? In [a paper now out in _Conservation
Biology_](https://conbio.onlinelibrary.wiley.com/doi/abs/10.1111/cobi.13499),
we estimated just that, for plant species in Singapore. This paper
follows from the [Chisholm Lab's](https://ryanchisholm.com/) related
work on Singapore birds and butterflies.

{%
    include figure.html 
    src="/wp-content/uploads/2020/06/orchid.png"
    caption="The orchid species Grammatophyllum speciosum has not been recorded in Singapore since 1918. Photo credit: Cerlin Ng"
%}

All over the world, many species remain undiscovered while both known
and unknown species continue to go extinct. This is particularly true
in the tropics, where biodiversity is high and development continues
apace. Singapore provides an invaluable case study of tropical
biodiversity loss. Since British colonialisation, most of Singapore's
forest cover has been replaced with urban landscape. However, it also
has one of the best-documented floras in the world, both in terms of
taxonomic and temporal coverage, with historical collections beginning
only a few years after colonialisation.

We collated a high-quality database of Singapore plant collections,
and we the "SEUX" model to estimate extinction rates and total numbers
over time. The SEUX model is based on a fairly straightforward idea:
if we assume that the per-year extinction rates were the same for
discovered and undiscovered species, then we have a basis for working
backwards in time to estimate the number undiscovered species and the
proportion that went extinct. The technically challenging aspect was
to turn this idea into a method for obtaining interval estimates.

We estimated that 30 - 38% of Singapore plant species have gone extinct
since 1822. The central estimate using classical methods was 32% and
that using Bayesian methods was 35%. Crucially, these numbers are
much higher than the 22% extinction rate that one obtains from the
naïve method of simply dividing the number of known extinctions by
the total number of discovered species, demonstrating the importance
of calculating extinction rates in a way that accounts for unknown
species.

{%
    include figure.html 
    src="/wp-content/uploads/2020/06/main_figure.png"
    caption="From the Singapore plants database, we inferred the number of discovered species that were extant and <br>  extinct over time. We then used the SEUX model on this data to estimate the number undiscovered species <br> that were extant and extinct over time."
%}

In addition to the 464 extinctions recorded in our database, we estimated that between 213-534 additional species (95% CI total range) went locally extinct. As we explain in the paper, these estimates should be treated as lower bounds. If undiscovered species are more likely to go extinct than discovered ones (likely), then both the total extinction rate and the number of undiscovered extinctions is in fact higher. The number of undiscovered extinctions will also be higher if many undiscovered species remain extant today (though the total extinction rate estimates are unaffected by this assumption).

The [Singapore plant collection](https://github.com/nadiahpk/inferring-undiscovered-species-extinctions) is a valuable resource: it is an unusually rich database, situated in a tropical biodiversity hot-spot, and temporally coinciding with extensive forest clearing and urbanisation. Our colleagues at Singapore Botanic Gardens did a lot of work compiling the database, including filtering for native species in wild localities, resolving taxonomic issues, and checking the correctness of records. The resulting database contains 34,224 specimens from 2,076 species and 174 families, from collections around the world. We hope that future researchers will find this dataset useful as a test-bed for their work.

#### Useful resources:

Kristensen, N.P., Seah, W.W., Chong, K.Y., Yeoh, Y.S., Fung, T., Berman, L.M., Tan, H.Z., Chisholm, R.A. (2020) [Extinction rate of discovered and undiscovered plants in Singapore](https://nadiah.org/wp-content/uploads/2020/06/Kristensen20-Extinction_undiscovered_plants_Singapore.pdf), Conservation Biology  
    - the new paper

Theng, M., Jusoh, W.F.A., Jain, A., Huertas, B., Tan, D.J.X., Tan, H.Z., Kristensen, N.P., Meier, R., Chisholm, R.A. (2020) [A comprehensive assessment of diversity loss in a well-documented tropical insect fauna: Almost half of Singapore’s butterfly species extirpated in 160 years](https://nadiah.org/wp-content/uploads/2020/01/Theng20-Half_Singapore_butterfly_species_extirpated.pdf), Biological Conservation, 242  
    - the SEUX model applied to butterflies in Singapore
 
Chisholm, R. A., Giam, X., Sadanandan, K. R., Fung, T., & Rheindt, F. E. (2016) [A robust nonparametric method for quantifying undetected extinctions](https://doi.org/10.1111/cobi.12640). Conservation Biology, 30(3), 610-617.  
    - the paper introducing the SEUX model

Kristensen, N.P. [SEUX for R](https://github.com/nadiahpk/seux) on Github  
    - a repository of an R package (including tutorials) so you can apply the SEUX model to your own data

[Previous blog post](https://nadiah.org/2020/01/16/extinction-of-undiscovered-butterflies/)  
    - a 5 minute tutorial to get started using the SEUX package
