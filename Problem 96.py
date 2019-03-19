"""
Quite proud of this one
Readability may not be the best
"""

def sudo_print(sudo):
    for a in range(9):
        if a% 3 == 0:
            print('')
        print(sudo[a])

def MemeLigne(sudoku, ligne, colonne):
    return sudoku[ligne]

def MemeColonne(sudoku, ligne, colonne):
    return [sudoku[a][colonne] for a in range(len(sudoku))]

def MemeCarré(sudoku, ligne, colonne):
    square = []
    corner = (3*(ligne//3), 3*(colonne//3))
    for a in range(corner[0], corner[0]+3):
        for b in range(corner[1], corner[1]+3):
            square.append(sudoku[a][b])
    return square

blocs = [MemeCarré, MemeColonne, MemeLigne]

def eup_rules(sudoku):
    n = len(sudoku)

    g = [[[True if not sudoku[b][a] else False for c in range(n)] for a in range(n)] for b in range(n)]

    def initialisation(sudoku, grid):
        n = len(sudoku)
        for i in range(n):
            for j in range(n):
                if sudoku[i][j]:
                    continue
                faux = []
                for k in blocs:
                    faux += k(sudoku, i, j)
                fossettes = sorted(set(faux))
                fossettes.remove(0)
                for z in fossettes:
                    grid[i][j][z-1] = False
                for a in range(len(grid[i][j])):
                    if not grid[i][j][a]:
                        continue
                    for k in blocs:
                        for b in k(grid, i, j):
                            if b[a] and b is not grid[i][j]:
                                break
                        else:
                            grid[i][j] = [False for a in range(9)]
                            grid[i][j][a] = True

        return grid

    def assignation(sudoku, g):
        modif = False
        for a in range(n):
            for b in range(n):
                if (g[a][b]).count(True) == 1:
                    sudoku[a][b] = g[a][b].index(True) + 1
                    g[a][b] = [False for e in range(9)]
                    modif = True
        return (sudoku, modif)

    modif = True

    while modif:
        g = initialisation(sudoku, g)
        ass = assignation(sudoku, g)
        sudoku = ass[0]
        modif = ass[1]


    return sudoku

def possibles(sudoku):

    grid = [[[] for a in range(len(sudoku[0]))] for b in range(len(sudoku))]

    for i in range(len(sudoku[0])):
        for j in range(len(sudoku)):
            if sudoku[i][j]:
                possible = {sudoku[i][j]}
            else:
                possible = set(range(1, 10)) - set(MemeCarré(sudoku, i, j)) - set(MemeColonne(sudoku, i, j)) - set(MemeLigne(sudoku, i, j))
            grid[i][j] = possible

    return grid

def valid_input(sudo, a, ligne, colonne):
    return a not in MemeLigne(sudo, ligne, colonne) and a not in MemeColonne(sudo, ligne, colonne) and a not in MemeCarré(sudo, ligne, colonne)

def empty_location(sudo, coords):
    for ligne in range(9):
        for colonne in range(9):
            if sudo[ligne][colonne] == 0:
                coords[0], coords[1] = ligne, colonne
                return True
    return False



def backtrack_solving(sudoku):

    coords = [1, 1]

    if not empty_location(sudoku, coords):
        return True

    ligne = coords[0]
    colonne = coords[1]
        
    for a in range(1, 10):
        if valid_input(sudoku, a, ligne, colonne):

            sudoku[ligne][colonne] = a

            if backtrack_solving(sudoku):
                return True
            
            sudoku[ligne][colonne] = 0
        
    return False

if __name__ == '__main__':

    sudoku_50 = [[0, 0, 0, 0, 0, 3, 0, 1, 7],
                 [0, 1, 5, 0, 0, 9, 0, 0, 8],
                 [0, 6, 0, 0, 0, 0, 0, 0, 0],

                 [1, 0, 0, 0, 0, 7, 0, 0, 0],
                 [0, 0, 9, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 5, 0, 0, 0, 0, 4],

                 [0, 0, 0, 0, 0, 0, 0, 2, 0],
                 [5, 0, 0, 6, 0, 0, 3, 4, 0],
                 [3, 4, 0, 2, 0, 0, 0, 0, 0]]

    sudoku_1 = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
                [9, 0, 0, 3, 0, 5, 0, 0, 1],
                [0, 0, 1, 8, 0, 6, 4, 0, 0],

                [0, 0, 8, 1, 0, 2, 9, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 8],
                [0, 0, 6, 7, 0, 8, 2, 0, 0],

                [0, 0, 2, 6, 0, 9, 5, 0, 0],
                [8, 0, 0, 2, 0, 3, 0, 0, 9],
                [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    """
    backtrack_solving(sudoku_50)

    sudo_print(sudoku_50)
    """
    suds = []

    with open('problem 96.txt') as p:

        lines = p.readlines()

    for line in range(len(lines)):
        if lines[line][0] == 'G':
            suds.append([])
            for a in range(1, 10):

                splitting = list(lines[line+a])
                splitting = [int(e) for e in splitting[:-1]]
                suds[-1].append(splitting)

    suds[-1][-1].append(6)

    def list_of_ints_to_ints(liste):
        liste = [str(a) for a in liste]
        number = ''
        for a in liste:
            number += a
        return int(number)

    solved = []

    for a in suds:
        b = eup_rules(a)
        backtrack_solving(b)
        solved.append(b[0][:3])

    result = []

    for i in solved:
        result.append(list_of_ints_to_ints(i))
        
    print(sum(result))
