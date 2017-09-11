from Tkinter import Tk, Label
import tkFont
import signal

def check():
    root.after(50, check) # 50 stands for 50 ms.

def signal_handler(signal, frame):
    print "Quitting..."
    root.destroy()

if __name__ == '__main__':
    signal.signal(signal.SIGUSR2, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    print "Starting..."

    root = Tk()

    # Add a callback so we can exit from the terminal
    root.after(50, check)

    root.attributes("-fullscreen", True)
    root.configure(background='black')
    time_font = tkFont.Font(family='Helvetica',
                         size=40,
                         weight='bold')
    time_label = Label(root,
                       text="22:22",
                       font=time_font,
                       foreground="white",
                       background="black",
                       height=100,
                       width=150)
    time_label.pack()

    root.mainloop()
