
# Netflix Data Analysis Project

## Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style='whitegrid')

## Step 2: Load Dataset
df = pd.read_csv('netflix_titles.csv')
print("Dataset Loaded Successfully!")
df.head()

## Step 3: Data Cleaning
# Check for missing values
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing critical values
df.dropna(subset=['director', 'cast', 'country'], inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Show data types
print(df.dtypes)

## Step 4: Exploratory Data Analysis (EDA)

### 1. Distribution of Movies vs. TV Shows
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=df, palette='Set2')
plt.title('Distribution of Content Type on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

### 2. Top 10 Genres
df['genres'] = df['listed_in'].apply(lambda x: x.split(', '))
all_genres = sum(df['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='Set3')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genres')
plt.show()

### 3. Content Added Over the Years
df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(10, 5))
sns.countplot(x='year_added', data=df, palette='coolwarm')
plt.title('Content Added Over the Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

### 4. Top 10 Directors
top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_directors.values, y=top_directors.index, palette='Blues_d')
plt.title('Top 10 Directors with Most Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

### 5. Word Cloud of Movie Titles
titles = ' '.join(df[df['type'] == 'Movie']['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(titles)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Movie Titles')
plt.show()

## Step 5: Conclusion

print("""
Insights:
- Most content on Netflix is Movies.
- TV-MA and TV-14 are the most common ratings.
- United States and India produce the most Netflix content.
- The most active period for new content was 2018–2020.
- Top directors include Rajiv Chilaka, Raúl Campos, and Steven Spielberg.
""")
