from assignment_1.data_transform import count_letters
from data.assignment_1_names import name_touple
from utils.plot_helper import bar_chart, histogram, wordcloud

def main():
    letter_count = count_letters(name_touple)
    
    letters = list(letter_count.keys())
    counts = list(letter_count.values())
    
    bar_chart(
        x_data=letters, 
        y_data=counts, 
        x_label="Letters", 
        y_label="Frequency", 
        title="Letter Frequency in Names"
    )
    
    histogram(
        data=counts, 
        x_label="Frequency", 
        y_label="Letters", 
        title="Distribution of Letter Frequencies"
    )
    
    wordcloud(
        data=letter_count, 
        title="Letter Frequency Word Cloud"
    )