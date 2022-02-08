import matplotlib.pyplot as plt

temperature=[17,28,24,30,32,35,49]
precipitation=[300,200,200,250,249,320,330]

plt.xlabel('temperature in degree centigrades')
plt.ylabel('precipation in centimeters')

plt.scatter(temperature,precipitation)
plt.show()

plt.xlabel('temperature in degree centigrades')
plt.ylabel('precipation in centimeters')

plt.plot(temperature,precipitation)
plt.show()