import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Fake Dataset Columns:", fake_df.columns.tolist())
print("True Dataset Columns:", true_df.columns.tolist())

fake_df.head()
fake_df.tail()

true_df.head()
true_df.tail()

fake_df['label'] = 0
true_df['label'] = 1

data_df = pd.concat([fake_df, true_df], ignore_index=True)

data_df.shape

data_df.info()

print("\nMissing Values:\n", data_df.isnull().sum())

print("\n Duplicate Rows:", data_df.duplicated().sum())

data_df = data_df.drop_duplicates().reset_index(drop=True)

data_df.shape

data_df.duplicated().sum()
