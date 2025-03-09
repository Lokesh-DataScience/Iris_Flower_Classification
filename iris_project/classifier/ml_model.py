import pickle
import numpy as np

with open("..\\model\\saved_model\\iris_model.pkl","rb") as f:
    model = pickle.load(f)

def predict_iris(features):
    features = np.array(features).reshape(1,-1)
    prediction = model.predict(features)
    classes = ["Setosa", "Versicolor", "Virginica"]
    return classes[prediction[0]]