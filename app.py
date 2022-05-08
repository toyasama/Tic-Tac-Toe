from tkinter import *
import os
from PIL import Image,ImageTk
from tkinter import messagebox

from click import command

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
newPath = os.path.join(fileDirectory, 'img\\TTT.ico')
bart_impath = os.path.join(fileDirectory,'img\\bart.jpg')
bart_mini_impath = os.path.join(fileDirectory,'img\\bart_mini.jpg')
nelson_impath = os.path.join(fileDirectory,'img\\nelson.jpg')
nelson_mini_impath = os.path.join(fileDirectory,'img\\nelson_mini.jpg')

class AppTicTacToe(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tic Tac Toe Game")
        self.geometry("1200x720")
        self.minsize(1200,720)
        self.iconbitmap(newPath)
        self.config(background="#41B77F")
        self.home_page()
        self.player = "X"
        self.end_game = False
        self.cells = "_________"
        self.score_player1 = IntVar(0)
        self.score_player2 = IntVar(0)
        self.player1_name = StringVar()
        self.player2_name = StringVar()
        
        self.winning_bloks = []

#gestion de  l'interface
    #interface d'accueil
    def home_page(self):
        self.home_frame = Frame(self, bg="#41B77F")
        self.home_title = Label(self.home_frame, text="Tic Tac Toe", font=("Courrier",50),bg="#41B77F",foreground="White")
        self.home_title.pack()
        self.home_subtitle = Label(self.home_frame, text="Bienvenue", font=("Courrier",40),bg="#41B77F",foreground="White")
        self.home_subtitle.pack()
        self.home_button = Button(self.home_frame, text="Lancer le jeu", font=("Courrier",15),foreground="#41B77F",bg="White",command=lambda: self.param())
        self.home_button.pack(pady=25)
        self.home_frame.pack(expand=YES)

    #interface intermediaire nom des perso
    def delete_param_page(self):
        self.game_title.pack_forget()
        self.cadre.pack_forget()
        self.intro.pack_forget()

    def param(self):
        self.home_frame.pack_forget()

        self.game_title = Label(self, text="Tic Tac Toe", font=("Courrier",50),bg="#41B77F",foreground="White")
        self.game_title.pack(pady=10,fill=X)

        self.intro = Label(self,text='Entrez le nom de vos personnages', font=("Courrier",30),bg="#41B77F",fg='white')
        self.intro.pack(fill=X,padx=10)


        self.cadre = LabelFrame(self,bg="#41B77F",bd=5,relief=RIDGE,text="Joueurs", font=('Courrier',20),padx=20,pady=10)
        self.cadre.pack(expand=YES)

        self.player1_img = Image.open(bart_mini_impath)
        self.player1_img = ImageTk.PhotoImage(self.player1_img, master = self.cadre)
        canvas = Canvas(self.cadre,width=100, height=100)
        canvas.create_image(0, 0, anchor=NW, image=self.player1_img)
        canvas.grid(row=0,column=0,padx=5,pady=10)

        nom1 = Entry(self.cadre)
        nom1.grid(row=0,column=1,padx=5)

        self.player2_img = Image.open(nelson_mini_impath)
        self.player2_img = ImageTk.PhotoImage(self.player2_img, master = self.cadre)
        canvas = Canvas(self.cadre,width=100, height=100)
        canvas.create_image(0, 0, anchor=NW, image=self.player2_img)
        canvas.grid(row=1,column=0,padx=5,pady=10)

        nom2 = Entry(self.cadre)
        nom2.grid(row=1,column=1,padx=5)

        Button(self.cadre,text="Commencer",font=("courrier",15), relief=GROOVE,command=lambda : self.enter_name(nom1.get(),nom2.get())).grid(row=2,column=0,columnspan=2)

    def enter_name(self,nom1,nom2):

        if (len(nom1) >= 2 and len(nom1) <= 10) and  (len(nom2) >=2 and len(nom2) <= 10) :
            self.player1_name.set(nom1)
            self.player2_name.set(nom2)
            self.game_page()
        else:
            messagebox.showinfo("nom","veuillez entrer un nom entre 2 et 10 caractères")


    def player1(self):
        self.player1_frame = Frame(self.containner,bd=5,bg='red')
        self.player1_frame.grid(row=0,column=0,padx=50)

        self.player1_img = Image.open(bart_impath)
        self.player1_img = ImageTk.PhotoImage(self.player1_img, master = self.player1_frame)
        canvas = Canvas(self.player1_frame,width=250, height=250)
        canvas.create_image(0, 0, anchor=NW, image=self.player1_img)
        canvas.pack(expand=YES,anchor=CENTER)

        self.player1_label = Label(self.player1_frame, textvariable=self.player1_name,font=("Courier", 30)).pack(fill=X,expand=YES,side=BOTTOM)

    def player2(self):
        self.player2_frame = Frame(self.containner,bd=5)
        self.player2_frame.grid(row=0,column=2,padx=50)

        self.player2_img = Image.open(nelson_impath)
        self.player2_img = ImageTk.PhotoImage(self.player2_img, master = self.player1_frame)
        canvas = Canvas(self.player2_frame,width=250, height=250)
        canvas.create_image(0, 0, anchor=NW, image=self.player2_img)
        canvas.pack(expand=YES)

        self.player2_label = Label(self.player2_frame, textvariable=self.player2_name,font=("Courier", 30)).pack(fill=X,expand=YES,side=BOTTOM)
    
    def TTT(self):
        
        self.TTT_frame = Frame(self.containner,bg="black",bd=5,width=500,height=500)
        self.TTT_frame.grid(row=0,column=1)

        self.canv1 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv1.grid(row=0,column=0,padx=5,pady=5)
        self.canv2 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv2.grid(row=0,column=1,padx=5,pady=5)
        self.canv3 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv3.grid(row=0,column=2,padx=5,pady=5)
        self.canv4 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv4.grid(row=1,column=0,padx=5,pady=5)
        self.canv5 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv5.grid(row=1,column=1,padx=5,pady=5)
        self.canv6 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv6.grid(row=1,column=2,padx=5,pady=5)
        self.canv7 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv7.grid(row=2,column=0,padx=5,pady=5)
        self.canv8 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv8.grid(row=2,column=1,padx=5,pady=5)
        self.canv9 = Canvas(self.TTT_frame, height=120, width=140)
        self.canv9.grid(row=2,column=2,padx=5,pady=5)

        self.button_case1 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(1,self.player))
        self.button_case1.grid(row=0,column=0,padx=5,pady=5)
        self.button_case2 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(2,self.player))
        self.button_case2.grid(row=0,column=1,padx=5,pady=5)
        self.button_case3 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(3,self.player))
        self.button_case3.grid(row=0,column=2,padx=5,pady=5)
        self.button_case4 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(4,self.player))
        self.button_case4.grid(row=1,column=0,padx=5,pady=5)
        self.button_case5 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(5,self.player))
        self.button_case5.grid(row=1,column=1,padx=5,pady=5)
        self.button_case6 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(6,self.player))
        self.button_case6.grid(row=1,column=2,padx=5,pady=5)
        self.button_case7 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(7,self.player))
        self.button_case7.grid(row=2,column=0,padx=5,pady=5)
        self.button_case8 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(8,self.player))
        self.button_case8.grid(row=2,column=1,padx=5,pady=5)
        self.button_case9 = Button(self.TTT_frame,width=20,height=8,command=lambda : self.draw(9,self.player))
        self.button_case9.grid(row=2,column=2,padx=5,pady=5)


    def game_page(self):
        self.delete_param_page()

        self.game_title = Label(self, text="Tic Tac Toe", font=("Courrier",50),bg="#41B77F",foreground="White",)
        self.game_title.pack(pady=10,fill=X)

        self.score_board = LabelFrame(self,text='score',bg="#41B77F",bd=1,labelanchor=N,font=(30),relief=RIDGE)
        self.score_board.pack(expand=YES)

        Label(self.score_board,textvariable=self.player1_name, font=("Courrier",30),bg="#41B77F").grid(row = 0, column=0)
        self.score_player1_label = Label(self.score_board,width=3,height=2,textvariable=self.score_player1, font=("Courrier",30),bg="#41B77F").grid(row = 0, column=1)
        Label(self.score_board,text=':', font=("Courrier",30),bg="#41B77F").grid(row = 0, column=2)
        self.score_player1_label = Label(self.score_board,width=3,height=2,textvariable=self.score_player2, font=("Courrier",30),bg="#41B77F").grid(row = 0, column=3)
        Label(self.score_board,textvariable=self.player2_name, font=("Courrier",30),bg="#41B77F").grid(row = 0, column=4)

        self.containner = Frame(self,bg="#41B77F")
        self.containner.pack(expand=YES,anchor=CENTER,fill=Y)
        self.player1()
        self.player2()
        self.TTT()
        


    def draw(self,case,player):
        if case == 1: 
            self.button_case1.grid_remove()
            coordonnee = (1,1)
            if player == 'X' :
                self.canv1.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv1.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv1.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 2 : 
            coordonnee = (1,2)
            self.button_case2.grid_remove()
            if player == 'X' :
                self.canv2.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv2.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv2.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 3: 
            coordonnee = (1,3)
            self.button_case3.grid_remove()
            if player == 'X' :
                self.canv3.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv3.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv3.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 4: 
            self.button_case4.grid_remove()
            coordonnee = (2,1)
            if player == 'X' :
                self.canv4.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv4.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv4.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 5: 
            self.button_case5.grid_remove()
            coordonnee = (2,2)
            if player == 'X' :
                self.canv5.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv5.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv5.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 6: 
            self.button_case6.grid_remove()
            coordonnee = (2,3)
            if player == 'X' :
                self.canv6.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv6.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv6.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)

        elif case == 7: 
            self.button_case7.grid_remove()
            coordonnee = (3,1)
            if player == 'X' :
                self.canv7.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv7.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv7.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)
        elif case == 8: 
            self.button_case8.grid_remove()
            coordonnee = (3,2)
            if player == 'X' :
                self.canv8.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv8.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv8.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)
        elif case == 9:
            self.button_case9.grid_remove() 
            coordonnee = (3,3)
            if player == 'X' :
                self.canv9.create_line(0, 0, 140, 120, fill="black", width=10)
                self.canv9.create_line(0, 120, 140 , 0, fill="black", width=10)
            elif player == 'O' :
                self.canv9.create_oval(10, 10, 130, 110, outline="red", width=10)
            self.game(coordonnee)
       


    def show_winner(self) :
        for val in self.winning_bloks :
            if val == 1 : 
                self.canv1.config(bg="blue")
            elif val == 2 : 
                self.canv2.config(bg="blue")
            elif val == 3 : 
                self.canv3.config(bg="blue")
            elif val == 4 : 
                self.canv4.config(bg="blue")
            elif val == 5 : 
                self.canv5.config(bg="blue")
            elif val == 6 : 
                self.canv6.config(bg="blue")
            elif val == 7 : 
                self.canv7.config(bg="blue")
            elif val == 8 : 
                self.canv8.config(bg="blue")
            elif val == 9 : 
                self.canv9.config(bg="blue")

    def new_game(self):
        self.canv1.delete('all')
        self.canv2.delete('all')
        self.canv3.delete('all')
        self.canv4.delete('all')
        self.canv5.delete('all')
        self.canv6.delete('all')
        self.canv7.delete('all')
        self.canv8.delete('all')
        self.canv9.delete('all')

        self.canv1.config(bg='white')
        self.canv2.config(bg='white')
        self.canv3.config(bg='white')
        self.canv4.config(bg='white')
        self.canv5.config(bg='white')
        self.canv6.config(bg='white')
        self.canv7.config(bg='white')
        self.canv8.config(bg='white')
        self.canv9.config(bg='white')
        self.cells = '_________'
        self.TTT()
    def delete_game_page(self):
        self.containner.pack_forget()
        self.game_title.pack_forget()
        self.score_board.pack_forget()
        self.cells = "_________"
        print("done")


# Gestion du jeu
    def change_score(self,player):
        if player == 'X' : 
            self.score_player1.set(self.score_player1.get()+1)
        else :  self.score_player2.set(self.score_player2.get() + 1) 
        

    def add_coins(self,coord,list_cell):
        if self.player == "X":
            list_cell[int(coord[0])-1][int(coord[1])-1] = "X"
        else :
            list_cell[int(coord[0])-1][int(coord[1])-1] = "O"
        return list_cell

    def new_cells(self,matrix):
        new_cells = ""
        for row in matrix:
            for value in row:
                new_cells+=value
        return new_cells

    def player_state(self,player,cells_list):
        for row in range(3):
            if cells_list[row][0] == player and cells_list[row][1] == player and cells_list[row][2] == player:
                if row == 0 : self.winning_bloks = [1,2,3]
                elif row == 1 : self.winning_bloks = [4,5,6]
                else : self.winning_bloks = [7,8,9]
                return "win"
        
        for column in range(3):
            if cells_list[0][column] == player and cells_list[1][column] == player and cells_list[2][column] == player:
                if column == 0 : self.winning_bloks = [1,4,7]
                elif column == 1 : self.winning_bloks = [2,5,8]
                else : self.winning_bloks = [3,6,9]
                return "win"
        
        if cells_list[0][0] == player and cells_list[1][1] == player and cells_list[2][2] == player:
            self.winning_bloks = [1,5,9]
            return "win"
        
        elif cells_list[0][2] == player and cells_list[1][1] == player and cells_list[2][0] == player:
            self.winning_bloks = [3,5,7]
            return "win"
        
        return "undefine"

    def game_state(self,cells_list):
        X_state = self.player_state("X",cells_list)
        O_state = self.player_state("O",cells_list)

        X_coin = 0
        O_coin = 0
        empty_block = 0
        for row in cells_list:
            for value in row:
                if value == "X" : X_coin += 1
                if value == "O" : O_coin += 1
                if value == "_" : empty_block += 1

        if empty_block == 0 :
            return True
            
        if X_state == "win" : 
            self.show_winner()
            self.change_score('X')
            return True

        elif O_state == "win" : 
            self.show_winner()
            self.change_score('O')
            return True
 
    def change_player(self):
        if self.player == "X":
            self.player2_frame.config(bg="red")
            self.player1_frame.config(bg="white")
            self.player = "O"
        else:
            self.player2_frame.config(bg="white")
            self.player1_frame.config(bg="red")
            self.player = "X"
    def game(self,coord):
        cell_list = [list(self.cells[0:3]),list(self.cells[3:6]),list(self.cells[6:])]
        cell_list = self.add_coins(coord,cell_list)
        self.cells=self.new_cells(cell_list)
        self.end_game = self.game_state(cell_list)
        if self.end_game :
            rep = messagebox.askquestion('Continue', 'Do you want to play a new game?')
            if rep == "yes" : self.new_game()
            else : 
                print("delete")
                self.delete_game_page()
                self.home_page()
        else : self.change_player()

if __name__ == "__main__":
    app = AppTicTacToe()
    app.mainloop()