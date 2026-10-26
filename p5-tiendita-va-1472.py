import matplotlib.pyplot as plt
import numpy as np

# jose solis nc 1472

num_mes = np.array(
    [1,2,3,4,5,6]
)
venta_manda2 = np.array(
    [0,2000,3500,7000,15000,20000]
)
plt.plot(num_mes, venta_manda2,
         marker ="o",
         markersize =10,
         markerfacecolor = "#F54927",
         markeredgecolor = "yellow"
         )
plt.show()


