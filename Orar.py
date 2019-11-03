from selenium import webdriver

import sys, time, threading, os

# Define your process.
def the_process_function():
    chromeDriver = 'C:\\Users\\CalinNUTU\\source\\chromedriver_win32\\chromedriver.exe'
    browser = webdriver.Chrome(chromeDriver)
    browser.maximize_window()
    browser.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vThTUuLTXVjArLiEL5PxLYAmXCfV5HLbxIaPSxbfIiQ9j06AwUNID7Hi2QAgeuDJkoW1MfBLIxpI6-m/pubhtml?gid=294857279&single=true')
    thing_not_complete = False

# Define your animated characters function:
def animated_loading():
    chars =  [    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",] 
       
    for i in range(len(chars)):
        sys.stdout.write('\r'+'loading...'+str(chars[i]) + '...loading')
        time.sleep(.1)
        sys.stdout.flush() 
        os.system('cls')

# define name dan target of your thread
the_process = threading.Thread(name='process', target=the_process_function)

# start the thread
the_process.start()

#while the process is alive, call the animated_loading() function
while the_process.isAlive():
    animated_loading()

print('DONE')
