import tkinter as tk
from random import shuffle
from tkinter import messagebox


class Application(tk.Frame):

    def __init__(self, master=None):
        self.board = list(range(16))
        shuffle(self.board)
        while not self.check_resolution():
            shuffle(self.board)
        self.empty = self.board.index(0)
        super().__init__(master)
        self.grid(sticky='NEWS')
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1, uniform='col')
            self.rowconfigure(i + 1, weight=1, uniform='row')
        self.create_widgets()

    def check_resolution(self):
        inv = 0
        for i in range(16):
            if self.board[i] != 0:
                for j in range(i + 1, 16):
                    if self.board[j] > self.board[i]:
                        inv += 1
        inv += self.board.index(0) // 4 + 1
        if inv % 2 == 0:
            return True
        return False

    def show_board(self):
        s = 0
        for i in self.buttons:
            if self.board[s] == 0:
                s += 1
            i['text'] = self.board[s]
            i.grid(row=s // 4 + 1, column=s % 4, sticky='NEWS')
            i['command'] = lambda param = s: self.move_board(param)
            s += 1

    def check(self, param):
        self.empty = self.board.index(0)
        if self.empty // 4 == param // 4 and (param + 1 == self.empty or param - 1 == self.empty) or \
                self.empty % 4 == param % 4 and (param + 4 == self.empty or param - 4 == self.empty):
            return True
        return False

    def move_board(self, param):
        if self.check(param):
            self.board[self.empty], self.board[param] = self.board[param], self.board[self.empty]
        self.show_board()
        if self.board[0:-1] == list(range(1, 16)):
            tk.messagebox.showinfo(message='Victory')
            self.new_game()

    def new_game(self):
        self.board = list(range(16))
        shuffle(self.board)
        while not self.check_resolution():
            shuffle(self.board)
        self.show_board()

    def create_widgets(self):
        self.new_button = tk.Button(self, text='NEW', command=self.new_game)
        self.new_button.grid(row=0, column=0, columnspan=2, sticky='NEWS', padx=10, pady=10)
        self.quit_button = tk.Button(self, text='QUIT', command=self.quit)
        self.quit_button.grid(row=0, column=2, columnspan=2, sticky='NEWS', padx=10, pady=10)
        self.buttons = list()
        for i in range(len(self.board)):
            if self.board[i] != 0:
                button = tk.Button(self, text=self.board[i])
                button.grid(row=i // 4 + 1, column=i % 4, sticky='NEWS')
                button['command'] = lambda param = i: self.move_board(param)
                self.buttons.append(button)


app = Application()
app.master.title('Sample application')
app.mainloop()
