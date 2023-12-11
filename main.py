import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix

field_size = 1024
field = coo_matrix((field_size, field_size), dtype=int).tolil()

ant_position = np.array([512, 512])
ant_direction = np.array([-1, 0])

while 0 < ant_position[0] < 1024 and 0 < ant_position[1] < 1024:

    current_color = field[ant_position[0], ant_position[1]]

    if current_color == 0:
        ant_direction = np.array([-ant_direction[1], ant_direction[0]])
    else:
        ant_direction = np.array([ant_direction[1], -ant_direction[0]])

    field[ant_position[0], ant_position[1]] = 1 - current_color

    ant_position += ant_direction

plt.imshow(field.toarray(), cmap='gray_r', interpolation='none')
plt.show()

black_cells_count = np.count_nonzero(field.toarray())
print(f"Количество черных клеток: {black_cells_count}")
