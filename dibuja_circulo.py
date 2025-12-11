import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Medidas en centímetros
fig, ax = plt.subplots(figsize=(4, 4))  # Tamaño de la figura en pulgadas (1 pulgada = 2.54 cm)

# Crear un círculo verde de 3 cm de diámetro (radio = 1.5 cm)
circle = patches.Circle((2, 2), 1.5/2.54, color='green')  # Convertir cm a pulgadas
ax.add_patch(circle)

# Ajustar límites y aspecto
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

plt.show()
