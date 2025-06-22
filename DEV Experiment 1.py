import pandas as pd
import matplotlib.pyplot as plt
data={'Name':['El','Max','Nancy'],
      'Age':[25,30,45],
      'Score':[90,95,98]}
df=pd.DataFrame(data)
print("Dataframe:")
print(df)
print("Data Analysis")
print("Mean Age:",df['Age'].mean())
print("Maximum Score:",df['Score'].max())
print("Mininum score:",df['Score'].min())
plt.figure(figsize=(8,4))
plt.bar(df['Name'],df['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Students')
plt.show()