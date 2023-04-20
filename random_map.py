import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
for i in range(10):
#class
    map_w = 50
    map_h = 50
    G = np.zeros(map_w*map_h)
    obs_num = int(G.size * 0.03)  
    obs_a = np.random.randint(low=0, high=G.size, size=obs_num) 
    G[obs_a] = 1 
    map_test = G.reshape([map_w, map_h]) 
    cmap = colors.ListedColormap(['none', 'black', 'white', 'magenta', 'yellow', 'cyan', 'green', 'red', 'blue'])
    plt.imshow(map_test, cmap=cmap, interpolation='nearest', vmin=0, vmax=7)
    plt.title(f"Envrioment PE")
    plt.show()
