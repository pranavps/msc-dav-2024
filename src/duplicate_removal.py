# The program to demonstrate how to remove duplicates from a DataFrame using the drop_duplicates function.
import pandas as pd

# Sample DataFrame
data = {
        'Name': ['John', 'Anna', 'John', 'Mike'],
        'Age': [28, 22, 28, 32]
        }

# This program demonstrates how to remove duplicates from a DataFrame 
# using the drop_duplicates function.
# The DataFrame below contains duplicate values in the 'Name' column. 
# The drop_duplicates function is then used to remove these duplicate values.
data_frame = pd.DataFrame(data)

# Todo: Lets check the dropped data also
dropped_data = data_frame[data_frame.duplicated()]
print("\nDropped Data:\n", dropped_data)



# Removing duplicates
data_frame = data_frame.drop_duplicates()

print(data_frame)

