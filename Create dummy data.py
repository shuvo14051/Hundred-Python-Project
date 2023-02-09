"""
If you are learning Data Science and 
find it hard to create a dataset for 
practice from scratch, you can either download 
a dataset from Kaggle or create fake data.
"""

from faker import Faker
import pandas as pd
fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.text())
# print(fake.profile())

data = [fake.profile() for i in range(50)]
df = pd.DataFrame(data)
# print(df.head())
# df.to_csv("fake_data.csv")

