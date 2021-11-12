---
id: 1291
title: Comparing E/MSY and Chisholm method
date: 2017-05-10T00:10:34+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=1291
permalink: /2017/05/10/comparing-e-msy-and-chisholm-method/
categories:
  - undiscovered_extinctions
---

*[Update: thoughts in this post contributed to <a href="https://conbio.onlinelibrary.wiley.com/doi/abs/10.1111/cobi.13499">Kristensen et al. (2020)</a>.]*

Historical data (e.g. sighting records) can be used to estimate historical extinction rates in a variety of ways. The Chisholm et al. (2016) method ([earlier post](https://nadiah.org/2017/03/31/estimating-undetected-extinctions/)) uses the data to estimate yearly extinction probabilities. The extinctions per million species-years (E/MSY) approach (Pimm et al., 2014) estimates they extinction probability averaged over species-years. Below, I use two small examples to illustrate the similarities and differences between them. 

#### Chisholm $$ = $$ E/SY when extinction constant

Consider the example in the table below, where the extinction probability $$ \mu_t $$ is the same in every year.

<table id="tablepress-2" class="tablepress tablepress-id-2">
<caption style="caption-side:bottom;text-align:left;border:none;background:none;margin:0;padding:0;"></caption>
<tbody class="row-hover">
<tr class="row-1 odd">
	<td class="column-1"></td><td colspan="2" class="column-2">discovered</td><td class="column-4"></td><td class="column-5"></td>
</tr>
<tr class="row-2 even">
	<td class="column-1">year \( t \)</td><td class="column-2">extant \( S_t \)</td><td class="column-3">extinct \(E_t\)</td><td class="column-4">discoveries \( \delta_t \)</td><td class="column-5">extinction rate \( \mu_t \)</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">0</td><td class="column-2">100</td><td class="column-3">0</td><td class="column-4">20</td><td class="column-5">0.2</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">1</td><td class="column-2">100</td><td class="column-3">20</td><td class="column-4">40</td><td class="column-5">0.2</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">2</td><td class="column-2">120</td><td class="column-3">40</td><td class="column-4">84</td><td class="column-5">0.2</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">3</td><td class="column-2">180</td><td class="column-3">64</td><td class="column-4">56</td><td class="column-5">0.2</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">4</td><td class="column-2">200</td><td class="column-3">100</td><td class="column-4">120</td><td class="column-5">0.2</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">5</td><td class="column-2">280</td><td class="column-3">140</td><td class="column-4">10</td><td class="column-5">0.2</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">6</td><td class="column-2">234</td><td class="column-3">196</td><td class="column-4">-</td><td class="column-5">-</td>
</tr>
</tbody>
</table>

The Chisholm et al. (2016) method calculates the total extinction probability $$ p $$ as described in [a previous blog post](https://nadiah.org/2017/03/31/estimating-undetected-extinctions/). The total extinction probability over the observation period is 1 - the cumulative probability of survival  

$$  
\begin{align}  
p &= 1 - \text{probability of survival} \\  
& = 1 - \prod_{t=0}^5 1 - \mu_t \\  
& = 1 - (1-0.2)^6 \\  
& = 0.74.  
\end{align}  
$$  

The year-averaged extinction probability is obviously 0.2, which we can obtain from $$ p $$ using the geometric mean of survival probabilities  

$$  
\begin{align}  
\text{year-averaged extinction rate} & = 1 - (1-p)^{1/6} \\  
& = 0.2  
\end{align}  
$$

The E/SY is calculated as follows. Each species' number of species-years is calculated from the time of its discovery to the time of its extinction, so the total number of species-years is  

$$  
\begin{align}  
\text{species-years} &= \sum_{t=0}^5 S_t \\  
& = 980.  
\end{align}  
$$  

Therefore  

$$  
\begin{align}  
\text{species-year averaged extinction rate} & = \frac{196}{980} \\  
& = 0.2,  
\end{align}  
$$  

which is the same as the Chisholm et al. (2016) method above.

#### Chisholm $$ \neq $$ E/SY when extinction probability varies

Consider the example in the table below, where the extinction probability $$\mu_t $$ varies year to year.

<table id="tablepress-3" class="tablepress tablepress-id-3">
<caption style="caption-side:bottom;text-align:left;border:none;background:none;margin:0;padding:0;"></caption>
<tbody class="row-hover">
<tr class="row-1 odd">
	<td class="column-1"></td><td colspan="2" class="column-2">discovered</td><td class="column-4"></td><td class="column-5"></td>
</tr>
<tr class="row-2 even">
	<td class="column-1">year \( t \)</td><td class="column-2">extant \( S_t \)</td><td class="column-3">extinct \( E_t \)</td><td class="column-4">discoveries \( \delta-t \)</td><td class="column-5">extinction rate \( \mu_t \)</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">0</td><td class="column-2">100</td><td class="column-3">0</td><td class="column-4">20</td><td class="column-5">0.4</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">1</td><td class="column-2">80</td><td class="column-3">40</td><td class="column-4">40</td><td class="column-5">0.2</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">2</td><td class="column-2">104</td><td class="column-3">56</td><td class="column-4">84</td><td class="column-5">0.125</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">3</td><td class="column-2">175</td><td class="column-3">69</td><td class="column-4">56</td><td class="column-5">0.04</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">4</td><td class="column-2">224</td><td class="column-3">76</td><td class="column-4">120</td><td class="column-5">0.0625</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">5</td><td class="column-2">330</td><td class="column-3">90</td><td class="column-4">10</td><td class="column-5">0.1</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">6</td><td class="column-2">307</td><td class="column-3">123</td><td class="column-4">-</td><td class="column-5">-</td>
</tr>
</tbody>
</table>

The total extinction probability over the observation period is  

$$  
\begin{align}  
p &= 1 - (0.6)(0.8)(0.875)(0.96)(0.9375)(0.9)\\  
&= 0.66,  
\end{align}  
$$  

giving  

$$  
\begin{align}  
\text{year-averaged extinction rate} &= 1 - (1-0.66)^{1/6} \\  
&= 0.16.  
\end{align}  
$$

The total number of species-years  

$$  
\begin{align}  
\text{species-years} &= \sum_{t=0}^5 S_t \\  
&= 1013,  
\end{align}  
$$  

so the E/SY is  

$$  
\begin{align}  
\text{species-year averaged extinction rate} &= \frac{123}{1013} \\  
&= 0.12,  
\end{align}  
$$  

which is different to the Chisholm et al. (2016) method.

#### References:

Chisholm, R.A., Giam, X., Sadanandan, K.R., Fung, T. and Rheindt, F.E. (2016), A robust nonparametric method for quantifying undetected extinctions. Conservation Biology, 30: 610-617. [doi:10.1111/cobi.12640](https://doi.org/10.1111/cobi.12640).

Pimm, S. L., Jenkins, C. N., Abell, R., Brooks, T. M., Gittleman, J. L., Joppa, L. N., Raven, P. H., Roberts, C. M. and Sexton, J. O. (2014). The biodiversity of species and their rates of extinction, distribution, and protection, Science 344(6187): 1246752.
