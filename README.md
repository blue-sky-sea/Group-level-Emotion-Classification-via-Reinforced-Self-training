========================================================================

# Zero-shot Emotion Classification via Reinforced Self-training

========================================================================

![image](https://user-images.githubusercontent.com/26008298/132282618-0440b99c-af47-4e75-9c45-2253ba94f59d.png)

========================================================================

| author | mizukiyuta | <br />   
| department | Tokyo Metropolitan University System Design |  <br />

========================================================================

## Used device

### VIVE PRO EYE headset(for eye tracking)

### Polar H10(for ECG)

## Data Collection
Based on VR virtual world to arose people's emotion by group discussion/communication<br /> 
meanwhile,sensors(headset,Polar H10) will collect collaborators' bio-data and save to csv 

## Experiment Design
#### APP: VRChat
Participants: more than 20 groups of collaborators (3 people a group)
#### Used Raw Data: 
ECG，Audio，Eye Tracking，Lip Tracking，Head position&rotation

#### Details:	
One participant wear sensors and VR headset as a main talker
other two participants just wear VR headset and talk
Each conversation lasted approximately three minutes
#### Topics:
Talk about specific topics that are likely to cause emotional fluctuations or produce opposing positions
Talk about a recent sad thing悲伤的事情  
Talk about the biggest worry担忧的事情  
Talk about the things that make u angry让人生气的事情  
Talk about the things that make people shy and embarrassed让人脸红/尴尬的事情  
Talk about the disgusting things that make you sick 讨论让人感到恶心不爽的事情
Talk about a happy thing开心的事情  
Talk about your hobby兴趣爱好  
Talk about the places you would most like to visit最想去旅游的地方
Talk about the type you like喜欢的类型  
Talk about your dream or future plan谈论你的梦想或者未来规划  
Talk about your research or project谈论你的研究或者项目  
Whether to agree with Dink？Why？同意丁克吗，为什么  


3.Talk about the things that make u angry让人生气的事情
#### Emotion model
PAD (Pleasure, Arousal, Dominance) model

## To solve

#### 为什么要VR

虚拟空间/虚拟会议/虚拟人/智能agent
智能主持会议、改变场景氛围提升体验感、介入对话以把控对话节奏、控制用户的负面情绪（对负面情绪用户进行关怀）、在task中把控参与者的对话情绪和对话氛围并给予适当提示

#### 为什么要对话氛围

对话氛围作为一种群体对话度量，是主观者对于整体的主观评价
我们打算发掘群体对话氛围和个人情感/生体情报之间的联系，
以考虑是否利用结合对话氛围维度和个人情感维度来提高虚拟空间对话的顺滑性
并加强虚拟空间的对话体验

包括一个Individual classifier
和一个Group classifier


## Our research
1.考虑不同虚拟环境下进行不同情感诱发对话后，生体情报的表现是否有所不同
（不同MIPs/attention等对HRV的影响）
attention似乎又和视线有关联

2.考虑新的强化学习模型来抽出个人差异
