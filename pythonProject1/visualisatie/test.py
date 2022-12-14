import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

x = [50, 50]

fig, axarr = plt.subplots(3)

# draw the initial pie chart
axarr[0].pie(x,autopct='%1.1f%%')
axarr[0].set_position([0.25,0.4,.5,.5])

# create the slider
axarr[1].set_position([0.1, 0.35, 0.8, 0.03])
risk = Slider(axarr[1], 'Risk', 0.1, 100.0, valinit=x[0])

# create some other random plot below the slider
axarr[2].plot(np.random.rand(10))
axarr[2].set_position([0.1,0.1,.8,.2])

def update(val):
    axarr[0].clear()
    axarr[0].pie([val, 100-val],autopct='%1.1f%%')
    fig.canvas.draw_idle()

risk.on_changed(update)

plt.show()


# pacman test
import matplotlib.pyplot as plt

waltuh = True
labels = ['pacman', 'not pacman']
values = [80, 20,]
colors = ['#FFFF00', 'black']
test = [80, 90, 99.9, 90]
test1 = [20, 10, 0.1, 10]
loop = 5

with plt.ion():
    while loop > 1:
        for index in range(len(test)):
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('black')
            values = [test[index], test1[index]]
            ax.pie(values, labels=labels, colors=colors, startangle=10)
            plt.pause(0.5)
        loop += -1