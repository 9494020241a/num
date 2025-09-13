import time
from IPython.display import clear_output, display, HTML

for i in range(1, 11):
    clear_output(wait=True) # Clear the previous output
    display(HTML(f'<h1 style="font-size: 200px; text-align: center;">{i}</h1>')) # Display the current number with a very large font and center it
    time.sleep(5) # Wait for 1 second