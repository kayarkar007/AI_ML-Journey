# Load Data
import pandas as pd
data= pd.read_csv("students.csv");
# print(data)

#Improve data / Feature the data
subjects=["maths","science","english"]
# for subject in subjects:
    # print(subject)
data["average"]= (data["maths"]+data["science"]+data["english"])/len(subjects)
print(data["average"])