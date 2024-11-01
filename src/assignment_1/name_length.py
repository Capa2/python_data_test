import statistics
from data.assignment_1_names import name_touple
from utils.plot_helper import box_plot, histogram

def calc_name_lengths(names):
    lengths = [len(name) for name in names]
    average = sum(lengths) / len(lengths)
    median = statistics.median(lengths)
    return average, median, lengths

def main():
    average, median, lengths = calc_name_lengths(name_touple)
    
    box_plot(
        data=lengths, 
        x_label="Name length",
        y_label="Letters",
        title=f"Name length (Median = {round(median)})"
    )

    histogram(
        data=lengths, 
        x_label="Name length", 
        y_label="Letters", 
        title=f"Distribution of length (Average = {round(average,1)})", 
        bins=6
    )
