import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def func(x,a,b,c):
   print("a",a)
   print("b",b)
   print("c",c)
   # return berekent y as?
   return a*np.exp(-b*x)-c

xData = np.loadtxt('MMX.txt')
yData = np.loadtxt('MMY.txt')


print(xData.min(), xData.max())
print(yData.min(), yData.max())
FitX = np.linspace(xData[0], xData[-1], 1000)



# Fit an exponential
guess = (-1, 0.1, 0)
popt, pcov = optimize.curve_fit(func, xData, yData, guess)
print("popt", popt)
yEXP = func(FitX, *popt)
print("yexp", len(yEXP))
print("fitx", len(FitX))


plt.figure()
plt.plot(xData, yData, label='Data', marker='o')
plt.plot(FitX, yEXP, 'r-',ls='--', label="Exp Fit")
plt.plot(yData.max(), 'b-',ls='-', label="yMax")

plt.axhline(y = yData.max(), color = 'b', linestyle = '-')

plt.legend()
plt.show()