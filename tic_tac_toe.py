from tkinter import ttk
import tkinter as tk
from windows import set_dpi_awareness
import tkinter.font as font
from random import *
set_dpi_awareness()

# can Associative rule learning can be used in this case to learn better with each game?
class main_frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic tac toe')
        self.geometry('600x600')
        self.resizable(False,False)
        self.player_tiles=[]
        self.computer_tiles=[1,9,8]
        self.used_tiles=[]
        self.winner=tk.StringVar()
        self.player_choice=tk.IntVar()
        self.available_tiles=[1,2,3,4,5,6,7,8,9]
        self.player_score = tk.IntVar(value=0)
        self.computer_score = tk.IntVar(value=0)
        self.label_player = ttk.Label(self, text=f'Player: {self.player_score.get()}', font=('Helvetica', 20))
        self.label_computer = ttk.Label(self, text=f'Computer: {self.computer_score.get()}', font=('Helvetica', 20))
        self.label_player.grid(row=0, column=0, padx=(20, 10), pady=(10, 20))
        self.label_computer.grid(row=0, column=1, padx=(10, 0), pady=(10, 20))
        self.btn1=tk.Button(self,width=25,height=10,command=self.button1)
        self.btn1.grid(row=1,column=0,padx=(23,0))
        self.btn2 = tk.Button(self, width=25, height=10,command=self.button2)
        self.btn2.grid(row=1, column=1)
        self.btn3 = tk.Button(self, width=25, height=10,command=self.button3)
        self.btn3.grid(row=1, column=2)
        self.btn4 = tk.Button(self, width=25, height=10,command=self.button4)
        self.btn4.grid(row=2, column=0,padx=(23,0))
        self.btn5 = tk.Button(self, width=25, height=10,command=self.button5)
        self.btn5.grid(row=2, column=1)
        self.btn6 = tk.Button(self, width=25, height=10,command=self.button6)
        self.btn6.grid(row=2, column=2)
        self.btn7 = tk.Button(self, width=25, height=10, command=self.button7)
        self.btn7.grid(row=3, column=0, padx=(23, 0))
        self.btn8 = tk.Button(self, width=25, height=10, command=self.button8)
        self.btn8.grid(row=3, column=1)
        self.btn9 = tk.Button(self, width=25, height=10, command=self.button9)
        self.btn9.grid(row=3, column=2)
        self.window_win_status=0 #close
        self.window_lost_status = 0  # close
        self.window_draw_status = 0  # close
        print("These are the style classes:")




    def set_values(self):

        self.label_player.config(text=f'Player: {self.player_score.get()}')
        self.select_winner()
        self.set_btn_state()
        if self.winner.get() == 'Player':
            self.win_window()

        elif self.winner.get() == 'Computer':
            self.lost_window()
        elif self.winner.get() == 'Draw':
            self.draw_window()


    def computer_choice(self):
        self.computer_score.set(self.computer_score.get()+1)
        self.label_computer.config(text=f'Computer: {self.computer_score.get()}')
        shuffle(self.available_tiles)
        val = self.available_tiles[randint(0,len(self.available_tiles)-1)]
        self.computer_tiles.append(val)
        self.used_tiles.append(val)
        self.available_tiles.remove(val)
        if val ==1:
            self.btn1.config(text='0')
        elif val ==2:
            self.btn2.config(text='0')
        elif val ==3:
            self.btn3.config(text='0')
        elif val ==4:
            self.btn4.config(text='0')
        elif val ==5:
            self.btn5.config(text='0')
        elif val ==6:
            self.btn6.config(text='0')
        elif val ==7:
            self.btn7.config(text='0')
        elif val ==8:
            self.btn8.config(text='0')
        elif val ==9:
            self.btn9.config(text='0')
        print(val)
        print(f'availableTiles{self.available_tiles}')
        print(f'used tiles {self.used_tiles}')










    def set_btn_state(self):
        for val in self.used_tiles:
            if val == 1:
                self.btn1.config(state='disabled')
            elif val == 2:
                self.btn2.config(state='disabled')
            elif val == 3:
                self.btn3.config(state='disabled')
            elif val == 4:
                self.btn4.config(state='disabled')
            elif val == 5:
                self.btn5.config(state='disabled')
            elif val == 6:
                self.btn6.config(state='disabled')
            elif val == 7:
                self.btn7.config(state='disabled')
            elif val == 8:
                self.btn8.config(state='disabled')
            elif val == 9:
                self.btn9.config(state='disabled')





    def select_winner(self):
        if self.player_score.get() == 3 and self.computer_score.get() == 3:

            a = self.player_tiles[0]
            b = self.player_tiles[1]
            c = self.player_tiles[2]
            d = self.computer_tiles[0]
            f = self.computer_tiles[1]
            e = self.computer_tiles[2]


            # in all these scenarios player wins
            if a in [1,5,9] and b in [1,5,9] and c in [1,5,9]:
                self.winner.set('Player')
            elif a in [1,2,3] and b in [1,2,3] and c in [1,2,3]:
                self.winner.set('Player')
            elif a in [4,5,6] and b in [4,5,6] and c in [4,5,6]:
                self.winner.set('Player')
            elif a in [7,8,9] and b in [7,8,9] and c in [7,8,9]:
                self.winner.set('Player')
            elif a in [1,4,7] and b in [1,4,7] and c in [1,4,7]:
                self.winner.set('Player')
            elif a in [2,5,8] and b in [2,5,8] and c in [2,5,8]:
                self.winner.set('Player')
            elif a in [3,6,9] and b in [3,6,9] and c in [3,6,9]:
                self.winner.set('Player')
            elif a in [7,5,3] and b in [7,5,3] and c in [7,5,3]:
                self.winner.set('Player')
              # in all these scenarios computer wins
            elif d in [1,5,9] and e in [1,5,9] and f in [1,5,9]:
                self.winner.set('Computer')
            elif d in [1,2,3] and e in [1,2,3] and f in [1,2,3]:
                self.winner.set('Computer')
            elif d in [4,5,6] and e in [4,5,6] and f in [4,5,6]:
                self.winner.set('Computer')
            elif d in [7,8,9] and e in [7,8,9] and f in [7,8,9]:
                self.winner.set('Computer')
            elif d in [1,4,7] and e in [1,4,7] and f in [1,4,7]:
                self.winner.set('Computer')
            elif d in [2,5,8] and e in [2,5,8] and f in [2,5,8]:
                self.winner.set('Computer')
            elif d in [3,6,9] and e in [3,6,9] and f in [3,6,9]:
                self.winner.set('Computer')
            elif d in [7,5,3] and e in [7,5,3] and f in [7,5,3]:
                self.winner.set('Computer')
            # in all other conditions it's a draw
            else:
                self.winner.set('Draw')






    def button1(self):
        self.player_choice.set(1)
        self.btn1.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(1)
        self.used_tiles.append(1)
        self.available_tiles.remove(1)
        self.computer_choice()
        self.set_values()


    def button2(self):
        self.player_choice.set(2)
        self.btn2.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(2)
        self.used_tiles.append(2)
        self.available_tiles.remove(2)
        self.computer_choice()
        self.set_values()

    def button3(self):
        self.player_choice.set(3)
        self.btn3.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(3)
        self.used_tiles.append(3)
        self.available_tiles.remove(3)
        self.computer_choice()
        self.set_values()

    def button4(self):
        self.player_choice.set(4)
        self.btn4.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(4)
        self.used_tiles.append(4)
        self.available_tiles.remove(4)
        self.computer_choice()
        self.set_values()

    def button5(self):
        self.player_choice.set(5)
        self.btn5.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(5)
        self.used_tiles.append(5)
        self.available_tiles.remove(5)
        self.computer_choice()
        self.set_values()

    def button6(self):
        self.player_choice.set(6)
        self.btn6.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(6)
        self.used_tiles.append(6)
        self.available_tiles.remove(6)
        self.computer_choice()
        self.set_values()

    def button7(self):
        self.player_choice.set(4)
        self.btn7.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(7)
        self.used_tiles.append(7)
        self.available_tiles.remove(7)
        self.computer_choice()
        self.set_values()

    def button8(self):
        self.player_choice.set(5)
        self.btn8.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(8)
        self.used_tiles.append(8)
        self.available_tiles.remove(8)
        self.computer_choice()
        self.set_values()

    def button9(self):
        self.player_choice.set(6)
        self.btn9.config(text='X')
        self.player_score.set(self.player_score.get() + 1)
        self.player_tiles.append(9)
        self.used_tiles.append(9)
        self.available_tiles.remove(9)
        self.computer_choice()
        self.set_values()

    def win_window(self):
        self.window_win_status=1 #active
        self.window_win = tk.Toplevel()
        self.window_win.geometry('200x100')
        self.window_win.title('You won no fuck off!')
        self.window_win.resizable(False, False)
        label=tk.Label(self.window_win,text='You won now fuck off!',font=('Helvetica',15))
        label.pack()
        button=tk.Button(self.window_win,text='Play again',command=self.reset)
        button.pack(pady=10)
    def lost_window(self):
        self.window_lost_status=1 #active
        self.window_lost = tk.Toplevel()
        self.window_lost.geometry('200x100')
        self.window_lost.title('You won no fuck off!')
        self.window_lost.resizable(False, False)
        label = tk.Label(self.window_lost, text='You lost now fuck off!', font=('Helvetica', 15))
        label.pack()
        button = tk.Button(self.window_lost, text='Play again', command=self.reset)
        button.pack(pady=10)
    def draw_window(self):
        self.window_draw_status=1 #active
        self.window_draw = tk.Toplevel()
        self.window_draw.geometry('200x100')
        self.window_draw.title('You won no fuck off!')
        self.window_draw.resizable(False,False)
        label = tk.Label(self.window_draw, text="It's a draw now fuck off!", font=('Helvetica', 10))
        label.pack()
        button = tk.Button(self.window_draw, text='Play again', command=self.reset)
        button.pack(pady=10)

    def reset(self):
        self.player_score.set(0)
        self.label_player.config(text=f'Player: {self.player_score.get()}')
        self.computer_score.set(0)
        self.label_computer.config(text=f'Player: {self.computer_score.get()}')
        self.btn1.config(text='')
        self.btn2.config(text='')
        self.btn3.config(text='')
        self.btn4.config(text='')
        self.btn5.config(text='')
        self.btn6.config(text='')
        self.btn7.config(text='')
        self.btn8.config(text='')
        self.btn9.config(text='')
        self.player_tiles=[]
        self.used_tiles=[]
        self.computer_tiles=[]
        self.available_tiles=[1,2,3,4,5,6,7,8,9]
        self.winner.set('')
        self.btn1['state'] = 'normal'
        self.btn2['state'] = 'normal'
        self.btn3['state'] = 'normal'
        self.btn4['state'] = 'normal'
        self.btn5['state'] = 'normal'
        self.btn6['state'] = 'normal'
        self.btn7['state'] = 'normal'
        self.btn8['state'] = 'normal'
        self.btn9['state'] = 'normal'

        if self.window_win_status == 1:
            self.window_win_status = 0
            self.window_win.destroy()
        if self.window_lost_status == 1:
            self.window_lost_status = 0
            self.window_lost.destroy()
        if self.window_draw_status == 1:
            self.window_draw_status = 0
            self.window_draw.destroy()



    # close the side menus as well in this function






root=main_frame()
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("clam"))

root.mainloop()