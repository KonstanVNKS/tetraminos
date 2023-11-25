def create_grid(w: int, h: int):
    """Crée une grille de taille (3w+2)×(3h+2) , comprenant les délimitations de la zone centrale."""
    grid = [['  ' for _ in range(3 * w + 2)] for _ in range(3 * h + 2)]
    return grid

def print_grid(grid: list(list), no_number: bool):
    """Print le plateau de jeu. Pour améliorer la jouabilité, les limites du plateau doivent être
affichées en utilisant les caractères ’|’ (bordures verticales) et (-) (bordures horizontales).
Référez-vous aux figures des sections précédentes pour un exemple (par exemple : Figure 1).
Le paramètre no_number indique si les pièces doivent être affichées avec (si sa valeur est
False) ou sans (si sa valeur est True) les chiffres correspondants.
"""



def import_card(file_path: str):

def setup_tetraminos(tetraminos: list(tetramino), grid: list(list)):

def place_tetraminos(tetraminos: list(tetramino), grid: list(list)):

def rotate_tetramino(tetramino: tetramino, clockwise: bool (default=True)):

def check_move(tetramino: tetramino, grid: list(list)):

def  check_win(grid: list(list)):

def main():






