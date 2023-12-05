
"""class Tetramino:"""
"""    def __init__(self):
        self.tetraminos = []
        self.grid = []
        self.file_path = """""

def import_card(file_path: str):
    """Permet l’import d’un fichier de jeu. Cette fonction ouvre le fichier, en extrait le contenu et
le traite de manière a générer les tétraminos définis ainsi que les dimensions du plateau."""



def create_grid(w, h):
    """Crée une grille de taille (3w+2)×(3h+2) , comprenant les délimitations de la zone centrale."""
    global board
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
for line in grid:
    print(line)













'''

    def setup_tetraminos(self, tetraminos: list(tetramino), grid: list(list)):

    def place_tetraminos(self, tetraminos: list(tetramino), grid: list(list)):

    def rotate_tetramino(self, tetramino: tetramino, clockwise: bool (default=True)):

    def check_move(self, tetramino: tetramino, grid: list(list)):

    def  check_win(self, grid: list(list)):'''



