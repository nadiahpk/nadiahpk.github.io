---
id: 461
title: Understanding the neigbour-modulated inclusive fitness approach
date: 2016-12-15T13:27:25+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=461
permalink: /2016/12/15/understanding-the-neigbour-modulated-inclusive-fitness-approach/
categories:
  - cooperation
---
The goal is to understand Equation 4.2 of Rodrigues and Kokko (2016).

To understand the technique, I read through Taylor et al. (2007), and Taylor and Frank (1996), specifically examples 4, 4a and 4b. Very briefly, we begin with a matrix $$ A = [w_{i,j} ] $$ whose elements represent the genetic contribution of class $$ j $$ to class $$ i $$. Then for some mutant genic value $$ x $$, the fitness derivative is

$$ \frac{dW}{dx} = \sum_{i,j} v_i \frac{dw_{i,j}}{dx} u_j $$

where $$ \mathbf{v} $$ is the left eigenvector of $$ A $$ and is the reproductive values, and $$ \mathbf{u} $$ is the right eigenvector of $$ A $$ and is the class frequencies. In the Appendix Taylor and Frank show us that the reproductive values and class frequencies at the steady state may be used, so one need only concern one's self with taking derivatives of the elements of the contributions matrix itself.

Given Equation 3 of Taylor and Frank (1996), the derivatives can be expanded as  

$$ \frac{d w_{i,j}}{dx} = \frac{\partial w_{i,j}}{\partial y} + r \frac{\partial w_{i,j}}{\partial z} $$

where $$ y $$ is the phenotype of the actor, $$ z $$ is the phenotype of the neighbour, and $$ r $$ is the relatedness of the neighbour to the actor, which scales the effect of the correlated change in the actor's phenotype to its effect on $$ w_{i,j} $$.

After working through the examples in Taylor and Frank (1996), I was able to rederive the results in  
Rodrigues and Kokko (2016). I will use the survival-survival scenario as an example.

From the appendix, the contributions matrix is  

$$ [w_{i,j}] = \begin{pmatrix} f_1 (1-G) + s_1 (1-A) & f_2 (1-G) + s_2 (1-\hat{s}_2) \\ f_1 G + s_1 A & f_2 G + s_2 \hat{s}_2 \\ \end{pmatrix} $$  

where $$ f_i $$ is fecundity in class $$ i $$, $$ s_i $$ is survival in class $$ i $$, $$ G $$ is the probability that a dispersing offspring joins a group, and $$ A $$ is the probability of being joined by a disperser. I have introduced a \`hat' to indicate which survival refers to the survival of the partner, as this makes the maths easier to follow later.

First, the helping behaviour only manifests when the individual has a partner, so we need only take derivatives of the $$ w_{1,2} $$ and $$ w_{2,2} $$.

Second, the cost $$ C $$ and benefit $$ B $$ mentioned in the paper are to be interpreted as the derivatives of survival with respect to the donor's and recipient's helping phenotype respectively  

$$ C = \frac{\partial s_2}{\partial y} = \frac{\partial \hat{s}_2}{\partial z} $$  

$$ B = \frac{\partial \hat{s}_2}{\partial y} = \frac{\partial s_2}{\partial z} $$  

Then  

$$ \frac{d w_{1,2}}{dx} = \frac{\partial w_{1,2}}{\partial y} + r \frac{\partial w_{1,2}}{\partial z} $$  

$$ \frac{d w_{1,2}}{dx} = (1-\hat{s_2}) \frac{\partial s_{2}}{\partial y} + s_2 \frac{\partial (1-\hat{s_2})}{\partial y} + r \left( (1-\hat{s_2}) \frac{\partial s_{2}}{\partial z} + s_2 \frac{\partial (1-\hat{s_2})}{\partial z} \right)$$

$$ \frac{d w_{1,2}}{dx} = (1-\hat{s_2}) \frac{\partial s_{2}}{\partial y} + s_2 \frac{\partial (1-\hat{s_2})}{\partial y} = - (1-\hat{s_2}) C - s_2 B + r \left( B (1-\hat{s_2}) + C s_2 \right)$$

Similarly

$$ \frac{d w_{2,2}}{dx} = \frac{\partial w_{2,2}}{\partial y} + r \frac{\partial w_{2,2}}{\partial z} $$  

$$ \frac{d w_{2,2}}{dx} = \hat{s_2} \frac{\partial s_{2}}{\partial y} + s_2 \frac{\partial \hat{s_2}}{\partial y} + r \left( \hat{s_2} \frac{\partial s_{2}}{\partial z} + s_2 \frac{\partial \hat{s_2}}{\partial z} \right)$$

$$ \frac{d w_{2,2}}{dx} = - \hat{s_2} C + s_2 B + r \left( B \hat{s_2} - C s_2 \right) $$

Then

$$ \frac{dW}{dx} = v_1 \frac{d w_{1,2}}{dx} u_2 + v_2 \frac{d w_{2,2}}{dx} u_2 $$  

$$ \frac{dW}{dx} = u_2 \left[ -C \left( (1-\hat{s}_2) v_1 - \hat{s}_2 v_2 \right) + B s_2 (v_2 - v_1) + Br \left( (1-\hat{s}_2) v_1 - \hat{s}_2 v_2 \right) - C r s_2 (v_2 - v_1) \right] $$

Setting $$ \hat{s}_2 = s_2 $$ gives the condition for invasion of the helping strategy given in Equation 4.2 in the text.
