import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob

path = '/home/amishra97/Contact_Simulation/Non-adhesive_simulations/Animation/*.png'
png_files = sorted(glob.glob(path))

fig = plt.figure()
ax = fig.add_subplot(111)

def animate(i):
    img = plt.imread(png_files[i])
    ax.imshow(img)

ani = animation.FuncAnimation(fig, animate, frames=len(png_files), interval=1000, repeat=False)
ani.save('animatedCP.gif', writer='pillow')
