from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Inputs
x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
#Outputs
y = np.array([5, 20, 14, 32, 22, 38])

# Calculate optimal coefficients (weights)
model = LinearRegression().fit(x, y)

#Check if the model is satisfactory
r_sq = model.score(x, y)
print("Coefficient of determination: ", r_sq)




