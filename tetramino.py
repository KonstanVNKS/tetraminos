import sys
from getkey import getkey
"""class Tetramino:"""
"""    def __init__(self):
        self.tetraminos = []
        self.grid = []
        self.file_path = """""

file_path = 'carte_1.txt'
def import_card(file_path: str):
    """Permet l’import d’un fichier de jeu. Cette fonction ouvre le fichier, en extrait le contenu et
    le traite de manière a générer les tétraminos définis ainsi que les dimensions du plateau.Return:
    (tuple(x, y), list(tetramino)) → Tuple contenant les dimensions du plateau (sous forme
    d’un tuple (x, y)), ainsi qu’une liste de tetraminos"""
    with open(file_path, 'r') as file:
        lignes = file.readlines()
    dimensions = tuple(map(int, lignes[0].strip().split(',')))
    tetraminos = []
    for line in lignes[1:]:
        data = line.strip().split(';;')
        pos_t = data[0].split(';')
        color = data[1]
        offset = (0, 0) # default value
        tetraminos.append((pos_t, color, offset))
    return dimensions, tetraminos

def create_grid(w, h):
    """Crée une grille de taille (3w+2)×(3h+2) , comprenant les délimitations de la zone centrale."""
    full_w = (3 * w) + 2
    full_h = (3 * h) + 2
    board = []
    for i in range(full_h):
        line = []
        if i < h:
            for j in range(full_w):
                line.append('  ')
            board.append(line)
        elif i == h:
            for l in range(w):
                line.append('  ')
            for k in range(w + 1, 2 * w + 1):
                line.append('--')
            for m in range(2 * w + 1, full_w+1):
                line.append('  ')
            board.append(line)
        elif h < i < 2 * h + 1:
            for j in range(full_w):
                if j == w-1:
                    line.append(' |')
                elif j == 2 * w:
                    line.append('| ')
                else:
                    line.append('  ')
            board.append(line)
        elif i == 2 * h + 1:
            for l in range(w):
                line.append('  ')
            for k in range(w + 1, 2 * w + 1):
                line.append('--')
            for m in range(2 * w + 1, full_w + 1):
                line.append('  ')
            board.append(line)
        elif 2 * h + 1 < i < full_h:
            for j in range(full_w):
                line.append('  ')
            board.append(line)
    return board


grid = create_grid(5, 4)

def print_grid(grid):
    """Affiche la grille de jeu dans la console."""
    for line in grid:
        print(line)


def setup_tetraminos(tetraminos, grid):
    """Mets en place les tétraminos importés depuis le fichier chacun dans leur sous-matrice sur la
matrice principale. Cette fonction est appelée une seule fois en début de jeu pour initialiser la grille de départ.
Return:(list(list), list(tetramino)) → Nouvelle grille avec les tetraminos placés, et la liste de tétraminos avec
leur nouvelle position mise à jour"""
    new_grid = [row[:] for row in grid]  # Copie de la grille pour éviter la modification de la grille originale
    updated_tetraminos = []
    for tetramino in tetraminos:
        coordinates, color = tetramino[:2]  # Récupérer les coordonnées et la couleur

        if len(tetramino) > 2:  # Vérifier s'il y a un décalage
            offset = tetramino[2]
            x_offset, y_offset = offset
        else:
            x_offset, y_offset = 0, 0

        # Placer le tétraminos dans sa sous-matrice respective sur la grille
        for coord in coordinates:
            x, y = coord
            new_grid[x + x_offset][y + y_offset] = color

        # Mettre à jour les coordonnées du tétraminos avec son nouvel emplacement
        updated_coordinates = [(x + x_offset, y + y_offset) for x, y in coordinates]
        updated_tetraminos.append((updated_coordinates, color, offset))

    return new_grid, updated_tetraminos


print(setup_tetraminos(import_card(file_path), grid))




'''

    def setup_tetraminos(tetraminos: list(tetramino), grid: list(list)):

    def place_tetraminos(tetraminos: list(tetramino), grid: list(list)):

    def rotate_tetramino(tetramino: tetramino, clockwise: bool (default=True)):

    def check_move(tetramino: tetramino, grid: list(list)):

    def  check_win(grid: list(list)):'''



