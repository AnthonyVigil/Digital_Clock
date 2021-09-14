from tkinter import Label, Tk
import time
app_window = Tk()   #Initialize Tk
app_window.title("Digital Clock")
app_window.geometry("720x450")      #Size of window
app_window.resizable(1,1)

#Add color, font, font size
text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 180

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

#Calls for the time variable and displays Hours, Minutes, and Seconds.
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
