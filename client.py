import socket
import tkinter as tk
from tkinter import messagebox
import threading

def client_program():
    def on_button_click(position):
        if not game_over:
            try:
                client_socket.send(str(position).encode())
            except:
                messagebox.showinfo("Game Info", "Connection to the server lost!")
                window.destroy()

    def receive_data():
        while not game_over:
            try:
                data = client_socket.recv(1024).decode()
                if "win" in data or "lose" in data or "draw" in data:
                    messagebox.showinfo("Game Info", data)
                    window.quit()
                elif data.startswith("move"):
                    pos, mark = data.split()[1:3]
                    buttons[int(pos)].config(text=mark, state="disabled")
                    label_status.config(text="Your move" if "Your" in label_status.cget("text") else "Opponent's move")
            except:
                break
        try:
            client_socket.close()
        except:
            pass

    host = '127.0.0.1'
    port = 65432
    client_socket = socket.socket()
    client_socket.connect((host, port))

    window = tk.Tk()
    window.title("Tic Tac Toe Client")
    buttons = []
    game_over = False

    for i in range(9):
        b = tk.Button(window, text=" ", font=('normal', 20), height=3, width=6,
                      command=lambda i=i: on_button_click(i))
        b.grid(row=i//3, column=i%3)
        buttons.append(b)

    label_status = tk.Label(window, text="Waiting for server...", font=('normal', 14))
    label_status.grid(row=3, column=0, columnspan=3)

    threading.Thread(target=receive_data, daemon=True).start()
    window.mainloop()
    game_over = True

if __name__ == '__main__':
    client_program()
