from mystyle import ms
import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(ms):
    plt.scatter(np.random.randn(50), np.random.randn(50))
    plt.show()
