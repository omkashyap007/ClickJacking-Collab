import pyautogui as pg
# this module helps to automate keyboard and mouse

import time
# import time to delay the process for some time as required . 

def click_jacking() :   
    while True : 
        # this statement ( while True) confirms that the loop will run continously  . 
        
        pg.click((653 , 349))
        # this is a mouse click function which clicks on certain position on  your computer . 
        
        pg.write("Hello World !")
        # this is a keyboard function which types something from your keyboard as required. takes input as a string . 
        
        time.sleep(2)
        # this helps to create a delay in the program . 
        
        pg.click((653 , 399))
        pg.write("Hello World Again!")
        time.sleep(2)
        
        pg.click((653 , 349))
        for i in range(30) :
            pg.press("backspace")
            # this is a keyboard function for pressing some keys in the keyboard . 
        time.sleep(2)
        pg.click((653 , 399))
        for i in range(30) : 
            pg.press("backspace")
            
"""

the input taken inside the pg.click() function is the coordinates of the point where i want to perform the click or some required operation . 

the position on your computer can be easily tracked by the function below .

Do this . 
  firstly comment the click_jacking() function call on the line:  and uncomment the function get_pos() in line: 
  then run the script and immediately place your cursor at point whose position you want . then you will be shown the position .
  then the posistion will be in the format of (x = x_value , y_value) . 
  then replace the coordinates with the coordinates above. 
  
  then uncomment the click_jacking() function and comment the get_pos() function calls . 
  
"""      
def get_pos() : 
    time.sleep(4)
    print(pg.position())
    
# get_pos()
click_jacking()
