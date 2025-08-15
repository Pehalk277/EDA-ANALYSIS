import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Here I Have Loaded My CSV File
df = pd.read_csv("shortened_data_50_rows (1).csv")
print("OUR CSV FILE\n",df)
# Here i have decribed my data
des=df.describe()
print("DESCRIPTION OF THE WHOLE DATA:\n",des)
#Here I Am Cleaning My Data
result=df["New deaths"].isnull()
print(result)
res=df["Recovered"].notnull()
print(res)
dev=df["1 week change"].dropna()
print(dev)
div=df["New cases"].fillna(5)
print(div)
var = pd.read_csv("shortened_data_50_rows (1).csv")
print(var)
# It Is Used To Make A Grid
sns.set_style("darkgrid")
# Here I Have Described The Size For The Figure
plt.figure(figsize=(18,6))
# BAR GRAPH
plt.subplot(1, 3, 1)
sns.barplot(data=var,x="WHO Region",y="Confirmed",palette="RdYlGn",saturation=0.5,
            order=["Africa","America","Europe","Eastern Mediterranean","South-East Asia","Western Pacific"],ci=0)
plt.xticks(rotation=45, fontsize=10)
plt.title("Confirmed Cases by WHO Region", fontsize=12)
# HISTOGRAM
plt.subplot(1, 3, 2)
sns.histplot(var["New cases"],kde=True,color="g",bins=50)
plt.title("Distribution of New Cases", fontsize=12)
plt.xlabel("New Cases")
# LINE PLOT
plt.subplot(1, 3, 3)
sns.lineplot(x="Recovered",y="Active",data=var,color="r", marker="o")
plt.title("Recovered vs Active Cases", fontsize=12)
# I Have Done This For Spacing
plt.tight_layout()
# It Is Used To Show The Graph
plt.show()