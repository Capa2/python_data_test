import os
import matplotlib.pyplot as plt
from functools import wraps

def plot_to_pdf(folder_path, base_filename="plot"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ensure the output directory exists
            os.makedirs(folder_path, exist_ok=True)
            plt.ioff()  # Turn off interactive plotting
            
            # Run the plotting function(s)
            func(*args, **kwargs)
            
            # Loop through all active figures and save each as a PDF
            for i, figure_num in enumerate(plt.get_fignums(), start=1):
                fig = plt.figure(figure_num)
                pdf_path = os.path.join(folder_path, f"{base_filename}_{i}.pdf")
                fig.savefig(pdf_path, format="pdf")
                plt.close(fig)  # Close the figure after saving
                print(f"Saved {pdf_path}")
            
            print("All figures saved as PNG files.")
        return wrapper
    return decorator