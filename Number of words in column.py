import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", 
                   encoding = 'latin1')
print(df.head())


df['Number of words Article'] = df['Article'].apply(lambda n:len(n.split()))
print(df.columns)
print(df['Number of words Article'])