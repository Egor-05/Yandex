nums = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chess = [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
         ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
         ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
         ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
         ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'],
         ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'],
         ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8'],
         ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']]


def possible_turns(cell):
    ca = []
    c = nums.index(cell[0])
    chi = chess[c].index(cell)
    if chi + 2 <= len(chess[c]) and c + 1 <= len(chess) - 1:
        ca.append(chess[c + 1][chi + 2])
    if 0 <= chi - 2 and 0 <= c - 1:
        ca.append(chess[c - 1][chi - 2])
    if chi + 1 <= len(chess[c]) and c + 2 <= len(chess) - 1:
        ca.append(chess[c + 2][chi + 1])
    if 0 <= chi - 1 and 0 <= c - 2:
        ca.append(chess[c - 2][chi - 1])
    if 0 <= chi - 2 and c + 1 <= len(chess) - 1:
        ca.append(chess[c + 1][chi - 2])
    if chi + 2 <= len(chess[c]) - 1 and 0 <= c - 1:
        ca.append(chess[c - 1][chi + 2])
    if chi + 1 <= len(chess[c]) - 1 and 0 <= c - 2:
        ca.append(chess[c - 2][chi + 1])
    if 0 <= chi - 1 and c + 2 <= len(chess) - 1:
        ca.append(chess[c + 2][chi - 1])
    ca.sort()
    return ca
