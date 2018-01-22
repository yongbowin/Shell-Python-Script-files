import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV
import pickle

stock_test = pd.read_csv('stock_test_data_20170916.csv')
#输出数据的信息统计
# print(stock_train.info())
#训练特征
feature = []
for i in range(0, 88):
	feature.append('feature' + str(i))
feature.append('group')
# print(feature) 
X = stock_test[feature]

#标准化数据
ss = StandardScaler()
X_test = ss.fit_transform(X)

#随机森林进行预测
# model name
filename = 'xgbc_submission.model'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

xgbc_y_predict = loaded_model.predict_proba(X_test)[:, 1]
#进行准确性评测
#print('The accuracy of XGBoost Classifier on testing set:', xgbc.score(X_test, y_test))

#输出预测结果(上边分割数据去掉)
# xgbc_submission = pd.DataFrame({'id': X_test['id'], 'label': xgbc_y_predict})
xgbc_submission = pd.DataFrame({'id': stock_test['id'], 'proba': xgbc_y_predict})
xgbc_submission.to_csv('xgbc_submission.csv', index=False) 