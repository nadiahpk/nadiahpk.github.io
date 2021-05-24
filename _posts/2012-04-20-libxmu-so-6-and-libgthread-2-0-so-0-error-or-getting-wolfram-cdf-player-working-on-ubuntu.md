---
id: 131
title: libXmu.so.6 and libgthread-2.0.so.0 error, or getting Wolfram CDF Player working on Ubuntu
date: 2012-04-20T09:06:21+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=131
permalink: /2012/04/20/libxmu-so-6-and-libgthread-2-0-so-0-error-or-getting-wolfram-cdf-player-working-on-ubuntu/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "131"
categories:
  - coding
---
Recently a colleague sent me some information on his model and a bunch of Mathematica `.nb` files. I don't use Mathematica (if I felt the need for that kind of thing I'd go for [Sage](http://www.sagemath.org)) and I don't have access to it, so I started looking around for a way to export the notebook, say to pdf.

I found an online nb to pdf converter hosted by Wolfram called [NBtoPDF](http://library.wolfram.com/Explore/Publishing/NBtoPDF.jsp), so I uploaded the smallest file (quite a few M) while I kept searching for a solution. 

I'm glad I did keep searching, because after a good deal of time the converter returned "Error uploading file" and that was the end of that.

It seems that over time Wolfram has released a few different reader and converter programs, like Mathreader and Mathematica Player, which seem to be differently-abled versions of Mathematica. All urls now lead to [Wolfram CDF Player](http://www.wolfram.com/cdf-player/), which is available for Linux, but not with browser capability. I downloaded it and installed it

{% highlight shell-session %}
$ chmod +x CDFPlayer_8.0.4_LINUX.sh
$ sudo ./CDFPlayer_8.0.4_LINUX.sh
{% endhighlight %}

and gave it go:

{% highlight shell-session %}
$ wolframcdfplayer
/usr/local/Wolfram/CDFPlayer/8.0/SystemFiles/FrontEnd/Binaries/Linux/WolframCDFPlayer:
error while loading shared libraries: 
libXmu.so.6: cannot open sharedobject file: 
No such file or directory
{% endhighlight %}

Hrm.

I checked out the Official Forums for any Linux related stuff, and the first thread I came across had an Official Forum Moderator [advising one student](http://forums.wolfram.com/student-support/topics/26445):

> If you have the stand-alone CDF Player and cannot open and run CDF  
> files in it, contact Wolfram Technical Support at support@wolfram.com. 

lol.

Then on the Ubuntu forums I found this post:

> It looks like that MathematicaPlayerPro is a pure 32bit  
> application (according to WRI-support). Just doing:  
> sudo apt-get install ia32-libs  
> fixes the issue.  
> Rolf 

So I did an `apt-get install ia32-libs`, and retried invoking the Mathematica CDF Player:

{% highlight shell-session %}
/usr/local/Wolfram/CDFPlayer/8.0/SystemFiles/FrontEnd/Binaries/Linux/WolframCDFPlayer:
error while loading shared libraries: 
libgthread-2.0.so.0: cannot open shared object file: 
No such file or directory
{% endhighlight %}

Well I guess that's progress.

I came across another [message](http://forums.wolfram.com/mathgroup/archive/2010/Jun/msg00031.html) on the Official Wolfram Forums suggesting that the solution to the missing `libXmu.so.6` library problem was to install `libxmu-dev`. Perhaps that install had something extra? But no, I tried it on top of what I did before and still the `libgthread-2.0.so.0: cannot open shared object file` problem persisted.

Both threads however mentioned the 32-bit library issue, that CDF Player uses that instead of the 64-bit types. I took a look in `/usr/lib/` and I could see both `libXmu.so.6` and `libgthread-2.0.so.0`, but in `/usr/lib32` the offending `libgthread-2.0.so.0` library was missing.

A search landed me on [this Debian bugs thread](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=478046), where one user writes:

> my ia32-libs creates a symlink /emul/ia32-linux/usr/lib/libgthread-2.so pointing to libgthread-2.0.so.0 in the same directory, but this file is missing 

That vaguely sounded like my problem. Another replied:

> The link is in the wrong packages. It belongs in ia32-libs-gtks. But if you install ia32-libs-gtk as well it will work. 

So I tried

{% highlight shell-session %}
$ apt-get install ia32-libs-gtk
{% endhighlight %}

and success. I was then able to run it and open the notebook files. <figure id="attachment_135" aria-describedby="caption-attachment-135" style="width: 300px" class="wp-caption aligncenter">

{%
    include figure.html
    src="/wp-content/uploads/2012/04/cdfplayersuccess.jpg"
    caption="Yay, it works."
%}

The final experiment was to see if I could export the notebooks to pdf to make checking equations quicker. The GUI menu has a print to pdf option. Using evince to open it I got:

{% highlight shell-session %}
Error: PDF file is damaged - 
attempting to reconstruct xref table...
{% endhighlight %}

but evince managed to work around whatever error CDF Player had put in the file and I could read it just fine.
