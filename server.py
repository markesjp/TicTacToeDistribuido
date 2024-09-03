import socket

def create_board():
    return [' ' for _ in range(9)]

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def server_program():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    conn1, address1 = server_socket.accept()
    conn2, address2 = server_socket.accept()

    try:
        conn1.send("Welcome Player 1! You are X".encode())
        conn2.send("Welcome Player 2! You are O".encode())

        board = create_board()
        turn = 0  # Player 1 starts

        while True:
            current_player = conn1 if turn % 2 == 0 else conn2
            other_player = conn2 if turn % 2 == 0 else conn1
            player_mark = 'X' if turn % 2 == 0 else 'O'

            data = current_player.recv(1024).decode()
            if data.isdigit() and 0 <= int(data) < 9:
                position = int(data)
                if board[position] == ' ':
                    board[position] = player_mark
                    board_state = f"move {position} {player_mark}"
                    current_player.send(board_state.encode())
                    other_player.send(board_state.encode())
                    if check_winner(board, player_mark):
                        current_player.send("You win!".encode())
                        other_player.send("You lose!".encode())
                        break
                    elif ' ' not in board:
                        current_player.send("It's a draw!".encode())
                        other_player.send("It's a draw!".encode())
                        break
                    turn += 1
                else:
                    current_player.send("Invalid move, try again".encode())
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn1.close()
        conn2.close()

if __name__ == '__main__':
    server_program()
