import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("dataset.csv")
X = df.drop("Disease", axis=1)
y = df["Disease"]

clf = DecisionTreeClassifier()
clf.fit(X, y)

pickle.dump(clf, open("disease_model.pkl", "wb"))
print("Model trained and saved successfully.")
