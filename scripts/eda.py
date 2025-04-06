import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 5)

sns.countplot(x='label', data=data_df, palette='Set2')
plt.xticks([0, 1], ['Fake', 'Real'])
plt.title('Distribution of Fake vs Real News')
plt.xlabel('News Type')
plt.ylabel('Count')
plt.show()

data_df['title_length'] = data_df['title'].apply(len)
data_df['word_count'] = data_df['title'].apply(lambda x: len(str(x).split()))

sns.histplot(data_df['title_length'], bins=50, kde=True, color='skyblue')
plt.title('Title Length Distribution (Character Count)')
plt.xlabel('Title Length')
plt.ylabel('Frequency')
plt.show()

sns.histplot(data_df['word_count'], bins=30, kde=True, color='coral')
plt.title('Title Word Count Distribution')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.show()

print("Average Title Length (Fake):", data_df[data_df['label'] == 0]['title_length'].mean())
print("Average Title Length (Real):", data_df[data_df['label'] == 1]['title_length'].mean())

print("Average Word Count (Fake):", data_df[data_df['label'] == 0]['word_count'].mean())
print("Average Word Count (Real):", data_df[data_df['label'] == 1]['word_count'].mean())

if 'subject' in data_df.columns:
    sns.countplot(y='subject', data=data_df, order=data_df['subject'].value_counts().index, palette='pastel')
    plt.title('Subject Distribution in News')
    plt.xlabel('Count')
    plt.ylabel('Subject')
    plt.show()
    
data_df['date'] = pd.to_datetime(data_df['date'], errors='coerce')
data_df['year'] = data_df['date'].dt.year

sns.countplot(x='year', data=data_df, palette='coolwarm')
plt.title('Articles Published per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
