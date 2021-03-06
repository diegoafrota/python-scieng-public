import numpy as np
import scipy.special
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 256)
cb0 = np.polynomial.Chebyshev.basis(0)(x)
cb1 = np.polynomial.Chebyshev.basis(1)(x)
cb2 = np.polynomial.Chebyshev.basis(2)(x)
cb3 = np.polynomial.Chebyshev.basis(3)(x)

fig, ax = plt.subplots(1, 1)

ax.plot(x, cb0, label='0')
ax.plot(x, cb1, label='1')
ax.plot(x, cb2, label='2')
ax.plot(x, cb3, label='3')
ax.axhline(color="grey", zorder=-1, lw=0.5)
ax.axvline(color="grey", zorder=-1, lw=0.5)
ax.set_ylim(-1.1, 1.1)
ax.set_title('Chebyshev polynomials')
ax.set_xlim(-1, 1)
ax.legend(title='$n$', loc=(0.2, 0.55))

plt.savefig('cheb.pdf')
plt.show()
