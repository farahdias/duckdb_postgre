import sys
import os

# Add the other directory to the system path
sys.path.append(os.path.join(os.path.dirname(_file_), 'other_directory'))

# Import the other script
import other_script

if _name_ == '_main_':
    # Call a function from other_script if needed
    other_script.some_function()  # Replace with actual function call