import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 3, figsize=(3, 6))

categories = ["<10", "10-19", "20-39", "40+"]
titles = [['Аргентина', 'Бразилия', 'Россия'], ['Буэнос-Айрес', 'Бразилиа', 'Москва']]

for i in range(2):
    for j in range(3):
        values = np.random.randint(3, 40, size=4)
        err_p = np.random.randint(1, 5, size=4)
        
        axs[i][j].bar(categories, values,
            yerr=[values, err_p],
            color='#000000',
            capsize=10,
            linewidth=2)
            
        axs[i][j].set_title(titles[i][j])
        axs[i][j].set(ylabel='Население, %')

plt.show()