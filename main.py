from projet_algo import carreler
import matplotlib.pyplot as plt
import random

 
if __name__ == "__main__":
    n = int(input("Entrez la taille de l'échiquier (n doit être une puissance de 2) : "))

    case_def_x = int(input(f"Entrez la ligne de la case définie (entre 0 et {n-1}) : "))
    case_def_y = int(input(f"Entrez la colonne de la case définie (entre 0 et {n-1}) : "))
    case_def = (case_def_x, case_def_y)
    
    echiquier = [[0 for _ in range(n)] for _ in range(n)]
    echiquier[case_def[0]][case_def[1]] = -1
    
    for ligne in echiquier:
        print(" ".join(f"{case:2}" for case in ligne))
    
    carrelage,nb=carreler(echiquier, n, case_def)

    for ligne in carrelage:
        print(" ".join(map(str, ligne)))
        
        



# Générer une couleur aléatoire pour chaque valeur unique (excepté 999)
unique_values = set(val for row in carrelage for val in row if val != -1)
color_map = {val: f"#{random.randint(0, 0xFFFFFF):06x}" for val in unique_values}

# Création des sous-figures
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Première sous-figure : Tableau avec cases blanches et case défectueuse
ax = axes[0]
for i in range(n):
    for j in range(n):
        if (i, j) == case_def:  # Case défectueuse
            color = "black"
        else:
            color = "white"

        # Dessiner un carré coloré
        rect = plt.Rectangle((j, n - i - 1), 1, 1, color=color)
        ax.add_patch(rect)

# Configurer l'affichage de la première sous-figure
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_aspect('equal')
ax.grid(color="gray", linestyle='--', linewidth=0.5)
ax.set_title("Tableau avec la case défectueuse")

# Deuxième sous-figure : Tableau carrelé avec couleurs en fonction des valeurs
ax2 = axes[1]
for i in range(n):
    for j in range(n):
        value = carrelage[i][j]
        if value == -1:  # Case défectueuse
            color = "black"
            text_color = "white"
        else:
            # Utiliser la couleur associée à la valeur
            color = color_map[value]
            text_color = "black"

        # Dessiner un carré coloré
        rect = plt.Rectangle((j, n - i - 1), 1, 1, color=color)
        ax2.add_patch(rect)

        # Ajouter le texte pour les cases normales
        if value != -1:
            ax2.text(
                j + 0.5, n - i - 0.5, str(value),
                color=text_color, ha="center", va="center", fontsize=8
            )

# Configurer l'affichage de la deuxième sous-figure
ax2.set_xlim(0, n)
ax2.set_ylim(0, n)
ax2.set_xticks(range(n))
ax2.set_yticks(range(n))
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_aspect('equal')
ax2.grid(color="gray", linestyle='--', linewidth=0.5)
ax2.set_title("Tableau carrelé")

# Afficher les deux figures côte à côte
plt.tight_layout()
image_path = "tableau_carrelage.png"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.show()