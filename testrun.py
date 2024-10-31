import pandas as pd
#opening a csvfile in vscode
df = pd.read_csv(r'C:\Users\MTECH\Desktop\bbygurl\data.csv')
##to index the file from 1
df.index += 1
##to make the column maxpulse in to a  float
df['Maxpulse'] = df["Maxpulse"].astype(float)
#renaming the calories column to Energy column
df = df.rename(columns = {"Calories" : "Energy"})
#to create a new column
df["Gross"]=" "
# to calculate percentage
percentages=[num * 0.1 for num in df['Energy']]
df['Gross']= df['Energy'] + percentages
#cal the max_value in colum energy
max_value = df['Maxpulse'].max()
print(max_value)
# to print columns duration and maxpulse
print(df['Duration'],['Maxpulse'])
#to print the rows from 3 to 5 using slicing
print(df.iloc[2:5])
#to print the rows from 5 to 17 using slicing
print(df.iloc[4:17])

def new_dataframe():
    n=int(input("enter a number: "))
    old_r=range(n, 169, n)
    collect =[]
    for i in old_r:
        val = df.iloc[i]
        collect.append(val)
        
    newdf = pd.DataFrame(collect, index=[x for x in range(1,(len(collect)+1))])
    print(newdf)
new_dataframe()