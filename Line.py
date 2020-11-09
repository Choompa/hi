import pandas as pd
import plotly.express as px 
df = pd.read_csv("x.csv") #read csv using pandas 
print (df) 
#fig = px.line(dataframe,x axis, y axis, divider,title="line graph") 
fig = px.line(df, x="even", y="odd",title="line graph") 
fig.show()