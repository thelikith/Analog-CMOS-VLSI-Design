import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\racha\Downloads\Techplots 130nm\NMOS\nmos_ft_vd_400.csv'
df = pd.read_csv(file_path)

wavelengths = [130, 230, 330, 430, 530, 630, 730, 830, 930, 1030, 1130, 1230]

plt.figure(figsize=(15, 10))

for i, wavelength in enumerate(wavelengths):
    x_column = df.iloc[:, 2*i]
    y_column = df.iloc[:, 2*i+1]
    plt.plot(x_column, y_column, label=f'L = {wavelength}nm')

plt.title('Frequency vs gm/Id (NMOS)')
plt.xlabel('gm/Id')
plt.ylabel('Frequency (Hz)')
plt.legend()

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', linewidth=0.5)

plt.show()
