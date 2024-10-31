import matplotlib.pyplot as plt
from assignment_1 import letter_plot
from assignment_1 import name_length
from assignment_2 import data_transformer
from assignment_3 import data_handler
from assignment_5 import nortwind
import big_data
import big_data.main
from utils import db_config

def main():
    run_assignment = 6
    
    if (run_assignment) == 1:
            letter_plot.main()
            name_length.main() 
            plt.show() 
    
    if (run_assignment) == 2:
            data_transformer.main()            
    
    if (run_assignment) == 3:
        data_handler.main()
    
    if (run_assignment == 4):
        print("Check Diagram and SQL file")
    
    if (run_assignment == 5):
         nortwind.main()
         plt.show()
    if (run_assignment == 6):
         big_data.main.main()
         
if __name__ == "__main__":
    main()
