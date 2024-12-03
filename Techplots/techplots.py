import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\racha\Downloads\130nm\NMOS\nmos-idw-vd-400.csv'
df = pd.read_csv(file_path)

wavelengths = [130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530]

plt.figure(figsize=(15, 10))

for i, wavelength in enumerate(wavelengths):
    x_column = df.iloc[:, 2*i]
    y_column = df.iloc[:, 2*i+1]
    plt.plot(x_column, y_column, label=f'L = {wavelength}nm')

plt.title('Id/W vs gm/Id (NMOS)')
plt.xlabel('gm/Id')
plt.ylabel('Id/W')
plt.legend()

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', linewidth=0.5)

plt.show()
