---
id: 1115
title: Estimating undetected extinctions
date: 2017-03-31T03:49:25+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=1115
permalink: /2017/03/31/estimating-undetected-extinctions/
categories:
  - undiscovered_extinctions
---
The purpose of this blog post is to give a simplified account of how the [Chisholm et al. (2016)](https://conbio.onlinelibrary.wiley.com/doi/abs/10.1111/cobi.12640) method works for estimating undetected extinctions.

To estimate the historical extinction rate within a taxonomic group, a naive approach would be to divide the number of species known to be extinct by the total number of species. However, this does not account for the historical process of species discovery and temporal fluctuations in the extinction rate. The approach can be improved by estimating the cumulative probability of persistence over the time period of interest. This is equivalent to accounting for species that went extinct before we had a chance to discover them.

For example, given the historical record in the table below, the naive approach would only use the present-day ($$t=2$$) totals to estimate the extinction rate $$100 / (300 + 100) = 0.25$$. However, the extinction probability is one minus the cumulative probability of persistence, i.e. $$p = 1 - (1-0.5)(1-0.2) = 0.6$$, which is substantially higher than the naive estimate.

<table id="tablepress-1" class="tablepress tablepress-id-1">
<caption style="caption-side:bottom;text-align:left;border:none;background:none;margin:0;padding:0;"></caption>
<tbody>
<tr class="row-1">
	<td class="column-1"></td><td colspan="2" class="column-2">discovered</td><td class="column-4"></td><td class="column-5"></td><td colspan="2" class="column-6">undiscovered</td>
</tr>
<tr class="row-2">
	<td class="column-1">year (\(t\))</td><td class="column-2">extant (\(S_t\))</td><td class="column-3">extinct (\(E_t\))</td><td class="column-4">discoveries (\(\delta_t\))</td><td class="column-5">extinction rate (\(\mu_t\))</td><td class="column-6">extant (\(U_t\))</td><td class="column-7">extinct (\(X_t\))</td>
</tr>
<tr class="row-3">
	<td class="column-1">0</td><td class="column-2">100</td><td class="column-3">0</td><td class="column-4">200</td><td class="column-5">0.5</td><td class="column-6">650</td><td class="column-7">0</td>
</tr>
<tr class="row-4">
	<td class="column-1">1</td><td class="column-2">250</td><td class="column-3">50</td><td class="column-4">100</td><td class="column-5">0.2</td><td class="column-6">125</td><td class="column-7">325</td>
</tr>
<tr class="row-5">
	<td class="column-1">2</td><td class="column-2">300</td><td class="column-3">100</td><td class="column-4">-</td><td class="column-5">-</td><td class="column-6">0</td><td class="column-7">350</td>
</tr>
</tbody>
</table>

If we assume that undiscovered species have the same extinction rate as discovered species, then the historical numbers of extant and extinct undiscovered species can be estimated by working backwards in time. Assuming that no undiscovered species remain in the present day, $$U_2=0$$, then in the previous year $$U_1 = 100/(1-0.2) = 125$$, and the year before that $$U_0 = (125+200)/(1-0.5) = 650$$. Then the total number of species $$M = U_0 + S_0 = 750$$, and the total number of undiscovered extinctions $$X_2 = M - S_2 - E_2 - U_2 = 350$$, giving the same total extinction rate $$(E_2 + X_2) / M = (100 + 350) / 750 = 0.6$$.

This example simplifies the problem by using the observed species extinction rates directly. A more complete description involves inferring confidence intervals on the estimates.

#### Reference:

Chisholm, R.A., Giam, X., Sadanandan, K.R., Fung, T. and Rheindt, F.E. (2016), A robust nonparametric method for quantifying undetected extinctions. Conservation Biology, 30: 610-617. [doi:10.1111/cobi.12640](https://doi.org/10.1111/cobi.12640).
