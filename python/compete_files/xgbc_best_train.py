import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV
import pickle

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

#标准化数据
ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.fit_transform(X_test)
X_train = ss.fit_transform(X)

#对特征进行特征向量化处理
# vec = DictVectorizer(sparse=False)
# X_train = vec.fit_transform(X_train.to_dict(orient='record'))
# X_test = vec.transform(X_test.to_dict(orient='record'))

#使用并行网格搜索寻找更好的超参数组合，期待提高性能
nestimators = []
for i in range(100, 1100, 200):
	nestimators.append(i)
print(nestimators)
maxdepth = []
for j in range(2, 7):
	maxdepth.append(i)
print(maxdepth)
#range(2, 7)是错误写法
params = {'max_depth':maxdepth, 'n_estimators':nestimators, 'learning_rate':[0.05, 0.1, 0.25, 0.5, 1.0]}
xgbc_best = XGBClassifier()
model = GridSearchCV(xgbc_best, params, n_jobs=27, cv=5, verbose=1)
model.fit(X_train, y)

# save the model to disk
filename = 'xgbc_best_submission.model'
pickle.dump(model, open(filename, 'wb'), -1)
