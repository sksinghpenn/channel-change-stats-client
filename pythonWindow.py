from tkinter import *


#within a window create a frame
class Window(Frame):
    #not passing anything right now    
        
    def __init__(self, master = NONE):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Quit Button")
        #put into the expandable frame
        self.pack(fill=BOTH, expand=1)
        
        quitButton = Button(self, text="Quit", command=self.client_exit)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)        

        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
            
        edit = Menu(menu)    
        edit.add_command(label='Undo')

        menu.add_cascade(label='Edit', menu=edit)
        
        #put it in the upper left of the frame
        #quitButton.place(x=0, y=0)  
        
        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)

        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)
    
       
    def showImg(self):
        load = Image.open('GV50.jpg')
        #render=ImageTk.PhotoImage(load)
        
        #img = Label(self, image=render)
        #img.image=render
        #img.place(x=0,y=0)
        
    def showTxt(self):
        text = Label(self, text = 'Happy 50th!')
        text.pack()
    


    def client_exit(self):
        exit() 
     
 
        
      

#importing from tkinter
root = Tk()


#specify the shape so all fits
root.geometry("400x300")

#create an instance of class Window
app = Window(root)

#generate/initialize window
root.mainloop()







