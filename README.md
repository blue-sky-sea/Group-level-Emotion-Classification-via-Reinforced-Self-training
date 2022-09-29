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
ネガティブな話題
Talk about a recent sad thing悲伤的事情  
Talk about the biggest worry担忧的事情  
Talk about the things that make u angry让人生气的事情  
Talk about the things that make people shy and embarrassed让人脸红/尴尬的事情  
Talk about the disgusting things that make you sick 讨论让人感到恶心不爽的事情
Talk about a recent failure讨论最近的一次失败
talk about a time when you felt alone.讨论你感到孤独的时候

積極的な話題
Talk about a happy thing开心的事情  
Talk about your hobby兴趣爱好  
Talk about the places you would most like to visit最想去旅游的地方
Talk about the type you like喜欢的类型  
Talk about your dream or future plan谈论你的梦想或者未来规划
Indoor?Outdoor?Why?喜欢出门吗，为什么？

議論を呼びやすい話題
Talk about your research or project谈论你的研究或者项目  
Whether to agree with Dink？Why？同意丁克吗，为什么  
Talk about your views on declining birthrate and aging population少子高齢化的看法
Use IT for economic recovery in the post-corona era用IT技术进行后新冠时代的经济恢复
Should English be the official language in Japanese companies?社内公用語を英語に
What do people live for?人活着是为了什么
Is marriage really necessary?结婚真的有必要吗
What do you think about the future of VR, AR and why?你对VR，AR的未来有什么看法，为什么？



3.Talk about the things that make u angry让人生气的事情
#### Emotion model
PAD (Pleasure, Arousal, Dominance) model

## To solve

#### 为什么要VR

Contactless Virtual Social become popular in recent years  

  
A smart virtual space/virtual agent is expected,
to help conversation on those online virtual world platforms

  
Dialogue atmosphere is a metric used to describe group-level interactions，which is different from individual emotion   

![image](https://user-images.githubusercontent.com/26008298/175459385-0af61f3d-3281-4470-bc40-1ed7ae706b6d.png)

## Experiment Design


![image](https://user-images.githubusercontent.com/26008298/175459542-99416628-b7be-430f-be25-11bc93b64de7.png)  

## Experiment Schedule
![image](https://user-images.githubusercontent.com/26008298/175459710-ff16b530-cf69-4324-8133-b99853e133e6.png)  

## Related Project:VIVEEyeTracking  
https://github.com/yamaguchi-three-KBS/VIveEyeTracking


# Reinforcement Learning Network
(1)State:
	preprocessed biometric data and confidence point

(2)Action:  
	Two class, whether choose this sample or not

(3)Reward:
	Based on the model’s performance on validation set

(4)Policy Network: 
	multi-layer perception(MLP)
	Input is State
	Output is Action’s probability distribution

#Motivation
most of the existing successfule stories of deep learning are still based on supervised learnng,
for example, object recognition,machine translation,text calssification.However, in many applications, 
it is not realistic to obtain large amount of labeled data.  

#DRL
DRL is a method that can solve human-level task.RL+DL is powerful and flexible

#Chanllenges in co-training
Choosing highly-confident self-labeled examples could be suboptimal  
Sampling bias shift is common.

#Assumption
not all the unlabeled data are useful  
we hope to get data in classifier boundary  

#Idea
performance-driven semi-supervised learning that learns an unlabeled data selection policy with RL,
instead of using random sampling.

#Reinforced SSL
1.Partition the unlabeled data space  
2.Train a RL agent to select useful unlabeled data
3.Reward:change in accuracy on the validation set
4.Clustering on unlabeled dataset based on the Jaccard Similarity, Partition the unlabeled dataset U into {U1,U2,...,Uk}
5.The first added sample for each subset Uk is recorded as the representative sample-

#Result on SAI's confidence Dataset
0.584 on initial accuracy  
0.71 accuracy on 3 class classification after Reinforcement Learning

