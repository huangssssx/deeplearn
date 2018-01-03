#曲线绘画
import numpy as np
import matplotlib.pyplot as plt

def curve(f):
    x = np.linspace(-10,10,100)
    y = f(x)
    plt.plot(x,y)


