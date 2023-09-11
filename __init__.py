from tkinter import *
from random import randint
import time

global number_tour
number_tour = 9
global tour
tour = 0
#variable pour la fontion contre playeur 2
global button1_var_player
button1_var_player = "rien1"
global button2_var_player
button2_var_player = "rien2"
global button3_var_player
button3_var_player = "rien3"
global button4_var_player
button4_var_player = "rien4"
global button5_var_player
button5_var_player = "rien5"
global button6_var_player
button6_var_player = "rien6"
global button7_var_player
button7_var_player = "rien7"
global button8_var_player
button8_var_player = "rien8"
global button9_var_player
button9_var_player = "rien9"

#variable pour player pour savoir si button est deja activer ou non
global button1_infos_player
button1_infos_player = "non"
global button2_infos_player
button2_infos_player = "non"
global button3_infos_player
button3_infos_player = "non"
global button4_infos_player
button4_infos_player = "non"
global button5_infos_player
button5_infos_player = "non"
global button6_infos_player
button6_infos_player = "non"
global button7_infos_player
button7_infos_player = "non"
global button8_infos_player
button8_infos_player = "non"
global button9_infos_player
button9_infos_player = "non"

#variable pour la fonction contre l'ordi
global button1_var_ordi
button1_var_ordi = "rien1"
global button2_var_ordi
button2_var_ordi = "rien2"
global button3_var_ordi
button3_var_ordi = "rien3"
global button4_var_ordi
button4_var_ordi = "rien4"
global button5_var_ordi
button5_var_ordi = "rien5"
global button6_var_ordi
button6_var_ordi = "rien6"
global button7_var_ordi
button7_var_ordi = "rien7"
global button8_var_ordi
button8_var_ordi = "rien8"
global button9_var_ordi
button9_var_ordi = "rien9"

#variable pour ordi pour savoir si button est deja activer ou non
global button1_infos_ordi
button1_infos_ordi = "non"
global button2_infos_ordi
button2_infos_ordi = "non"
global button3_infos_ordi
button3_infos_ordi = "non"
global button4_infos_ordi
button4_infos_ordi = "non"
global button5_infos_ordi
button5_infos_ordi = "non"
global button6_infos_ordi
button6_infos_ordi = "non"
global button7_infos_ordi
button7_infos_ordi = "non"
global button8_infos_ordi
button8_infos_ordi = "non"
global button9_infos_ordi
button9_infos_ordi = "non"


def mainmenu():
    def player():
        def def_button1_player():
            global button1_infos_player
            global button1_var_player
            nonlocal role
            if button1_infos_player == "non":
                if role == 1:
                    button_player.config(text="x")
                    role = 2
                    button1_var_player = "x"
                    button1_infos_player = "oui"
                elif role == 2:
                    button_player.config(text="o")
                    role = 1
                    button1_var_player = "o"
                    button1_infos_player = "oui"
            elif button1_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()


        def def_button2_player():
            global button2_infos_player
            global button2_var_player
            nonlocal role
            if button2_infos_player == "non":
                if role == 1:
                    button2_player.config(text="x")
                    role = 2
                    button2_var_player = "x"
                    button2_infos_player = "oui"
                elif role == 2:
                    button2_player.config(text="o")
                    role = 1
                    button2_var_player = "o"
                    button2_infos_player = "oui"
            elif button2_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()


        def def_button3_player():
            global button3_infos_player
            global button3_var_player
            nonlocal role
            if button3_infos_player == "non":
                if role == 1:
                    button3_player.config(text="x")
                    role = 2
                    button3_var_player = "x"
                    button3_infos_player = "oui"
                elif role == 2:
                    button3_player.config(text="o")
                    role = 1
                    button3_var_player = "o"
                    button3_infos_player = "oui"
            elif button3_infos_player == "oui ":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button4_player():
            global button4_infos_player
            global button4_var_player
            nonlocal role
            if button4_infos_player == "non":
                if role == 1:
                    button4_player.config(text="x")
                    role = 2
                    button4_var_player = "x"
                    button4_infos_player = "oui"
                elif role == 2:
                    button4_player.config(text="o")
                    role = 1
                    button4_var_player = "o"
                    button4_infos_player = "oui"
            elif button4_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button5_player():
            global button5_infos_player
            global button5_var_player
            nonlocal role
            if button5_infos_player == "non":
                if role == 1:
                    button5_player.config(text="x")
                    role = 2
                    button5_var_player = "x"
                    button5_infos_player = "oui"
                elif role == 2:
                    button5_player.config(text="o")
                    role = 1
                    button5_var_player = "o"
                    button5_infos_player = "oui"
            elif button5_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button6_player():
            global button6_infos_player
            global button6_var_player
            nonlocal role
            if button6_infos_player == "non":
                if role == 1:
                    button6_player.config(text="x")
                    role = 2
                    button6_var_player = "x"
                    button6_infos_player = "oui"
                elif role == 2:
                    button6_player.config(text="o")
                    role = 1
                    button6_var_player = "o"
                    button6_infos_player = "oui"
            elif button6_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button7_player():
            global button7_infos_player
            global button7_var_player
            nonlocal role
            if button7_infos_player == "non":
                if role == 1:
                    button7_player.config(text="x")
                    role = 2
                    button7_var_player = "x"
                    button7_infos_player = "oui"
                elif role == 2:
                    button7_player.config(text="o")
                    role = 1
                    button7_var_player = "o"
                    button7_infos_player = "oui"
            elif button7_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button8_player():
            global button8_infos_player
            global button8_var_player
            nonlocal role
            if button8_infos_player == "non":
                if role == 1:
                    button8_player.config(text="x")
                    role = 2
                    button8_var_player = "x"
                    button8_infos_player = "oui"
                elif role == 2:
                    button8_player.config(text="o")
                    role = 1
                    button8_var_player = "o"
                    button8_infos_player = "oui"
            elif button8_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button9_player():
            global button9_infos_player
            global button9_var_player
            nonlocal role
            if button9_infos_player == "non":
                if role == 1:
                    button9_player.config(text="x")
                    role = 2
                    button9_var_player = "x"
                    button9_infos_player = "oui"
                elif role == 2:
                    button9_player.config(text="o")
                    role = 1
                    button9_var_player = "o"
                    button9_infos_player = "oui"
            elif button9_infos_player == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def calcul():
            finish = False
            global button1_var_player
            global button2_var_player
            global button3_var_player
            global button4_var_player
            global button5_var_player
            global button6_var_player
            global button7_var_player
            global button8_var_player
            global button9_var_player

            if button1_var_player == button2_var_player:
                if button2_var_player == button3_var_player:
                    text1 = ("le joueur '" + button1_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text1)
                    finish = True

            if button4_var_player == button5_var_player:
                if button5_var_player == button6_var_player:
                    text2 = ("le joueur '" + button4_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text2)
                    finish = True

            if button7_var_player == button8_var_player:
                if button8_var_player == button9_var_player:
                    text3 = ("le joueur '" + button7_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text3)
                    finish = True

            if button1_var_player == button4_var_player:
                if button4_var_player == button7_var_player:
                    text4 = ("le joueur '" + button1_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button2_var_player == button5_var_player:
                if button5_var_player == button8_var_player:
                    text4 = ("le joueur '" + button2_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button3_var_player == button6_var_player:
                if button6_var_player == button9_var_player:
                    text4 = ("le joueur '" + button3_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button1_var_player == button5_var_player:
                if button5_var_player == button9_var_player:
                    text4 = ("le joueur '" + button1_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button7_var_player == button5_var_player:
                if button5_var_player == button3_var_player:
                    text4 = ("le joueur '" + button7_var_player + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if finish == True:
                finish_wind()


        def finish_wind():
            FINISH_wind = Tk()
            FINISH_wind.title("fin du jeux, merci d'y avoir jouer")
            FINISH_wind.minsize(840, 460)
            FINISH_wind.config(background="black")

            merci = Label(FINISH_wind,text="Merci d'avoir jouer a mon tictactoe cela me fait très plaisir,\njespère qu'il aurra été sujet d'un réel amusemant pour vous.\nMerci encore :)",fg="white" ,bg="black")
            merci.pack(expand=YES)

            FINISH_wind.mainloop()

        def mmainmenu():
            mainmenu.geometry('800x480')
            mainmenu.minsize(800, 480)
            player_window.destroy()


        def destroy():
            mainmenu.destroy()
            player_window.destroy()



        player_window = Tk()

        mainmenu.minsize(0, 0)
        mainmenu.maxsize(0, 0)
        mainmenu.geometry("0x0")

        player_window.title('tictactoe contre player2')
        player_window.geometry('800x480')
        player_window.minsize(800, 480)
        player_window.maxsize(800, 480)
        player_window.config(background='black')

        frame_main = Frame(player_window, bd=0, bg='black')
        frame_left = Frame(frame_main, bd=0, bg='black')
        frame_right = Frame(frame_main, bd=0, bg='black')
        frame_center = Frame(frame_main, bd=0, bg='black')
        retourn = Frame(player_window, bd=0, bg='black')

        affichage = Entry(player_window, bg='white', width=30, fg='black')
        affichage.pack(side=TOP)

        affichage.delete(0, END)
        affichage.insert(0, texte)

        stop = Button(retourn, text="exit", bg='white', fg='black', command= destroy)
        stop.pack(side=TOP)

        back = Button(retourn, text="back to the menu", bg='white', fg='black', command= mmainmenu)
        back.pack(side=BOTTOM)

        button_player = Button(frame_left, text="", bg='white', fg='black', height=4, width=6,font=(6), command= def_button1_player)
        button_player.pack()

        button2_player = Button(frame_left, bg='white', fg='black', height=4, width=6,font=(6), command= def_button2_player)
        button2_player.pack()

        button3_player = Button(frame_left, bg='white', fg='black', height=4, width=6,font=(6), command= def_button3_player)
        button3_player.pack()

        button4_player = Button(frame_center, bg='white', fg='black', height=4, width=6,font=(6), command= def_button4_player)
        button4_player.pack()

        button5_player = Button(frame_center, bg='white', fg='black', height=4, width=6,font=(6), command= def_button5_player)
        button5_player.pack()

        button6_player = Button(frame_center, bg='white', fg='black', height=4, width=6,font=(6), command= def_button6_player)
        button6_player.pack()

        button7_player = Button(frame_right, bg='white', fg='black', height=4, width=6,font=(6), command= def_button7_player)
        button7_player.pack()

        button8_player = Button(frame_right, bg='white', fg='black', height=4, width=6,font=(6), command= def_button8_player)
        button8_player.pack()

        button9_player = Button(frame_right, bg='white', fg='black', height=4, width=6,font=(6), command= def_button9_player)
        button9_player.pack()

        frame_left.pack(side=LEFT)
        frame_right.pack(side=RIGHT)
        frame_center.pack()
        frame_main.pack(expand=YES)
        retourn.pack(side=BOTTOM)


    def ordi():
        def def_button1_ordi():
            global tour
            global number_tour
            global button1_infos_ordi
            global button1_var_ordi
            if button1_infos_ordi == "non":
                button1.config(text="o")
                button1_var_ordi = "o"
                button1_infos_ordi = "oui"
                tour += 1
            elif button1_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button2_ordi():
            global tour
            global number_tour
            global button2_infos_ordi
            global button2_var_ordi
            if button2_infos_ordi == "non":
                button2.config(text="o")
                button2_var_ordi = "o"
                button2_infos_ordi = "oui"
                tour += 1
            elif button2_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button3_ordi():
            global tour
            global number_tour
            global button3_infos_ordi
            global button3_var_ordi
            if button3_infos_ordi == "non":
                button3.config(text="o")
                button3_var_ordi = "o"
                button3_infos_ordi = "oui"
                tour += 1
            elif button3_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button4_ordi():
            global tour
            global number_tour
            global button4_infos_ordi
            global button4_var_ordi
            if button4_infos_ordi == "non":
                button4.config(text="o")
                button4_var_ordi = "o"
                button4_infos_ordi = "oui"
                tour += 1
            elif button4_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button5_ordi():
            global tour
            global number_tour
            global button5_infos_ordi
            global button5_var_ordi
            if button5_infos_ordi == "non":
                button5.config(text="o")
                button5_var_ordi = "o"
                button5_infos_ordi = "oui"
                tour += 1
            elif button5_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button6_ordi():
            global tour
            global number_tour
            global button6_infos_ordi
            global button6_var_ordi
            if button6_infos_ordi == "non":
                button6.config(text="o")
                button6_var_ordi = "o"
                button6_infos_ordi = "oui"
                tour += 1
            elif button6_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button7_ordi():
            global tour
            global number_tour
            global button7_infos_ordi
            global button7_var_ordi
            if button7_infos_ordi == "non":
                button7.config(text="o")
                button7_var_ordi = "o"
                button7_infos_ordi = "oui"
                tour += 1
            elif button7_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button8_ordi():
            global tour
            global number_tour
            global button8_infos_ordi
            global button8_var_ordi
            if button8_infos_ordi == "non":
                button8.config(text="o")
                button8_var_ordi = "o"
                button8_infos_ordi = "oui"
                tour += 1
            elif button8_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")
            calcul()

        def def_button9_ordi():
            global tour
            global number_tour
            global button9_infos_ordi
            global button9_var_ordi
            if button9_infos_ordi == "non":
                button9.config(text="o")
                button9_var_ordi = "o"
                button9_infos_ordi = "oui"
                tour += 1
            elif button9_infos_ordi == "oui":
                affichage.delete(0, END)
                affichage.insert(0, "boutton déjà utiliser")

            calcul()

        def calcul_I_A():
            global tour
            global number_tour
            global number
            number = "false"
            global button1_infos_ordi
            global button2_infos_ordi
            global button3_infos_ordi
            global button4_infos_ordi
            global button5_infos_ordi
            global button6_infos_ordi
            global button7_infos_ordi
            global button8_infos_ordi
            global button9_infos_ordi

            global button1_var_ordi
            global button2_var_ordi
            global button3_var_ordi
            global button4_var_ordi
            global button5_var_ordi
            global button6_var_ordi
            global button7_var_ordi
            global button8_var_ordi
            global button9_var_ordi

            # comme l'ordinateur ne peut pas defendre car il n'y a pas deux o aligner alors on verifie si elle peut gagner
            # on verifier si l'ordinateur peut placer un dernier x pour gagner
            if button3_infos_ordi == "non" and button1_var_ordi == button2_var_ordi and button1_var_ordi == "x":  #x| |
                button3.config(text="x")                                                                          #x| |
                button3_infos_ordi = "oui"                                                                        # | |
                button3_var_ordi = "x"
                number = "true"
                tour += 1

            elif button2_infos_ordi == "non" and button1_var_ordi == button3_var_ordi and button1_var_ordi == "x":  #x| |
                button2.config(text="x")                                                                            # | |
                button2_infos_ordi = "oui"                                                                          #x| |
                button2_var_ordi = "x"
                number = "true"
                tour += 1

            elif button1_infos_ordi == "non" and button2_var_ordi == button3_var_ordi and button2_var_ordi == "x":  # | |
                button1.config(text="x")                                                                            #x| |
                button1_infos_ordi = "oui"                                                                          #x| |
                button1_var_ordi = "x"
                number = "true"
                tour += 1

            elif button6_infos_ordi == "non" and button4_var_ordi == button5_var_ordi and button4_var_ordi == "x":  # |x|
                button6.config(text="x")                                                                            # |x|
                button6_infos_ordi = "oui"                                                                          # | |
                button6_var_ordi = "x"
                number = "true"
                tour += 1

            elif button5_infos_ordi == "non" and button4_var_ordi == button6_var_ordi and button4_var_ordi == "x":  # |x|
                button5.config(text="x")                                                                            # | |
                button5_infos_ordi = "oui"                                                                          # |x|
                button5_var_ordi = "x"
                number = "true"
                tour += 1

            elif button4_infos_ordi == "non" and button5_var_ordi == button6_var_ordi and button5_var_ordi == "x":  # | |
                button4.config(text="x")                                                                            # |x|
                button4_infos_ordi = "oui"                                                                          # |x|
                button4_var_ordi = "x"
                number = "true"
                tour += 1

            elif button9_infos_ordi == "non" and button7_var_ordi == button8_var_ordi and button7_var_ordi == "x":  # | |x
                button9.config(text="x")                                                                            # | |x
                button9_infos_ordi = "oui"                                                                          # | |
                button9_var_ordi = "x"
                number = "true"
                tour += 1

            elif button8_infos_ordi == "non" and button7_var_ordi == button9_var_ordi and button7_var_ordi == "x":  # | |x
                button8.config(text="x")                                                                            # | |
                button8_infos_ordi = "oui"                                                                          # | |x
                button8_var_ordi = "x"
                number = "true"
                tour += 1

            elif button7_infos_ordi == "non" and button8_var_ordi == button9_var_ordi and button8_var_ordi == "x":  # | |
                button7.config(text="x")                                                                            # | |x
                button7_infos_ordi = "oui"                                                                          # | |x
                button7_var_ordi = "x"
                number = "true"
                tour += 1

            elif button7_infos_ordi == "non" and button1_var_ordi == button4_var_ordi and button1_var_ordi == "x":  #x|x|
                button7.config(text="x")                                                                            # | |
                button7_infos_ordi = "oui"                                                                          # | |
                button7_var_ordi = "x"
                number = "true"
                tour += 1

            elif button4_infos_ordi == "non" and button1_var_ordi == button7_var_ordi and button1_var_ordi == "x":  #x| |x
                button4.config(text="x")                                                                            # | |
                button4_infos_ordi = "oui"                                                                          # | |
                button4_var_ordi = "x"
                number = "true"
                tour += 1

            elif button1_infos_ordi == "non" and button4_var_ordi == button7_var_ordi and button4_var_ordi == "x":  # |x|x
                button1.config(text="x")                                                                            # | |
                button1_infos_ordi = "oui"                                                                          # | |
                button1_var_ordi = "x"
                number = "true"
                tour += 1

            elif button8_infos_ordi == "non" and button2_var_ordi == button5_var_ordi and button2_var_ordi == "x":  # | |
                button8.config(text="x")                                                                            #x|x|
                button8_infos_ordi = "oui"                                                                          # | |
                button8_var_ordi = "x"
                number = "true"
                tour += 1

            elif button5_infos_ordi == "non" and button2_var_ordi == button8_var_ordi and button2_var_ordi == "x":  # | |
                button5.config(text="x")                                                                            #x| |x
                button5_infos_ordi = "oui"                                                                          # | |
                button5_var_ordi = "x"
                number = "true"
                tour += 1

            elif button2_infos_ordi == "non" and button5_var_ordi == button8_var_ordi and button5_var_ordi == "x":  # | |
                button2.config(text="x")                                                                            # |x|x
                button2_infos_ordi = "oui"                                                                          # | |
                button2_var_ordi = "x"
                number = "true"
                tour += 1

            elif button9_infos_ordi == "non" and button3_var_ordi == button6_var_ordi and button3_var_ordi == "x":  # | |
                button9.config(text="x")                                                                            # | |
                button9_infos_ordi = "oui"                                                                          #x|x|
                button9_var_ordi = "x"
                number = "true"
                tour += 1

            elif button6_infos_ordi == "non" and button3_var_ordi == button9_var_ordi and button3_var_ordi == "x":  # | |
                button6.config(text="x")                                                                            # | |
                button6_infos_ordi = "oui"                                                                          #x| |x
                button6_var_ordi = "x"
                number = "true"
                tour += 1

            elif button3_infos_ordi == "non" and button6_var_ordi == button9_var_ordi and button6_var_ordi == "x":  # | |
                button3.config(text="x")                                                                            # | |
                button3_infos_ordi = "oui"                                                                          # |x|x
                button3_var_ordi = "x"
                number = "true"
                tour += 1

            elif button9_infos_ordi == "non" and button1_var_ordi == button5_var_ordi and button1_var_ordi == "x":  #x| |
                button9.config(text="x")                                                                            # |x|
                button9_infos_ordi = "oui"                                                                          # | |
                button9_var_ordi = "x"
                number = "true"
                tour += 1

            elif button5_infos_ordi == "non" and button1_var_ordi == button9_var_ordi and button1_var_ordi == "x":  #x| |
                button5.config(text="x")                                                                            # | |
                button5_infos_ordi = "oui"                                                                          # | |x
                button5_var_ordi = "x"
                number = "true"
                tour += 1

            elif button1_infos_ordi == "non" and button5_var_ordi == button9_var_ordi and button5_var_ordi == "x":  # | |
                button1.config(text="x")                                                                            # |x|
                button1_infos_ordi = "oui"                                                                          # | |x
                button1_var_ordi = "x"
                number = "true"
                tour += 1

            elif button3_infos_ordi == "non" and button7_var_ordi == button5_var_ordi and button7_var_ordi == "x":  # | |x
                button3.config(text="x")                                                                            # |x|
                button3_infos_ordi = "oui"                                                                          # | |
                button3_var_ordi = "x"
                number = "true"
                tour += 1

            elif button5_infos_ordi == "non" and button3_var_ordi == button7_var_ordi and button3_var_ordi == "x":  # | |x
                button5.config(text="x")                                                                            # | |
                button5_infos_ordi = "oui"                                                                          #x| |
                button5_var_ordi = "x"
                number = "true"
                tour += 1

            elif button7_infos_ordi == "non" and button3_var_ordi == button5_var_ordi and button3_var_ordi == "x":  # | |
                button7.config(text="x")                                                                            # |x|
                button7_infos_ordi = "oui"                                                                          #x| |
                button7_var_ordi = "x"
                number = "true"
                tour += 1
            else:
                # L'ordinateur va verifier si l'enemi a deux o cote a cote
                if button3_infos_ordi == "non" and button1_var_ordi == button2_var_ordi and button1_var_ordi == "o":  # o| |
                    button3.config(text="x")                                                                          # o| |
                    button3_infos_ordi = "oui"                                                                        #  | |
                    button3_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button2_infos_ordi == "non" and button1_var_ordi == button3_var_ordi and button1_var_ordi == "o":  #o| |
                    button2.config(text="x")                                                                            # | |
                    button2_infos_ordi = "oui"                                                                          #o| |
                    button2_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button1_infos_ordi == "non" and button2_var_ordi == button3_var_ordi and button2_var_ordi == "o":  # | |
                    button1.config(text="x")                                                                            #o| |
                    button1_infos_ordi = "oui"                                                                          #o| |
                    button1_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button6_infos_ordi == "non" and button4_var_ordi == button5_var_ordi and button4_var_ordi == "o":  # |o|
                    button6.config(text="x")                                                                            # |o|
                    button6_infos_ordi = "oui"                                                                          # | |
                    button6_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button5_infos_ordi == "non" and button4_var_ordi == button6_var_ordi and button4_var_ordi == "o":  # |o|
                    button5.config(text="x")                                                                            # | |
                    button5_infos_ordi = "oui"                                                                          # |o|
                    button5_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button4_infos_ordi == "non" and button5_var_ordi == button6_var_ordi and button5_var_ordi == "o":  # | |
                    button4.config(text="x")                                                                            # |o|
                    button4_infos_ordi = "oui"                                                                          # |o|
                    button4_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button9_infos_ordi == "non" and button7_var_ordi == button8_var_ordi and button7_var_ordi == "o":  # | |o
                    button9.config(text="x")                                                                            # | |o
                    button9_infos_ordi = "oui"                                                                          # | |
                    button9_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button8_infos_ordi == "non" and button7_var_ordi == button9_var_ordi and button7_var_ordi == "o":  # | |o
                    button8.config(text="x")                                                                            # | |
                    button8_infos_ordi = "oui"                                                                          # | |o
                    button8_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button7_infos_ordi == "non" and button8_var_ordi == button9_var_ordi and button8_var_ordi == "o":  # | |
                    button7.config(text="x")                                                                            # | |o
                    button7_infos_ordi = "oui"                                                                          # | |o
                    button7_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button7_infos_ordi == "non" and button1_var_ordi == button4_var_ordi and button1_var_ordi == "o":  #o|o|
                    button7.config(text="x")                                                                            # | |
                    button7_infos_ordi = "oui"                                                                          # | |
                    button7_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button4_infos_ordi == "non" and button1_var_ordi == button7_var_ordi and button1_var_ordi == "o":  #o| |o
                    button4.config(text="x")                                                                            # | |
                    button4_infos_ordi = "oui"                                                                          # | |
                    button4_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button1_infos_ordi == "non" and button4_var_ordi == button7_var_ordi and button4_var_ordi == "o":  # |o|o
                    button1.config(text="x")                                                                            # | |
                    button1_infos_ordi = "oui"                                                                          # | |
                    button1_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button8_infos_ordi == "non" and button2_var_ordi == button5_var_ordi and button2_var_ordi == "o":  # | |
                    button8.config(text="x")                                                                            #o|o|
                    button8_infos_ordi = "oui"                                                                          # | |
                    button8_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button5_infos_ordi == "non" and button2_var_ordi == button8_var_ordi and button2_var_ordi == "o":  # | |
                    button5.config(text="x")                                                                            #o| |o
                    button5_infos_ordi = "oui"                                                                          # | |
                    button5_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button2_infos_ordi == "non" and button5_var_ordi == button8_var_ordi and button5_var_ordi == "o":  # | |
                    button2.config(text="x")                                                                            # |o|o
                    button2_infos_ordi = "oui"                                                                          # | |
                    button2_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button9_infos_ordi == "non" and button3_var_ordi == button6_var_ordi and button3_var_ordi == "o":  # | |
                    button9.config(text="x")                                                                            # | |
                    button9_infos_ordi = "oui"                                                                          #o|o|
                    button9_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button6_infos_ordi == "non" and button3_var_ordi == button9_var_ordi and button3_var_ordi == "o":  # | |
                    button6.config(text="x")                                                                            # | |
                    button6_infos_ordi = "oui"                                                                          #o| |o
                    button6_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button3_infos_ordi == "non" and button6_var_ordi == button9_var_ordi and button6_var_ordi == "o":  # | |
                    button3.config(text="x")                                                                            # | |
                    button3_infos_ordi = "oui"                                                                          # |o|o
                    button3_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button9_infos_ordi == "non" and button1_var_ordi == button5_var_ordi and button1_var_ordi == "o":  #o| |
                    button9.config(text="x")                                                                            # |o|
                    button9_infos_ordi = "oui"                                                                          # | |
                    button9_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button5_infos_ordi == "non" and button1_var_ordi == button9_var_ordi and button1_var_ordi == "o":  #o| |
                    button5.config(text="x")                                                                            # | |
                    button5_infos_ordi = "oui"                                                                          # | |o
                    button5_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button1_infos_ordi == "non" and button5_var_ordi == button9_var_ordi and button5_var_ordi == "o":  # | |
                    button1.config(text="x")                                                                            # |o|
                    button1_infos_ordi = "oui"                                                                          # | |o
                    button1_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button3_infos_ordi == "non" and button7_var_ordi == button5_var_ordi and button7_var_ordi == "o":  # | |o
                    button3.config(text="x")                                                                            # |o|
                    button3_infos_ordi = "oui"                                                                          # | |
                    button3_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button5_infos_ordi == "non" and button3_var_ordi == button7_var_ordi and button3_var_ordi == "o":  # | |o
                    button5.config(text="x")                                                                            # | |
                    button5_infos_ordi = "oui"                                                                          #o| |
                    button5_var_ordi = "x"
                    number = "true"
                    tour += 1

                elif button7_infos_ordi == "non" and button3_var_ordi == button5_var_ordi and button3_var_ordi == "o":  # | |
                    button7.config(text="x")                                                                            # |o|
                    button7_infos_ordi = "oui"                                                                          #o| |
                    button7_var_ordi = "x"
                    number = "true"
                    tour += 1



            #si l'IA ne peut ni defendre ni placer un x pour gagner alors elle place un x au hazard dans la grille
            while number == "false" and tour < 9:
                activation_but_IA = randint(1, number_tour)
                if activation_but_IA == 1 and button1_infos_ordi == "non":
                    button1.config(text="x")
                    button1_infos_ordi = "oui"
                    button1_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 2 and button2_infos_ordi == "non":
                    button2.config(text="x")
                    button2_infos_ordi = "oui"
                    button2_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 3 and button3_infos_ordi == "non":
                    button3.config(text="x")
                    button3_infos_ordi = "oui"
                    button3_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 4 and button4_infos_ordi == "non":
                    button4.config(text="x")
                    button4_infos_ordi = "oui"
                    button4_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 5 and button5_infos_ordi == "non":
                    button5.config(text="x")
                    button5_infos_ordi = "oui"
                    button5_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 6 and button6_infos_ordi == "non":
                    button6.config(text="x")
                    button6_infos_ordi = "oui"
                    button6_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 7 and button7_infos_ordi == "non":
                    button7.config(text="x")
                    button7_infos_ordi = "oui"
                    button7_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 8 and button8_infos_ordi == "non":
                    button8.config(text="x")
                    button8_infos_ordi = "oui"
                    button8_var_ordi = "x"
                    number = "true"
                    tour += 1
                elif activation_but_IA == 9 and button9_infos_ordi == "non":
                    button9.config(text="x")
                    button9_infos_ordi = "oui"
                    button9_var_ordi = "x"
                    number = "true"
                    tour += 1
                time.sleep(1)
            calcul2()

        def calcul2():
            finish = False
            global button1_var_ordi
            global button2_var_ordi
            global button3_var_ordi
            global button4_var_ordi
            global button5_var_ordi
            global button6_var_ordi
            global button7_var_ordi
            global button8_var_ordi
            global button9_var_ordi

            if button1_var_ordi == button2_var_ordi:
                if button2_var_ordi == button3_var_ordi:
                    text1 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text1)
                    finish = True

            if button4_var_ordi == button5_var_ordi:
                if button5_var_ordi == button6_var_ordi:
                    text2 = ("le joueur '" + button4_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text2)
                    finish = True

            if button7_var_ordi == button8_var_ordi:
                if button8_var_ordi == button9_var_ordi:
                    text3 = ("le joueur '" + button7_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text3)
                    finish = True

            if button1_var_ordi == button4_var_ordi:
                if button4_var_ordi == button7_var_ordi:
                    text4 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button2_var_ordi == button5_var_ordi:
                if button5_var_ordi == button8_var_ordi:
                    text4 = ("le joueur '" + button2_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button3_var_ordi == button6_var_ordi:
                if button6_var_ordi == button9_var_ordi:
                    text4 = ("le joueur '" + button3_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button1_var_ordi == button5_var_ordi:
                if button5_var_ordi == button9_var_ordi:
                    text4 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button7_var_ordi == button5_var_ordi:
                if button5_var_ordi == button3_var_ordi:
                    text4 = ("le joueur '" + button7_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if finish == True:
                finish_wind()

        def calcul():
            finish = False
            global button1_var_ordi
            global button2_var_ordi
            global button3_var_ordi
            global button4_var_ordi
            global button5_var_ordi
            global button6_var_ordi
            global button7_var_ordi
            global button8_var_ordi
            global button9_var_ordi

            if button1_var_ordi == button2_var_ordi:
                if button2_var_ordi == button3_var_ordi:
                    text1 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text1)
                    finish = True

            if button4_var_ordi == button5_var_ordi:
                if button5_var_ordi == button6_var_ordi:
                    text2 = ("le joueur '" + button4_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text2)
                    finish = True

            if button7_var_ordi == button8_var_ordi:
                if button8_var_ordi == button9_var_ordi:
                    text3 = ("le joueur '" + button7_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text3)
                    finish = True

            if button1_var_ordi == button4_var_ordi:
                if button4_var_ordi == button7_var_ordi:
                    text4 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button2_var_ordi == button5_var_ordi:
                if button5_var_ordi == button8_var_ordi:
                    text4 = ("le joueur '" + button2_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button3_var_ordi == button6_var_ordi:
                if button6_var_ordi == button9_var_ordi:
                    text4 = ("le joueur '" + button3_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button1_var_ordi == button5_var_ordi:
                if button5_var_ordi == button9_var_ordi:
                    text4 = ("le joueur '" + button1_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if button7_var_ordi == button5_var_ordi:
                if button5_var_ordi == button3_var_ordi:
                    text4 = ("le joueur '" + button7_var_ordi + "' à gagner")
                    affichage.delete(0, END)
                    affichage.insert(0, text4)
                    finish = True

            if finish == True:
                finish_wind()
            elif finish == False:
                calcul_I_A()

        def finish_wind():
            FINISH_wind = Tk()
            FINISH_wind.title("fin du jeux, merci d'y avoir jouer")
            FINISH_wind.minsize(840, 460)
            FINISH_wind.config(background="black")

            merci = Label(FINISH_wind,text="Merci d'avoir jouer a mon tictactoe cela me fait très plaisir,\njespère qu'il aurra été sujet d'un réel amusemant pour vous.\nMerci encore :)",fg="white" ,bg="black")
            merci.pack(expand=YES)

            FINISH_wind.mainloop()

        def mmainmenu():
            mainmenu.geometry('800x480')
            mainmenu.minsize(800, 480)
            ordi_window.destroy()

        def destroy():
            mainmenu.destroy()
            ordi_window.destroy()





        ordi_window = Tk()

        mainmenu.minsize(0,0)
        mainmenu.maxsize(0,0)
        mainmenu.geometry("0x0")

        ordi_window.geometry('800x480')
        ordi_window.minsize(800, 480)
        ordi_window.title('tictactoe contre ordi')
        ordi_window.config(background='black')

        frame_main = Frame(ordi_window, bd=0, bg='black')
        frame_left = Frame(frame_main, bd=0, bg='black')
        frame_right = Frame(frame_main, bd=0, bg='black')
        frame_center = Frame(frame_main, bd=0, bg='black')
        retourn = Frame(ordi_window, bd=0, bg='black')

        affichage = Entry(ordi_window, bg='white', fg='black', width=25)
        affichage.pack()

        affichage.delete(0, END)
        affichage.insert(0, "le joueur commence (o)")

        back = Button(retourn, text="back to the menu", bg='white', fg='black', command=mmainmenu)
        back.pack(side=BOTTOM)

        stop = Button(retourn, text="exit", bg='white', fg='black', command=destroy)
        stop.pack(side= TOP)

        button1 = Button(frame_left, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button1_ordi)
        button1.pack()

        button2 = Button(frame_left, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button2_ordi)
        button2.pack()

        button3 = Button(frame_left, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button3_ordi)
        button3.pack()

        button4 = Button(frame_center, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button4_ordi)
        button4.pack()

        button5 = Button(frame_center, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button5_ordi)
        button5.pack()

        button6 = Button(frame_center, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button6_ordi)
        button6.pack()

        button7 = Button(frame_right, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button7_ordi)
        button7.pack()

        button8 = Button(frame_right, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button8_ordi)
        button8.pack()

        button9 = Button(frame_right, text='', bg='white', fg='black', height=4, width=6,font=(6), command=def_button9_ordi)
        button9.pack()

        frame_left.pack(side=LEFT)
        frame_right.pack(side=RIGHT)
        frame_center.pack()
        frame_main.pack(expand=YES)
        retourn.pack(side=BOTTOM)

        ordi_window.mainloop()

    role = randint(1, 2)
    if role == 1:
        texte = ("c'est au joueur 'x' de commencer")
    elif role == 2:
        texte = ("c'est au joueur 'o' de commencer")

    mainmenu = Tk()

    mainmenu.geometry('800x480')
    mainmenu.minsize(800, 480)
    mainmenu.maxsize(800,480)
    mainmenu.title('tictactoe menu principal')
    mainmenu.config(background='black')

    frame = Frame(mainmenu, bg='black', bd=0)

    title = Label(mainmenu, text='Bienvenue à toi!', bg='black', fg='white', font=('Arial', 15))
    title.pack(side=TOP)

    button_P = Button(frame, text='contre player2', bg='white', fg='black', width=12, command= player)
    button_P.pack()

    button_O = Button(frame, text='contre ordi', bg='white', fg='black', width=12, command= ordi)
    button_O.pack()

    frame.pack(expand=YES)

    mainmenu.mainloop()
mainmenu()