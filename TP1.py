#MADE BY ABF DZ
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_excel('BD_MEDIC.xlsx')# Load the data from an Excel file
X = df.iloc[2:, 1:-1].values
y = df.iloc[2:, -1].values
classifier = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
classifier.fit(X,y)
A=int(input("Pression Artérielle Moyenne (mm Hg) : "))
B=int(input("Taux de choléstérol (mg/dl) : "))
Test=[[A,B]]
y_pred = classifier.predict(Test)
print("Attaque Cardiaque Antérieure :",y_pred)
