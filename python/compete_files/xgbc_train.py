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
#输出数据的信息统计
# print(stock_train.info())
#训练特征
feature = []
for i in range(0, 88):
	feature.append('feature' + str(i))
feature.append('group')
# print(feature) 
X = stock_train[feature]
# print('==========================================')
# print(X)
y = stock_train['label']
# print(y)
#对训练集随机采样25%作为测试集(用作训练)，其中X中不包括id
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

#随机选取n个1-20的随机数
era_value = []
for j in range(1, 21):
	era_value.append(j)
b = random.sample(era_value,2)
print(b)
#集合的差集c = era_value - b
c = list(set(era_value).difference(set(b)))

#选取所有符合条件的行
# print(stock_train.loc[stock_train['era'].isin(b)])
s_test = stock_train.loc[stock_train['era'].isin(b)]
s_train = stock_train.loc[stock_train['era'].isin(c)]

X_train_pre = s_train[feature]
y_train = s_train['label']
X_test_pre = s_test[feature]
y_test = s_test['label']

#标准化数据
ss = StandardScaler()
X_train = ss.fit_transform(X_train_pre)
X_test = ss.fit_transform(X_test_pre)
# X_train = ss.fit_transform(X)

#对特征进行特征向量化处理
# vec = DictVectorizer(sparse=False)
# X_train = vec.fit_transform(X_train.to_dict(orient='record'))
# X_test = vec.transform(X_test.to_dict(orient='record'))

#XGBoost进行预测
# Fit the model on 25%
model = XGBClassifier(nthread=3, eval_metric: 'logless')
model.fit(X_train, y_train)
# model.fit(X_train, y)

# XGBClassifier(base_score=0.5, colsample_bylevel=1, colsample_bytree=1,
#               gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=3,
#               min_child_weight=1, missing=None, n_estimators=100, nthread=-1,
#               objective='binary:logistic', reg_alpha=0, reg_lambda=1,
#               scale_pos_weight=1, seed=0, silent=True, subsample=1)

# save the model to disk
filename = 'xgbc_submission.model'
pickle.dump(model, open(filename, 'wb'), -1)

xgbc_y_predict = model.predict_proba(X_test)[:, 1]
#进行准确性评测
print('The accuracy of XGBoost Classifier on testing set:', model.score(X_test, y_test))
#输出预测结果
# xgbc_submission = pd.DataFrame({'id': X_test['id'], 'label': xgbc_y_predict})
# xgbc_submission = pd.DataFrame({'id': stock_test['id'], 'proba': xgbc_y_predict})
# xgbc_submission.to_csv('xgbc_submission.csv', index=False) 

