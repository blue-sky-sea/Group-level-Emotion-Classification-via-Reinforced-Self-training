# -*- coding: utf-8 -*-
import gym
import numpy as np

import numpy as np
import copy
global SS
SS=0

class CS_Agent:
    def __init__(self,df_train_labeled,df_train_unlabeled,df_test,df_val):
        self.df_train_labeled = df_train_labeled
        self.df_train_unlabeled = df_train_unlabeled
        self.df_test = df_test 
        self.df_val = df_val

        self.df_train_labeled_ = self.df_train_labeled
        self.df_train_unlabeled_ = self.df_train_unlabeled
        self.df_test_ = self.df_test 
        self.df_val_ = self.df_val

        self.base_clf = self.trainModel(df_train_labeled)

        #当前遍历的第n个unlabeled数据
        self.now_iter_num = 0

    def reset(self):
        #将Agent恢复到初始状态
        self.df_train_labeled_ = df_train_labeled
        self.df_train_unlabeled_ = df_train_unlabeled
        self.df_test_ = df_test 
        self.df_val_ = df_val

    def getUnlabeledlength(self):
        return len(self.df_train_unlabeled_)
    def setTrain_labeled_(self,df_train_unlabeled):
        self.df_train_labeled_ = df_train_labeled

    def predictDataset(self,df_train):
        X = df_train_labeled[['MntMeatProducts', 'MntWines']]
        proba = self.base_clf.predict_proba(X)

        return proba
    def trainModel(self,df_train):
      X_baseline = df_train[['MntMeatProducts', 'MntWines']]
      #y_baseline = df_train['Dependents_Target'].values
      y_baseline = df_train['Dependents_Flag'].values
      #input(y_baseline)

      model = SVC(kernel='rbf', 
          probability=True, 
          C=1.0, # default = 1.0
          gamma='scale', # default = 'scale'
          random_state=0
      )
      clf = model.fit(X_baseline, y_baseline)
      return clf 
    def step(self, actions):
        observation = None
        done = False
        reward = 0
        Info = [] 


        i=0
        delete_unlabeled_i = []
        
        for action in actions:
            #选择，并加入df_train_labeled_中，作为已假定标签的数据集
            if(action == 0):
                #不加入到labeled的数据集中
                #print("pass")
                pass
            elif(action == 1):
                new_df = self.df_train_unlabeled_.iloc[[i]]
                delete_unlabeled_i.append(i)

                #
                self.df_train_labeled_ = self.df_train_labeled_.append(new_df)
                #print(len( self.df_train_labeled_),len(new_df))
                #print(len(self.df_train_labeled_))

                """
                x = new_df[['MntMeatProducts', 'MntWines']]
                predict = self.base_clf.predict(x)
                if(predict[0]==0):
                    reward = -1
                elif(predict[0]==1):
                    reward = 1"""
            i = i + 1 
        #print(len(self.df_train_labeled_))
        #input(len(self.df_train_labeled_))
        #print(self.df_train_labeled_)
        #input()
        clf = self.trainModel(self.df_train_labeled_)
        X_val = self.df_val[['MntMeatProducts', 'MntWines']]
        y_val = self.df_val['Dependents_Flag'].values
        accuracy_score = clf.score(X_val, y_val)
        #print(self.base_clf.score(X_val, y_val))
        reward =  accuracy_score
        print(reward)

        self.df_train_unlabeled_ = self.df_train_unlabeled_.drop(index = self.df_train_unlabeled_.index[[delete_unlabeled_i]])

        self.now_iter_num = self.now_iter_num +1

        #if(self.now_iter_num == len(self.df_train_unlabeled_)):
            #done = True           
        #print(len(self.df_train_unlabeled_))
        #什么时候结束循环呢？ sample <10
        if(len(self.df_train_unlabeled_)<=10):
            done = True       


        self.now_iter_num = 0

        
        return observation, reward, done, Info 
        
def try_CS(df_train_labeled,df_train_unlabeled,df_test,df_val):
    env = CS_Agent(df_train_labeled,df_train_unlabeled,df_test,df_val)
    env.reset()

    # episodes of game
    random_episodes = 0
    # sum of reward of game per episode
    reward_sum = 0

    R=0
    while random_episodes < 2:
        R=R+1
        print("ROUND-",R," episode:",random_episodes)
        #env.reset()
        #observation, reward, done, _ = env.step(np.random.randint(0, 2))
        observation, reward, done, _ = env.step(np.random.randint(2,size = env.getUnlabeledlength()))
        #print( observation, reward, done )

        reward_sum += reward
        if done:
            random_episodes += 1
            print("Reward for this episode was: {}".format(reward_sum))
            reward_sum = 0
            env.reset()
    pass

if __name__ == '__main__':
    try_CS(df_train_labeled,df_train_unlabeled,df_test,df_val)