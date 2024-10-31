import numpy as np
import matplotlib.pyplot as plt
# Load the data
data = np.loadtxt('Data_reg.csv', delimiter=';')
X = data[:, 0]
Y = data[:, 1]
X1 = np.column_stack((X, np.ones(X.shape[0])))
#Weights
W = np.linalg.inv(X1.T @ X1) @ X1.T @ Y
#predicted output
Y1 = X * W[0] + W[1]
#ploting
plt.scatter(X, Y)
plt.plot(X, Y1, color='red')
plt.xlabel('caractéristiques')
plt.ylabel('sorties réelles')
plt.title('REG')
plt.grid(True)
plt.show()
m=20
S=0
for i in range(0,m):
    S+=(W[0]*X[i]+W[1])**2
RSME=np.sqrt((1/m)*S)
print("RSME=",RSME)

