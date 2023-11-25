
class Tetramino:
    def __init__(self):
        self.tetraminos = []
        self.grid = []
        self.file_path = ""
    def create_grid(self, w: int, h: int):
        """Crée une grille de taille (3w+2)×(3h+2) , comprenant les délimitations de la zone centrale."""
        grid = [['  ' for _ in range(3 * w + 2)] for _ in range(3 * h + 2)]
        for i in range(w + 1, 2 * w + 1):
            grid[h][i] = "--"
        for j in range(h + 1, 2 * h + 1):
            grid[j][w] = "|"
            grid[j][2 * w + 1] = "|"
        return grid

    def print_grid(self, grid: list(list), no_number: bool):
        """Print le plateau de jeu. Pour améliorer la jouabilité, les limites du plateau doivent être
    affichées en utilisant les caractères ’|’ (bordures verticales) et (-) (bordures horizontales).
    Référez-vous aux figures des sections précédentes pour un exemple (par exemple : Figure 1).
    Le paramètre no_number indique si les pièces doivent être affichées avec (si sa valeur est
    False) ou sans (si sa valeur est True) les chiffres correspondants.
    """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end='')
            print()


'''    def import_card(self, file_path: str):

    def setup_tetraminos(self, tetraminos: list(tetramino), grid: list(list)):

    def place_tetraminos(self, tetraminos: list(tetramino), grid: list(list)):

    def rotate_tetramino(self, tetramino: tetramino, clockwise: bool (default=True)):

    def check_move(self, tetramino: tetramino, grid: list(list)):

    def  check_win(self, grid: list(list)):'''

'''def main():
    game = Tetramino()'''




