---
id: 74
title: An example linear programming problem in Octave
date: 2008-07-05T05:16:51+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=74
permalink: /2008/07/05/an-example-linear-programming-problem-in-octave/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "74"
categories:
  - coding
---
Tools for solving linear programming problems are useful to me because the necessary condition for permanence in a Lotka-Volterra system can be reduced to a linear programming problem (Jansen 1987, _J. Math. Biol._; Law & Morton 1996, _Ecology_). Below, I've adapted an example from Tommi Sotinen's [ORMS 1020 lecture notes](http://lipas.uwasa.fi/~tsottine/lecture_notes/or.pdf) (p. 24-38) to demonstrate how to solve a linear programming problem in Octave.

&#8212;-

Giapetto’s Woodcarving, Inc., manufactures two types of wooden toys: peace-keepers and trains. A peace-keeper sells for $27 and uses $10 worth of raw materials. Each peace-keeper that is manufactured increases Giapetto’s variable labor and overhead costs by $14. A train sells for $21 and uses $9 worth of raw materials. Each train built increases Giapetto’s variable labor and overhead costs by $10. The manufacture of wooden peace-keeper and trains requires two types of skilled labor: carpentry and finishing. A peace-keeper requires 2 hours of finishing labor and 1 hour of carpentry labor. A train requires 1 hour of finishing labor and 1 hour of carpentry labor. Each week, Giapetto can obtain all the needed raw material but only 100 finishing hours and 80 carpentry hours. Demand for trains is unlimited, but at most 40 peace-keepers are bought each week. Giapetto wants to maximize weekly profit (revenues-costs).

$$ x_1 $$ : Number of peace-keepers produced each week  

$$ x_2 $$ : Number of trains produced each week

The objective function of this problem is simply the revenue minus the costs for each toy:  

$$  
\begin{align}  
z & = (27-10-14)x_1 + (21-9-10)x_2 \\  
& = 3x_1+2x_2  
\end{align}  
$$

Maximise $$ z = 3x_1+2x_2 $$ subject to:
* $$ 2x_1+x_2 \leq 100 $$ Finishing hours constraint
* $$ x_1+x_2 \leq 80 $$ Carpentry hours constraint
* $$ x_1 \leq 40 $$ Demand for peace-keepers
* $$ x_1, x_2 \geq 0 $$ Non-negative number of toys made

In Octave, use the `glpk` function to perform the optimisation:

{% highlight matlab %}
c=[3 2]; % maximise z = 3 x_1 + 2 x_2
% subject to:
A=[2,1;1,1;1,0;1,0;0,1]; % coefficients
b=[100;80;40;0;0] % bounds

lb=[0;0]
ub=[Inf;Inf];
ctype = ["U";"U";"U";"L";"L"]; % indicates upper bound or lower bound
vtype = ["C";"C"]; % continuous variables

sense=-1; % maximises
[xopt,zmx]=glpk(c,A,b,lb,ub,ctype,vtype,sense)

xopt =

20
60

zmx = 180
{% endhighlight %}

So maximum revenue for Giapetto Woodworking Inc. is $180 each week. The report also shows that Giapetto can maximize weekly profit by producing 20 peace-keepers and 60 trains each week.
