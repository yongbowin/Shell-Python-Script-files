import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV

stock_train = pd.read_csv('stock_train_data_20170916.csv')
#输出数据的信息统计
# print(stock_train.info())
#训练特征
feature = []
for i in range(0, 88):
	feature.append('feature' + str(i))
feature.append('group')
feature.append('label')
# print(feature) 
X = stock_train[feature]
# print('==========================================')
# print(X)
y = stock_train['label']
# print(y)
#对训练集随机采样25%作为测试集(用作训练)，其中X中不包括id
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

#标准化数据
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

#对特征进行特征向量化处理
# vec = DictVectorizer(sparse=False)
# X_train = vec.fit_transform(X_train.to_dict(orient='record'))
# X_test = vec.transform(X_test.to_dict(orient='record'))

#随机森林进行预测
rfc = RandomForestClassifier(n_jobs=7)
rfc.fit(X_train, y_train)
rfc_y_predict = rfc.predict(X_test)
#进行准确评测
print('The accuracy of RFC on testing set:', rfc.score(X_test, y_test))
#输出预测结果(上边分割数据去掉)
# rfc_submission = pd.DataFrame({'id': X_test['id'], 'label': rfc_y_predict})
rfc_submission = pd.DataFrame({'label': rfc_y_predict})
rfc_submission.to_csv('rfc_submission.csv', index=False)

#XGBoost进行预测
xgbc = XGBClassifier(nthread=7)
xgbc.fit(X_train, y_train)
# XGBClassifier(base_score=0.5, colsample_bylevel=1, colsample_bytree=1,
#               gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=3,
#               min_child_weight=1, missing=None, n_estimators=100, nthread=-1,
#               objective='binary:logistic', reg_alpha=0, reg_lambda=1,
#               scale_pos_weight=1, seed=0, silent=True, subsample=1)
xgbc_y_predict = xgbc.predict(X_test)
#进行准确性评测
print('The accuracy of XGBoost Classifier on testing set:', xgbc.score(X_test, y_test))

#输出预测结果(上边分割数据去掉)
# xgbc_submission = pd.DataFrame({'id': X_test['id'], 'label': xgbc_y_predict})
xgbc_submission = pd.DataFrame({'label': xgbc_y_predict})
xgbc_submission.to_csv('xgbc_submission.csv', index=False) 

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
gs = GridSearchCV(xgbc_best, params, n_jobs=7, cv=5, verbose=1)
gs.fit(X_train, y_train)

xgbc_best_y_predict = gs.predict(X_test)
# xgbc_best_submission = pd.DataFrame({'id': X_test['id'], 'label': xgbc_best_y_predict})
xgbc_best_submission = pd.DataFrame({'label': xgbc_best_y_predict})
xgbc_best_submission.to_csv('xgbc_best_submission.csv', index=False)