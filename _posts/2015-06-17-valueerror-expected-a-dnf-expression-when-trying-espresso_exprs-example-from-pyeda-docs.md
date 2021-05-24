---
id: 230
title: '"ValueError: expected a DNF expression" when trying espresso_exprs example from pyeda docs'
date: 2015-06-17T22:06:50+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=230
permalink: /2015/06/17/valueerror-expected-a-dnf-expression-when-trying-espresso_exprs-example-from-pyeda-docs/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "230"
categories:
  - coding
  - qualitative_modelling
---
I've recently been working on a qualitative modelling project where I am trying to uncover "truths" about the response of species in an ecosystem to control of invasive species. Long story short, I've been looking into various boolean minimisation techniques. I've been playing with [Python EDA](http://pyeda.readthedocs.org/en/latest/index.html), a Python library that I think provides a front-end to the Robert Brayton and Richard Rudell [espresso heuristic logic minimiser](https://en.wikipedia.org/wiki/Espresso_heuristic_logic_minimizer), [developed at University of California, Berkeley](http://embedded.eecs.berkeley.edu/pubs/downloads/espresso/index.htm).

I was trying out [the examples on the Two-level Logic Minimisation docs page](http://pyeda.readthedocs.org/en/latest/2llm.html), and I had no issues with the second 'Minimise truth tables' example. However for the first example, where we're trying to minimise a boolean expression, I kept on getting the following error

{% highlight python %}
---> 11 f1m, = espresso_exprs(f1)

ValueError: expected a DNF expression
{% endhighlight %}

I'm not real clear yet on what the various types of expressions are yet[1], but converting `f1` was a simple enough thing, and the espresso algorithm for expressions worked after that.

I've written out a minimal script that gets it going below.

{% highlight python %}
from pyeda.inter import *
from pyeda.boolalg.expr import exprvar

a, b, c = map(exprvar, 'abc')
f1 = ~a & ~b & ~c | ~a & ~b & c | a & ~b & c | a & b & c | a & b & ~c
f1dnf = f1.to_dnf()

f1m, = espresso_exprs(f1dnf)
f1m 
{% endhighlight %}

&#8212;  
[1] update: DNF stands for [Disjunctive Normal Form](https://github.com/cjdrake/pyeda/pull/122#issuecomment-112986517), which is an or-sum of boolean ands. It's basically what you'd have your UPCs table as. This function is also good for making the result of a fold more readable. For example,

{% highlight python %}
# ors is the result of some loop that has 
# ors.append( fp.reduce(lambda x, y: x & y, ands) )
# where ands was a list of boolean variables for 
# that iteration like 
# ands = [~cat_frugivores, ~cat_flyingFox, ~cat_rat]

In [122]: ors
Out[122]: 
[And(~rat_cat, ~rat_brownBooby),
 And(~rat_brownBooby, ~rat_cat),
 And(And(~rat_cat, ~rat_gecko), ~rat_hawkOwl),
...

In [123]: f1 = fp.reduce(lambda x,y: x | y, ors)

In [124]: f1
Out[124]: Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(And(~rat_cat,~rat_brownBooby), And(~cat_rat, ~cat_brownBooby)), And(~cat_brownBooby, ~cat_rat)), And(~rat_brownBooby, ~rat_cat)), And(And(~rat_cat, ~rat_gecko), ~rat_hawkOwl)), And(And(~rat_cat, #... 

# Awful!

In [125]: f1.to_dnf()
Out[125]: Or(And(~rat_brownBooby, ~rat_cat), And(~cat_brownBooby, ~cat_rat), And(~rat_gecko, ~rat_hawkOwl, ~rat_cat), And(~rat_cat, ~rat_goshawk, ~rat_tropicBird), 
... 
# Much nicer
{% endhighlight %}

&#8212;  
Update (22 July 2015)

Using a fold to do a boolean product or sum, like I did above, is an ungainly way of going about it. Much better to do something like this:

{% highlight python %}
from pyeda.boolalg.expr import And, Or

# ... some code here ...

# Where BoolList is a list of boolean variables
myBoolProduct = And(*BoolList)
myBoolSum = Or(*BoolList)
{% endhighlight %}

The boolean sum and product above are DNFs, so no need to do `.to_dnf()`.

&#8212;  
Other keywords to help Googlers find this post, particularly sociologists: boolean analysis of questionnaire data, Quinne-McCluskey, Alain Degenne, Marie-Odile Lebeaux, ultimate canonical projections, UCP, Flament, Peter Theuns, Guttman analysis, Projection Canonique Ultime, PCU, prime implicant Martin Schrepp, Ragin, qualitative comparative analysis.
