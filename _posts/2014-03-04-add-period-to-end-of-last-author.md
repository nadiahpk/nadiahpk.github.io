---
id: 161
title: Add period to end of last author (Biology Letters .bst)
date: 2014-03-04T13:10:12+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=161
permalink: /2014/03/04/add-period-to-end-of-last-author/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "161"
categories:
  - coding
---
I had an issue today where I wanted to create a custom .bst file for _Biology Letters_ that would format as follows:

1. Parmesan C, Yohe G. 2003 A globally coherent fingerprint of climate change impacts across natural systems. Nature **421**, 37–42.

I was using makebst, incrementally editing my .dbj file, but I couldn't seem to get that '.' on the end of the author list to come out. The problem seemed to be some interaction between the default for blocks and authors.

My options for author were

{% highlight none %}
%<>PUNCTUATION AFTER AUTHORS:
{% endhighlight %}

So going with the default invoked (I think) this section of the .dbj file

{% highlight none %}
%<>PUNCTUATION BETWEEN SECTIONS (BLOCKS):
{% endhighlight %}

Unfortunately the "else commas" up there means commas after the author block. So the combination above was producing

1. Parmesan C, Yohe G, 2003 A globally coherent fingerprint of climate change impacts across natural systems. Nature **421**, 37–42.

When I tried going for the default, i.e.

{% highlight none %}
%<>PUNCTUATION BETWEEN SECTIONS (BLOCKS):
{% endhighlight %}

I was still getting a comma. I'm not sure what the openbib option is so that might have been the answer there.

Instead, my solution (if you can call it that) was to leave the punctuation between sections as default, and change the author section to

{% highlight none %}
%<>PUNCTUATION AFTER AUTHORS:
{% endhighlight %}

I then went into the .bst file and initially tried to replace all instances of 'add.colon' with 'add.period', but when that didn't work, I found the 'add.colon' function and put a new 'add.period' function under it.

{% highlight none %}
FUNCTION {add.colon}
{ duplicate$ empty$
 'skip$
 { ":" * add.blank }
 if$
}

FUNCTION {add.period}
{ duplicate$ empty$
 'skip$
 { "." * add.blank }
 if$
}
{% endhighlight %}

The .bst file now produced what I needed.

You can find the .bst files here: [biologyletters.bst](https://s3.amazonaws.com/nadiah.org/toolfiles/biologyletters.bst), [biologyletters.dbj](https://s3.amazonaws.com/nadiah.org/toolfiles/biologyletters.dbj).
