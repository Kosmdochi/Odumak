#==========================import function======================================================================================================================================================
import tkinter              #import tk interface
import tkinter.font         #import tk interface font
#==========================creat window=========================================================================================================================================================
Odumak_interface = tkinter.Tk() # creat Odumak screen
User_interface = tkinter.Tk()   # creat User interface screen 
Odumak_interface.title("Odumak")                # Odumak screen title
Odumak_interface.geometry("1024x800+800+350")   # Odumak screen size
Odumak_interface.resizable(False , False)       # can not change Odumak screen size+
User_interface.title("Odumak_User")             # User interface screen title
User_interface.geometry("500x800+250+350")      # user interface screen size
User_interface.resizable(False , False)         # can not change user interface size
#=============================font==============================================================================================================================================================
Entry_Input_font=tkinter.font.Font(family="맑은 고딕", size=15)     #font of some Label , Button
Button_font=tkinter.font.Font(family="맑은 고딕", size=13)          #font of some Label , Button
#==========================game Photo===========================================================================================================================================================
Map1=tkinter.PhotoImage(file="Odumak_map1.png")             # Mellan island image
Map2=tkinter.PhotoImage(file="Odumak_map2.png")             # liv after detta image
Odumak_title = tkinter.PhotoImage(file="Odumak_title.png")  # Odmak title image
#==========================creat variable , dic=================================================================================================================================================
#==siganl of image==
Game_Situation = "title"        # Odumak game situation
#==user Data==
User_name = "?"                 # User name
#==========================creat function=======================================================================================================================================================
def Change_map1():                                      #function of change map1
    Game_Photo_Interface.config(image=Map1)                 #screen change to map1
    Game_Map_Place.config(text = "Mellan Island")           #text change to Island
def Change_map2():                                      #function of change map2    
    Game_Photo_Interface.config(image=Map2)                 #screen change to map2 
    Game_Map_Place.config(text = "Liv After Detta")         #text chagne to Detta
def Change_screen():                                    #function of change picture by situation
    global Game_Situation                                   
    if Game_Situation == "title":                           #if situation is title
        Game_Photo_Interface.config(image=Odumak_title)     #screen change to title
#==========================creat Odumak interface===============================================================================================================================================
Game_Text_Massage=tkinter.Label(Odumak_interface,text="game massage!\nand story massage",width=150,height=20,fg="black",relief="groove",bd=3,bg="gray")     #creat Label game_massage 
Game_Manage_Massage=tkinter.Label(Odumak_interface,text="game manager massage!",width=150,height=3,fg="blue",relief="groove",bd=3,bg="gray")                #creat Label game_manage_massage
Game_Map_Place=tkinter.Label(Odumak_interface,text="Mellan Island",width=150,height=3,fg="white",relief="groove",bd=3,bg="gray")                            #creat Label game Map text
Game_Input = tkinter.Entry(Odumak_interface,width=70 ,bd=10,insertwidth = 4,font = Entry_Input_font)                                                        #creat entry bring massage from user
Input_Button = tkinter.Button(Odumak_interface, text = "input" ,overrelief="solid", width=15 , fg="black" ,bg="gray",font = Button_font)                    #creat button input
Game_Photo_Interface=tkinter.Label(Odumak_interface , image=Odumak_title)                                                                                   #creat place fill by game screen
#==========================creat Odumak user interface==========================================================================================================================================
Map1_button = tkinter.Button(User_interface, text= "change Map" ,overrelief="solid", width=15, command=Change_map1,font = Button_font)                      #creat button change map1
Map2_button = tkinter.Button(User_interface, text= "change Map" ,overrelief="solid", width=15, command=Change_map2,font = Button_font)                      #creat button change map2
Situation_screen_button = tkinter.Button(User_interface, text= "change screen" ,overrelief="solid", width=15, command=Change_screen,font = Button_font)     #creat button change screen by situation
User_name_interface1 = tkinter.Label(User_interface,text="name :",width=5,height=2,fg="black",relief="groove",bd=2,bg="white")                              #creat label "name"
User_name_interface2 = tkinter.Label(User_interface,text=User_name,width=15,height=2,fg="black",relief="groove",bd=2,bg="white")                            #creat label user name
#==========================Odumak interface pack================================================================================================================================================
Game_Text_Massage.pack(side = "top" , anchor = "center")                         
Game_Manage_Massage.pack(side = "top" , anchor = "center")
Game_Photo_Interface.pack(side = "top" , anchor = "center")
Game_Map_Place.pack(side = "top" , anchor = "center")
Game_Input.pack(side = "left")
Input_Button.pack(side = "left")
#==========================Odumak user interface pack===========================================================================================================================================
Map1_button.pack(side = "left" , anchor= "n")
Map2_button.pack(side = "left" , anchor= "n")
Situation_screen_button.pack(side = "left", anchor= "n")
User_name_interface1.pack(side = "left", anchor= "n")
User_name_interface2.pack(side = "left", anchor= "n")
#==========================mainloop=============================================================================================================================================================
Odumak_interface.mainloop()
User_interface.mainloop()