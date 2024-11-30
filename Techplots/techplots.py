import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\racha\Downloads\BL_Kit\pmostechplots\gmro.csv'
df = pd.read_csv(file_path)
wavelengths = [120, 1020, 1120, 220, 320, 420, 520, 620, 720, 820, 920]
plt.figure(figsize=(10, 6))
for i, wavelength in enumerate(wavelengths):
    x_column = df.iloc[:, 2*i]
    y_column = df.iloc[:, 2*i+1]
    plt.plot(x_column, y_column, label=f'L = {wavelength}nm')


plt.title('gm*ro vs gm/Id (PMOS)')
plt.xlabel('gm/Id')
plt.ylabel('gm*ro')
plt.legend()
plt.show()
