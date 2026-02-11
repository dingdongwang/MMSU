# MMSU: A Massive Multi-task Spoken Language Understanding and Reasoning Benchmark

[**📄 MMSU arXiv**](https://arxiv.org/pdf/2506.04779) | [**🎧 Demo Page**](https://ddw.github.io/mmsu_homepage/) | [**🏆 Leaderboard**](https://sakshi113.github.io/mmau_homepage/#leaderboard-v15-parsed) | [**🤗 Dataset Download**](https://huggingface.co/datasets/ddwang2000/MMSU) 

## Overview

MMSU (Massive Multi-task Spoken Language Understanding and Reasoning Benchmark) is a comprehensive benchmark for evaluating fine-grained spoken language understanding and reasoning in multimodal models. It systematically captures the variance of real-world linguistic phenomena in daily speech through 47 sub-tasks, including phonetics, prosody, rhetoric, syntactics, semantics, and paralinguistics, spanning both perceptual and higher-level reasoning capabilities. The benchmark comprises 5,000 carefully curated audio–question–answer pairs derived from diverse authentic recordings.

![Alt text](images/example.png)


MMSU consists of three levels of depth to classify different tasks and assessment dimensions. **At the first level**, MMSU distinguishes between two fundamental dimensions: perception abilities and reasoning abilities. Similar to human cognitive processes, perception focuses on extracting basic audio information and recognizing fundamental speech features, while reasoning involves deeper cognitive processes for interpretation and inference. **At the second level**, both dimensions are further divided into linguistics and paralinguistics categories. Linguistics is the scientific study of language structure, meaning, and usage, whereas paralinguistics is a component of meta-communication that studies the effect of vocal characteristics on semantic interpretation, such as emotion, pitch, and volume. **At the third level**, the linguistics category branches into semantics and phonology. Semantics focuses on the content-related aspects, including meaning interpretation and contextual understanding, while phonology deals with sound patterns such as tone, prosody, and phonemic distinctions. Concurrently, the paralinguistics category divides into speaker traits and speaking style. Speaker traits involve inherent characteristics such as voice timbre and speaker identity, while speaking style encompasses variable elements such as pitch, speed, and emotion.

![Alt text](images/mmsu_benchmark.png)
