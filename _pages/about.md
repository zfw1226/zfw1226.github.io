---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently working as Boya Postdoctoral Researcher at Peking University with Prof. [Song-Chun Zhu](http://www.stat.ucla.edu/~sczhu/).
Before that, I received Ph.D in Computer Science from EECS, Peking University, supervised by Prof. [Yizhou Wang](https://cfcs.pku.edu.cn/wangyizhou/#../../../english/index.htm), and received B.Sc in Communication Engineering from Beijing Jiaotong University.

My current research interests are robot learning, multi-agent learning, and computer vision, particularly in building embodied agents with physical and social common sense.

{% include_relative includes/news.md %}

{% include_relative includes/pub.md %}

{% include_relative includes/honers.md %}

{% include_relative includes/others.md %}