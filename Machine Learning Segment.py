import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def Machine_Learning(dataset):
	# import the generated csv file for Income Data 
	income = pd.read_csv('Income Data File.csv' , index_col = 0)

	# For cleaning, need to split the columns that have more than two categories, into the # of categories as columns
	Uni = pd.get_dummies(income['University'], drop_first = True)
	Pro = pd.get_dummies(income['Program'], drop_first = True)
	# Schol = pd.get_dummies(income['Scholarship'], drop_first = True)

	# include the dummy variables into the dataframe
	income['Uni1'] = Uni[1]
	income['Uni2'] = Uni[2]
	income['Uni3'] = Uni[3]
	income['Uni4'] = Uni[4]
	income['Uni5'] = Uni[5]

	income['Pro1'] = Pro[1]
	income['Pro2'] = Pro[2]
	income['Pro3'] = Pro[3]
	income['Pro4'] = Pro[4]

	# remove the now redundant columns
	income = income.drop(['University', 'Program', 'Criminal Record', 'Scholarship'], axis = 1)

	# Create train-test split set

	X = income.drop(['Income'], axis=1)
	Y = income['Income']

	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

	# We've used three different training models and are moving forward with KNearest Neighbours
	knn = KNeighborsClassifier(n_neighbors=3)
	knn.fit(X_train,y_train)

	pred = knn.predict(np.array(dataset))

	if pred[0] == 'low':
		return 45000
	elif pred[0] == 'mid':
		return 60000
	else:
		return 75000










