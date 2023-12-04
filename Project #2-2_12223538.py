import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np

def sort_dataset(dataset_df):
        sorted_df = dataset_df.sort_values(by='p_year', ascending=True)
        return sorted_df

def split_dataset(dataset_df):
        dataset_df['salary'] *= 0.001
        train_df = dataset_df.iloc[:1718]
        test_df = dataset_df.iloc[1718:]

        X_train = train_df.drop('salary', axis=1)
        X_test = test_df.drop('salary', axis=1)
        Y_train = train_df['salary']
        Y_test = test_df['salary']

        return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	numerical_columns = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
	numerical_df = dataset_df[numerical_columns]
	return numerical_df

def train_predict_decision_tree(X_train, Y_train, X_test):
	decision_tree_model = DecisionTreeRegressor()
	decision_tree_model.fit(X_train, Y_train)

	prediction = decision_tree_model.predict(X_test)
	return prediction

def train_predict_random_forest(X_train, Y_train, X_test):
	random_forest_model = RandomForestRegressor()
	random_forest_model.fit(X_train, Y_train)

	prediction = random_forest_model.predict(X_test)
	return prediction

def train_predict_svm(X_train, Y_train, X_test):
	pipeline = make_pipeline(
                StandardScaler(),
                SVR())
	pipeline.fit(X_train, Y_train)

	prediction = pipeline.predict(X_test)
	return prediction

def calculate_RMSE(labels, predictions):
	rmse = np.sqrt(np.mean((predictions - labels) ** 2))
	return rmse

if __name__=='__main__':
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
