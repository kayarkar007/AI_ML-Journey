# from fastapi import FastAPI
# import pickle
# import numpy as np

# app = FastAPI()

# # Load saved objects
# model = pickle.load(open("model/model.pkl", "rb"))
# scaler = pickle.load(open("model/scaler.pkl", "rb"))

# @app.get("/")
# def home():
#     return {"message": "House Price API running"}

# @app.post("/predict")
# def predict(data: dict):

#     # Convert input → array
#     features = np.array([
#         data["OverallQual"],
#         data["GrLivArea"],
#         data["GarageCars"],
#         data["TotalBsmtSF"],
#         data["YearBuilt"],
#         data["FullBath"]
#     ]).reshape(1, -1)

#     # Scale
#     features = scaler.transform(features)

#     # Predict
#     prediction = model.predict(features)[0]

#     return {"Predicted Price": float(prediction)}


from fastapi import FastAPI
import pickle
import numpy as np
app=FastAPI()
model=pickle.load(open("model/model.pkl","rb"))
scaler=pickle.load(open("model/scaler.pkl","rb"))

@app.get("/")
def home():
    return {"message":"House Price API running"}

@app.post("/predict")

def predict(data:dict):
    # Convert input → array
    features = np.array([
        data["OverallQual"],
        data["GrLivArea"],
        data["GarageCars"],
        data["TotalBsmtSF"],
        data["YearBuilt"],
        data["FullBath"]
    ]).reshape(1, -1)

    # Scale
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)[0]


    return {"Predicted Price": float(prediction)}     