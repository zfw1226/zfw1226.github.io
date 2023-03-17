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

My current research interests are robot learning, multi-agent learning, and computer vision, particularly in building agents with physical and social common sense  <a href='https://scholar.google.com/citations?user=ejDz1bYAAAAJ&hl'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2023.02*: &nbsp;🎉🎉 One paper was accepted by CVPR'23. 
- *2022.01*: &nbsp;🎉🎉 One paper was accepted by ICLR'23. 

# 📝 Recent Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/publication/cvpr23.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[GFPose: Learning 3D Human Pose Prior with Gradient Fields](https://arxiv.org/pdf/2212.08641.pdf)

Hai Ci, Mingdong Wu, Wentao Zhu, Xiaoxuan Ma, Hao Dong, **Fangwei Zhong#**, Yizhou Wang

[**Project**](https://sites.google.com/view/gfpose/) <strong><span class='show_paper_citations' data='ejDz1bYAAAAJ:8k81kl-MbHgC'></span></strong>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/gfpose-learning-3d-human-pose-prior-with/multi-hypotheses-3d-human-pose-estimation-on)](https://paperswithcode.com/sota/multi-hypotheses-3d-human-pose-estimation-on?p=gfpose-learning-3d-human-pose-prior-with)
[![arXiv](https://img.shields.io/badge/arXiv-2212.08641-b31b1b.svg)](https://arxiv.org/abs/2212.08641)
[![code](https://img.shields.io/github/stars/Embracing/GFPose?style=social&label=Code+Stars)](https://github.com/Embracing/GFPose) 
- a versatile framework to model plausible 3D human poses for various applications.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2023</div><img src='images/publication/iclr23.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[Proactive Multi-Camera Collaboration for 3D Human Pose Estimation](https://openreview.net/pdf?id=CPIy9TWFYBG)

Hai Ci, Mickel Liu, Xuehai Pan, **Fangwei Zhong#**, Yizhou Wang

[**Project**](https://sites.google.com/view/active3dpose) <strong><span class='show_paper_citations' data='ejDz1bYAAAAJ:MXK_kJrjxJIC'></span></strong>
- We propose a novel MARL framework to solve proactive multi-camrea collaborations for 3D HPE in human crowds.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2023</div><img src='images/publication/aaai23.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[RSPT: Reconstruct Surroundings and Predict Trajectories for Generalizable Active Object Tracking]()

**Fangwei Zhong***,  Xiao Bi*,  Yudi Zhang,  Wei Zhang, Yizhou Wang

[**Project**](https://sites.google.com/view/aot-rspt) <strong><span class='show_paper_citations' data=''></span></strong>
- we propose a framework called RSPT to form a structure-aware motion representation by Reconstructing Surroundings and Predicting the target Trajectory.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2022</div><img src='images/publication/neurips22.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[TarGF: Learning Target Gradient Field to Rearrange Objects without Explicit Goal Specification](https://arxiv.org/pdf/2209.00853.pdf)

Mingdong Wu*, **Fangwei Zhong***, Yulong Xia, Hao Dong

[**Project**](https://sites.google.com/view/targf) <strong><span class='show_paper_citations' data='ejDz1bYAAAAJ:0EnyYjriUFMC'></span></strong>
[![code](https://img.shields.io/github/stars/AaronAnima/TarGF?style=social&label=Code+Stars)](https://github.com/AaronAnima/TarGF) 
- We develop a framework based on a target gradient field trained by score-matching to tackle object rearrangement without explicit goal specification.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS D\&B 2022</div><img src='images/publication/mate.gif' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[MATE: Benchmarking Multi-Agent Reinforcement Learning in Distributed Target Coverage Control](https://openreview.net/pdf?id=SyoUVEyzJbE)

Xuehai Pan, Mickel Liu, **Fangwei Zhong#**, Yaodong Yang, Song-Chun Zhu, Yizhou Wang

[**Project**](https://github.com/UnrealTracking/mate) <strong><span class='show_paper_citations' data='ejDz1bYAAAAJ:5nxA0vEk-isC'></span></strong>
[![code](https://img.shields.io/github/stars/UnrealTracking/mate?style=social&label=Code+Stars)](https://github.com/UnrealTracking/mate) 
- A gamification of the multi-camera multi-target target coverage problem, and an all-in-one multi-agent reinforcement learning benchmark
</div>
</div>


# 🎖 Selected Honors and Awards
- *2021.09* ACM China SIGAI Doctoral Dissertation Award.
- *2021.06* China National Postdoctoral Program for Innovative Talents.
- *2021.06* Outstanding Graduate in Peking University and Beijing.
- *2021.05* Top 10 Outstanding Research Award in the School of EECS, Peking University.
- *2016.08* The Second Place in DJI RoboMasters Summer Camp Competition (2/10).

# 📖 Educations
- *2016.09 - 2021.07*, Peking University, Ph.D in Computer Science.
- *2012.09 - 2016.07*, Beijing Jiaotong University, B.S. in Communication Engineering. 

[comment]: <> (# 💬 Invited Talks)

[comment]: <> (- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

[comment]: <> (- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]]&#40;https://github.com/&#41;)

# 💻 Academic Service
- *Journal Reviewer*: Nature Machine Intelligence, IJRR, IEEE TIP, IEEE TVT, IEEE RAL, ACM TOMM, Sensors, IEEE Access 
- *Conference Reviewer*: ICML 2020/21/22/23, NeurIPS 2020/21/22, ICLR 2020/21/22/23, CVPR 2020/21/22/23, ICCV 2019/21/23, ECCV 2020/22, ACCV 2020, WACV 2021/22/23
- *PC Member*: AAAI 2020/21/22/23