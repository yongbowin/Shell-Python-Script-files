import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV
import pickle
import random

stock_train = pd.read_csv('stock_train_data_20170916.csv')

# print(stock_train.info())

#统计各组数量
era = stock_train['era']
# # print(era)
# print(era.count())
# era_list = era.tolist()

# for i in range(1, 21):
# 	print('元素' + str(i) + '的个数:' + str(era_list.count(i)))

#随机选取n个1-20的随机数
era_value = []
for j in range(1, 21):
	era_value.append(j)
b = random.sample(era_value,5)
print(b)
#集合的差集era_value - b
c = list(set(era_value).difference(set(b)))
print(c)

# print(stock_train.loc[stock_train['era'].isin(b)])