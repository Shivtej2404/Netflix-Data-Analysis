import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv("netflix.csv")
print(df.head())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'])

# Handle missing values
df.dropna(subset=['director', 'country'], inplace=True)

# Extract year, month, day
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month
df['day'] = df['date_added'].dt.day

# Preview cleaned data
print(df.info())

#content type distribution 
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title("Content Type Distribution on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("type_distribution.png")
plt.close()

# top 10 genres
df['genres'] = df['listed_in'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])
all_genres = sum(df['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='Set3')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.close()

#rating 
rating_counts = df['rating'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette='Set1')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.close()

#top 10 countries
country_counts = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis')
plt.title("Top 10 Countries by Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

#yearly addition 
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='year', palette='coolwarm')
plt.title("Content Added Over the Years")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("yearly_additions.png")
plt.close()

#word cloud of titles
titles = ' '.join(df['title'].dropna().tolist())
wordcloud = WordCloud(width=1000, height=400, background_color='black').generate(titles)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig("wordcloud_titles.png")
plt.close()

#top 10 directors
top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, palette='cubehelix')
plt.title("Top 10 Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.tight_layout()
plt.savefig("top_directors.png")
plt.close()
