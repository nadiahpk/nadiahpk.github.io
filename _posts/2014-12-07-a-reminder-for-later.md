---
id: 210
title: A reminder for later
date: 2014-12-07T01:24:21+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=210
permalink: /2014/12/07/a-reminder-for-later/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "210"
categories:
  - coding
---
The [Automatic Differentiation](http://hackage.haskell.org/package/ad) package in Haskell can do some interesting things.

{% highlight none %}
Prelude Numeric.AD> jacobian ([x, y] -> [x*x*y, 5*x + sin y]) [1, 1]
[[2.0,1.0],[5.0,0.5403023058681398]]
{% endhighlight %}
