# Charles Jazon Y. Dorero
# BS in Information Technology 2nd year-Block 3
# PALSU Integrative Programming & Technologies 1
# Guessing Game - Client

import socket

def main():
    HOST = '127.0.0.1'
    PORT = 7777

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        print(s.recv(1024).decode())

        name = input("Enter your name: ")
        s.send(name.encode())

        difficulty = input("Choose difficulty: Easy, Medium, Hard: ")
        s.send(difficulty.encode())

        while True:
            response = s.recv(1024).decode()
            print(response)
            if "Congratulations" in response:
                break
            guess = input("Enter your guess: ")
            s.send(guess.encode())

        print("Goodbye!")

if __name__ == "__main__":
    main()
