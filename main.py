import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

x = np.linspace(-5, 5, 100)


def gauss(sigma, mu):
    return 1 / (sigma * (2 * np.pi) ** .5) * np.e ** (-(x - mu) ** 2 / (2 * sigma ** 2))


dpi = 120
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

plt.plot(x, gauss(0.5, 1.0), 'ro-')
plt.plot(x, gauss(7.0, 0.5), 'go-')
plt.plot(x, gauss(1.5, 0.0), 'bo-')

plt.legend(['sigma = 0.5, mu = 1.0',
            'sigma = 1.0, mu = 0.5',
            'sigma = 1.5, mu = 0.0'], loc='upper left')
plt.cool()
fig.savefig('gauss.png')
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()