import random
import copy

EMPTY = 0
AI = -1
HUMAN = 1
COLS = 7
ROWS = 6

def create_board():
    return [[EMPTY for _ in range(ROWS)] for _ in range(COLS)]

def print_board(board):
    print("\n")
    for y in reversed(range(ROWS)):
        for x in range(COLS):
            cell = board[x][y]
            if cell == EMPTY:
                print(" . ", end="")
            elif cell == HUMAN:
                print(" 🟡 ", end="")  # Humain = Jaune
            else:
                print(" 🔴 ", end="")  # IA = Rouge
        print()
    print(" " + "  ".join(str(i) for i in range(COLS)))

def get_first_empty_row(col, board):
    for row in range(ROWS):
        if board[col][row] == EMPTY:
            return row
    return -1

def is_full(board):
    return all(get_first_empty_row(col, board) == -1 for col in range(COLS))

def average(values, total):
    return sum(values) / total

def check_win(board, x, y, player):
    directions = [
        (1, 0),   # horizontal
        (0, 1),   # vertical
        (1, 1),   # diagonal /
        (-1, 1),  # diagonal \
    ]
    for dx, dy in directions:
        count = 1
        for dir in [-1, 1]:
            i = 1
            while True:
                nx = x + dx * i * dir
                ny = y + dy * i * dir
                if 0 <= nx < COLS and 0 <= ny < ROWS and board[nx][ny] == player:
                    count += 1
                    i += 1
                else:
                    break
        if count >= 4:
            return True
    return False

def evaluate_moves(board, depth, depth_opponent):
    scores = [0] * COLS
    if depth == 0:
        return scores

    for col in range(COLS):
        row = get_first_empty_row(col, board)
        if row != -1:
            map_copy = copy.deepcopy(board)
            map_copy[col][row] = AI

            if check_win(map_copy, col, row, AI):
                scores[col] = 100
                continue

            lost_moves = COLS
            opponent_scores = [0] * COLS
            for opp_col in range(COLS):
                opp_row = get_first_empty_row(opp_col, map_copy)
                if opp_row != -1:
                    map_copy2 = copy.deepcopy(map_copy)
                    map_copy2[opp_col][opp_row] = HUMAN
                    if check_win(map_copy2, opp_col, opp_row, HUMAN):
                        opponent_scores[opp_col] = -100
                        break
                    else:
                        next_scores = evaluate_moves(map_copy2, depth - 1, depth_opponent - 1)
                        opponent_scores[opp_col] = max(next_scores)
                else:
                    lost_moves -= 1
                    opponent_scores[opp_col] = 1000

            if depth_opponent > 0:
                scores[col] = min(opponent_scores)
            else:
                scores[col] = average(opponent_scores, COLS) - ((1000 / COLS) * (COLS - lost_moves))
        else:
            scores[col] = -1000
    return scores

def ai_choose_move(board, depth_ai=3, depth_opponent=2):
    scores = evaluate_moves(board, depth_ai, depth_opponent)
    max_score = max(scores)
    best_columns = [i for i, s in enumerate(scores) if s == max_score]
    print("Scores IA :", scores)
    return random.choice(best_columns)

# Boucle principale du jeu
def play_game():
    board = create_board()
    print_board(board)

    turn = HUMAN  # Le joueur humain commence

    while True:
        if turn == HUMAN:
            try:
                move = int(input("Votre coup (0-6) : "))
                if move < 0 or move >= COLS:
                    print("Colonne invalide. Réessayez.")
                    continue
                row = get_first_empty_row(move, board)
                if row == -1:
                    print("Colonne pleine. Choisissez une autre.")
                    continue
                board[move][row] = HUMAN
                if check_win(board, move, row, HUMAN):
                    print_board(board)
                    print("Vous avez gagné !")
                    break
            except ValueError:
                print("Entrez un nombre valide.")
                continue
        else:
            print("L'IA réfléchit...")
            move = ai_choose_move(board)
            row = get_first_empty_row(move, board)
            board[move][row] = AI
            if check_win(board, move, row, AI):
                print_board(board)
                print(" L'IA a gagné !")
                break

        print_board(board)
        if is_full(board):
            print("Match nul ! Le plateau est plein.")
            break

        turn = AI if turn == HUMAN else HUMAN

# Lancer le jeu
play_game()


