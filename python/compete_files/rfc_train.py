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
feature.append('label')
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

#随机森林进行预测
# Fit the model on 25%
model = RandomForestClassifier(n_jobs=27)
# model.fit(X_train, y_train)
model.fit(X_train, y)

# save the model to disk
filename = 'rfc_submission.model'
pickle.dump(model, open(filename, 'wb'), -1)

# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# #进行准确评测
# result = loaded_model.score(X_test, y_test)
# print('The accuracy of RFC on testing set:', result)

# rfc_y_predict = loaded_model.predict_proba(X_test).ix[:, 1]
# #输出预测结果(上边分割数据去掉)
# # rfc_submission = pd.DataFrame({'id': X_test['id'], 'label': rfc_y_predict})
# rfc_submission = pd.DataFrame({'label': rfc_y_predict})
# rfc_submission.to_csv('rfc_submission.csv', index=False)
