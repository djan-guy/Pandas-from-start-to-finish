import pandas as pd

df = pd.read_csv('pandas_task_data.csv')
print(df)
print(df.describe())
#df1 = df["Tickets"] # Use for no header
df1 = df[["Tickets"]]
print(df1)
print(df1.mean())
df2 = df[["Gift Shop","Tickets"]]
print(df2)
print(df2.mean())
df3 = df.iloc[0] # Selects row by index
print(df3)
df4 = df.iloc[0:3] # Selects multiple rows by index
print(df4)
df5=df[df["Tickets"] > 400] # Selects rows based on condition
df6=df[df["Day"] == "Monday"]
print(df5)
print(df6)
df7 = df[(df["Tickets"] > 400) & (df["Tickets"] < 500)] # Selects rows based on multiple conditions
df8 = df[(df["Day"] == "Monday") | (df["Day"] == "Tuesday")]
print(df7)
print(df8)
df9 = df.copy() # Copies the CSV into another variable
df9["Row Summary"] = df9[["Tickets", "Gift Shop", "Snack Stand", "Pictures"]].sum(axis=1) # Summarises data for each row seperately
print(df9)
df10 = df.groupby("Day").sum() # Group by one column and summarise
print(df10)
df11 = df.groupby(["Day", "Pay Type"]).sum() # Group and summarise for multiple columns
print(df11)
df12 = df.sort_values(by="Tickets") # Sort values
print(df12)