---
id: 981
title: Pretty diagram of directory structure
date: 2019-04-04T07:05:53+00:00
author: nadiahkristensen
layout: post
guid: https://nadiah.org/?p=981
permalink: /2019/04/04/pretty-diagram-of-directory-structure/
image: /wp-content/uploads/2019/04/repo_structure.png
categories:
  - coding
---
In a [recent project](https://nadiah.org/category/conservation/undetected-extinctions/), I wanted to create a diagram of a repository for the appendix of a paper, including comments to highlight key files and explain how the folders were organised. I found [this answer on Stack Exchange](https://tex.stackexchange.com/a/270761) by user [Gonzalo Medina](https://tex.stackexchange.com/users/3954/gonzalo-medina), which I tweaked to produce the diagram below.

{%
    include figure.html 
    src="/wp-content/uploads/2019/04/repo_structure.png"
    caption="An annotated directory structure."
%}

The code is below:

{% highlight latex %}
% Adapted from https://tex.stackexchange.com/a/270761

\documentclass[tikz,border=5mm]{standalone}
\usepackage[edges]{forest}

\definecolor{foldercolor}{RGB}{124,166,198}
\newcommand{\size}[2]{ {\fontsize{#1}{0}\selectfont#2}}
\definecolor{blue}{RGB}{0,50,200}
\newcommand{\comment}[0]{\color{blue} \rm}

\tikzset{pics/folder/.style={code={
  \node[inner sep=0pt, minimum size=#1](-foldericon){};
  \node[folder style, inner sep=0pt, minimum width=0.3*#1, minimum height=0.6*#1, above right, xshift=0.05*#1] at (-foldericon.west){};
  \node[folder style, inner sep=0pt, minimum size=#1] at (-foldericon.center){};}
  },
  pics/folder/.default={20pt},
  folder style/.style={draw=foldercolor!80!black,top color=foldercolor!40,bottom color=foldercolor}
}

\forestset{is file/.style={edge path'/.expanded={
    ([xshift=\forestregister{folder indent}]!u.parent anchor) |- (.child anchor)},
    inner sep=1pt},
  this folder size/.style={edge path'/.expanded={
    ([xshift=\forestregister{folder indent}]!u.parent anchor) |- (.child anchor) pic[solid]{folder=#1}}, inner xsep=0.6*#1},
  folder tree indent/.style={before computing xy={l=#1}},
  folder icons/.style={folder, this folder size=#1, folder tree indent=3*#1},
  folder icons/.default={12pt},
}

\begin{document}

\begin{forest}
  for tree={font=\ttfamily, grow'=0, folder indent=.9em, folder icons}
    [repository
      [data
        [cleaned\_plants\_database
          [experts\_extant.csv {\comment (which species are common and extant according to experts)}, is file]
          [merged.csv {\comment (the plants database merged from different herbaria and museums)}, is file]
          ]
        [processed
          [first\_last\_detns\_final.csv {\comment (input to SEUX model)}, is file]
        ]
      ]
      [undetected\_extinctions {\comment (shared SEUX model functions)}
      ]
    ]
\end{forest}

\end{document}

{% endhighlight %}

