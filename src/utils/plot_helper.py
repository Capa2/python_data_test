# utils/plot_helper.py

import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def bar_chart(x_data, y_data, x_label, y_label, title, rotate_labels=False):
    plt.figure(figsize=(10, 5))
    sns.barplot(x=x_data, y=y_data, palette="viridis", hue=x_data, legend=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if rotate_labels:
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

def histogram(data, x_label, y_label, title, bins=10, rotate_labels=False):
    plt.figure(figsize=(10, 5))
    sns.histplot(data, bins=bins, kde=False, color="skyblue")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if rotate_labels:
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

def boxplot(data, x_label, title, y_label, rotate_labels=False):
    plt.figure(figsize=(10, 5))
    sns.boxplot(y=data, color="lightgreen")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if rotate_labels:
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

def heatmap(data, x_column, y_column, value_column, x_label, y_label, title, cmap="YlGnBu"):
    plt.figure(figsize=(12, 6))
    
    pivot_table = data.pivot(index=y_column, columns=x_column, values=value_column)
    
    sns.heatmap(pivot_table, cmap=cmap, annot=True, fmt="g", linewidths=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()

def wordcloud(data, title):
    wordcloud = WordCloud(width=400, height=400, background_color="white", colormap="viridis")
    wordcloud.generate_from_frequencies(data)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)