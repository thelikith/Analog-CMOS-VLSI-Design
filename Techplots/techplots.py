import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = r'C:\Users\racha\Downloads\likith_techplots\nmos\gmro.csv'

# Load the CSV file
data = pd.read_csv(file_path)

# List of lengths and step size
lengths = [45 * i for i in range(1, 13)]  # 45nm to 540nm
num_columns = len(lengths) * 2  # Each length has two columns

# Ensure only the required columns are considered
data = data.iloc[:, :num_columns]

# Plot data
plt.figure(figsize=(12, 8))
for i in range(0, num_columns, 2):
    length = lengths[i // 2]
    x_data = data.iloc[:, i]  # Column for x-axis
    y_data = data.iloc[:, i + 1]  # Column for y-axis
    plt.plot(x_data, y_data, label=f'Length = {length} nm')

# Configure plot aesthetics
plt.title('gm*ro vs gm/Id (NMOS)')
plt.xlabel('gm/Id')
plt.ylabel('gm*ro')
plt.legend()
plt.grid()
plt.show()
