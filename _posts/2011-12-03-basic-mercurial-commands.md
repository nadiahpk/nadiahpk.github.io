---
id: 27
title: Basic mercurial commands
date: 2011-12-03T02:42:23+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=27
permalink: /2011/12/03/basic-mercurial-commands/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "27"
categories:
  - coding
---
I've started using the Mercurial version control system. I like that it doesn't leave a whole heap of files around, just one .hg directory. The commands to get started are fairly straightforward:

  1. `hg init .`
  2. `hg status`: Look at what is included or not.
  3. `hg add *`: Add everything in the directory.
  4. `hg commit`: Here you can enter some initial comment about the repository
  5. `hg view`: This allows you to look at the history of the repository through a GUI
