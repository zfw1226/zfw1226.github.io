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

I am an Associate Professor at the School of Artificial Intelligence, Beijing Normal University.
Prior to this, I served as a Boya Postdoc at Peking University, working with [Prof. Song-Chun Zhu](https://zhusongchun.net/).
I received my PhD in Computer Science from the School of EECS at Peking University, where I was advised by [Prof. Yizhou Wang](https://cfcs.pku.edu.cn/wangyizhou/#../../../english/index.htm), 
and I obtained my bachelor's degree in Communication Engineering from Beijing Jiaotong University.

My research interests are embodied AI and multi-agent system, particularly in building cognition-inspired agents with physical and social common sense.

{% include_relative includes/news.md %}

{% include_relative includes/pub.md %}

{% include_relative includes/honers.md %}

{% include_relative includes/others.md %}