from collections import defaultdict
from data.assignment_1_names import name_touple

def print_line(add_space = False):
    print("-" * 40)
    if add_space:
        print("")

def sort_by_length(names, print_flag = False):
    sorted_by_length = sorted(names, key=len)
    def print_sorted_names(): 
        print("Names sorted by length:")
        print_line()
        print(sorted_by_length)
        print_line(True)
    
    if print_flag:
        print_sorted_names()

    return sort_by_length

def sort_alphabetically(names, print_flag = False):
    sorted_alphabetically = sorted(names)
    def print_sorted_names():
        print("Names Sorted alphabetically:")
        print_line()
        print(sorted_alphabetically)
        print_line(True)

    if print_flag:
        print_sorted_names()

    return sort_alphabetically

def count_letters(names, print_flag = False):
    letter_count = defaultdict(int)

    for name in names:
        chars = list(name)
        for char in chars:
            letter_count[str.upper(char)] += 1

    letter_count_sorted = dict(sorted(letter_count.items()))

    def print_sorted_letters():
        print("Letter count in names:")
        print_line()
        for i, (key, value) in enumerate(letter_count_sorted.items()):
            prefix = ", " if i != 0 else ""
            print(f"{prefix}{key}: {value}", end="")
        print("\n")
        print_line(True)

    if print_flag:
        print_sorted_letters()

    return letter_count_sorted
        

def main():
    names = name_touple
    sort_by_length(names, True)
    sort_alphabetically(names, True)
    count_letters(names, True)
    


