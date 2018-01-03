##梯度下降
import Curve
import numpy as np
import matplotlib.pyplot as plt

#目标函数
def f(x):
    return x*x -2*x +1

#f(x)的梯度
def g(x):
    return 2*x-2

#梯度下降公式
'''
x_start 下降起点
step 步长
g 梯度
'''
def gd(x_start,step,g):
    x = x_start
    for i in range(20):
        grad = g(x)
        x -= grad*step
        print('[Epoch{0}] grad={1},x={2}'.format(i,grad,x) )
        if abs(grad) < 1e-6:
            break;
    return x;

gd(5,0.1,g)

Curve.curve(f)