from tkinter import *
from pygame import mixer
from PIL import ImageTk,Image
from random import randint
import pyttsx3
mixer.init()


user_count=0
com_count=0

choice = {1:'rock', 2: 'paper', 3: 'scissor'}
def runGame(startWindow):
    mixer.music.stop()
    startWindow.destroy()
    startWindow.quit()

    def win_music():

        mixer.music.load(r'''C:\Users\DELL E6430S\Desktop\winsound.wav''')
        mixer.music.play(1)

    def loss_music():
        mixer.music.load(r'''C:\Users\DELL E6430S\Desktop\loss.wav''')
        mixer.music.play()

    # GUI interface for game**/////////////////********
    root = Tk()
    root.geometry('1200x1100')  # ///size of tkinter window
    root.configure(background='grey10')
    root.title("Let's play Rock Paper Scissor")

#///////////////***voice insruction*******//////////
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say("Let's play the game of rock,paper and scissor")

    engine.runAndWait()
    engine.stop

    expr1 = ""
    expr2=""
    user=""

    expr1 = StringVar()
    expr2=StringVar()
    var1=StringVar()
    var2=StringVar()

    result=StringVar()
    choice = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}


    # driver function for program/////////**////
    def game_fun(user_choice):

        engine = pyttsx3.init()


        global user_count
        global com_count
        global user
        user=user_name.get()


        com_choice = randint(1, 3)




        if (com_choice == user_choice):
            expr1.set(choice[user_choice])
            expr2.set(choice[com_choice])
            result.set("It's a tie ")
            engine.setProperty('rate',100)
            engine.say("its a tie")
            engine.runAndWait()
            engine.stop()
        elif (user_choice == 1 and com_choice == 3):
            expr1.set(choice[user_choice])
            expr2.set(choice[com_choice])
            win_music()
            result.set(f"{user} wins!!!")
            engine.say(f"{user} wins")
            engine.runAndWait()
            engine.stop()

            user_count+=1

        elif (user_choice == 2 and com_choice == 1):
            expr1.set(choice[user_choice])
            expr2.set(choice[com_choice])
            result.set(f"{user} wins!!!")
            win_music()
            engine.say(f"{user} wins")
            engine.runAndWait()
            engine.stop()
            user_count+=1

        elif (user_choice == 3 and com_choice == 2):
            expr1.set(choice[user_choice])
            expr2.set(choice[com_choice])
            result.set(f"{user} wins!!!")
            win_music()
            engine.say(f"{user} wins")
            engine.runAndWait()
            engine.stop()
            user_count += 1



        else:
            expr1.set(choice[user_choice])
            expr2.set(choice[com_choice])
            result.set("Computer wins")
            loss_music()
            engine.say("Computer wins")
            engine.runAndWait()
            engine.stop()
            com_count += 1


        var1.set(str(user_count))
        var2.set(str(com_count))



    #///////****user_details****//////////
    entry_label = Label(root, text='Enter your name :', fg='white', bg='black')
    user_name = Entry(root)
    entry_label.place(x=10, y=10)
    user_name.place(x=120, y=10)
    #//////////**********?????????????????????////

    #/////****///////////////////*****////////
    user_count_label = Label(root, text="User   :",fg="white",bg="black").place(x=900, y=10)
    user_count_entry = Label(root, textvar=var1,fg="white",bg="grey10").place(x=970, y=10)
    com_count_label = Label(root, text="Com  :",fg="white",bg="black").place(x=900, y=30)
    com_count_entry = Label(root, textvar=var2,fg="white",bg="grey10").place(x=970, y=30)

    # ////////////*******IMAGE resizing and widgets******/////////
    rock_image = ImageTk.PhotoImage(
        (Image.open(r'''...\rock.png''')).resize((200, 200), Image.ANTIALIAS))
    b1 = Button(root, image=rock_image, command=lambda: game_fun(1))
    b1.place(x=150, y=100)
    paper_image = ImageTk.PhotoImage(
        (Image.open(r'''C:\Users\DELL E6430S\Desktop\paper.png''')).resize((200, 200), Image.ANTIALIAS))
    b2 = Button(root, image=paper_image, command=lambda: game_fun(2))
    b2.place(x=450, y=100)
    scissor_image = ImageTk.PhotoImage(
        (Image.open(r'''C:\Users\DELL E6430S\Desktop\scissor.png''')).resize((200, 200), Image.ANTIALIAS))
    b3 = Button(root, image=scissor_image, command=lambda: game_fun(3))
    b3.place(x=750, y=100)


    # ////////****////// user and computer choice//////******//////////


    user_result_l=Label(root,text="User:",font="Times 15 bold",fg="white",bg="grey10").place(x=150,y=445)
    com_result_l=Label(root,text="Com:",fg="white",font="Times 15 bold",bg="grey10").place(x=750,y=445)
    user_result = Entry(root,bg="grey30", textvariable=expr1,font="Times 12 bold").place(x=210, y=450)
    com_result=Entry(root,bg="grey30",textvariable=expr2,font="Times 12 bold" ).place(x=800,y=450)
    vs_label=Label(root,text="VS",font="Times 30 bold",bg="grey10",fg="grey").place(x=520,y=440)

    result_label=Label(root,textvariable=result,width =20,font="Times 20 bold",fg="black",bg="grey25").place(x=390,y=550)

    #//////////**************adding instruction for user**********************////////////////
    def instruct():
        engine.say("enter your name and click the button to select your choice ")
        engine.runAndWait()
        engine.say("rock versus paper paper wins")
        engine.runAndWait()
        engine.say("rock versus scissor rock wins ")
        engine.runAndWait()
        engine.say("paper versus scissor scissor wins")
        engine.runAndWait()
        engine.stop()
    instruct_button=Button(root,text="INSTRUCTIONS",font="Times 12 bold",fg="yellow",bg="black",command=instruct).place(x=550,y=640)

    # ////////////******////////destroy window fuction and button///////////////*******//////
    def destroy_win():
        root.destroy()


    destroy_button = Button(root, text="QUIT GAME", font="Times 12 bold",fg="yellow",bg="black",command=destroy_win).place(x=430, y=640)

    root.mainloop()




def startScreen():

    #Plays music for the application
    def playMusic():
        mixer.music.load(r'''C:\Users\DELL E6430S\Desktop\musify.wav''')
        mixer.music.play()

    #Start Window
    startWindow = Tk()
    startWindow.title('[Rock] [Paper] [Scissors]')

    #Imports image as title
    load = Image.open(r'''C:\Users\DELL E6430S\Desktop\rps.png''')
    render = ImageTk.PhotoImage(load)
    img = Label(startWindow, image=render, bd=0).place(x=30, y=0)

    clickToPlay = Button(startWindow, text='Play!', width=8, font='Bizon 20 bold', bg='Black', fg='grey', relief=RIDGE, bd=0, command=lambda:runGame(startWindow))
    clickToPlay.place(x=110, y=250)

    #Credit
    authorName = Label(startWindow, text='Written by : Prashant Saraswat', font='Times 6 bold', bg='Black', fg='Yellow')
    authorName.place(x=2, y=280)

    versionNum = Label(startWindow, text='[V 1.2]', font='Times 6 bold', bg='Black', fg='Red')
    versionNum.place(x=300, y=280)

    #Start Screen Music
    playMusic()

    #Locks window size
    startWindow.maxsize(350, 300)
    startWindow.minsize(350,300)

    #Sets window background to black
    startWindow.config(background='Black')

    startWindow.mainloop()

startScreen()

