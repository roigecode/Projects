import os,sys,time,pyautogui

path = "C:\Program Files\Git\git-bash.exe"
os.startfile(path)

"""
           >> GIT CREDENTIALS AUTO TOOL <<
___________________________________________________

           _______ __  ___         __      
          / ____(_) /_/   | __  __/ /_____ 
         / / __/ / __/ /| |/ / / / __/ __ \
        / /_/ / / /_/ ___ / /_/ / /_/ /_/ /
        \____/_/\__/_/  |_\__,_/\__/\____/ 
                                   
_________________________________________________

                   >> v1.0.0 <<
                 
 · WRITE YOUR CREDENTIALS BELLOW FOR THE LAST TIME ·
     -> CHECK LINES: 27, 28, 83, 89 <-
  
"""

# WRITE YOUR CREDENTIALS HERE AND UNCOMMENT 'gitWriteAutoCredentials()':

GITHUB_USERNAME = 'YOUR_USERNAME'
GITHUB_PASSWORD = 'YOUR_PASSWORD'

def cdFolder(fdirectory):
    pyautogui.write('cd ' + fdirectory)
    pyautogui.press('enter')
    time.sleep(1)
    
def gitPull():
    pyautogui.write('git pull')
    pyautogui.press('enter')
    time.sleep(1)

def gitStatus():
    pyautogui.write('git status')
    pyautogui.press('enter')
    time.sleep(1)

def gitAddAll():
    pyautogui.write('git add .')
    pyautogui.press('enter')
    time.sleep(1)

def gitCommit():
    message = input("Which message of commit:")
    pyautogui.write('git commit -m "{message}"')
    pyautogui.press('enter')
    time.sleep(1)

def gitPush():
    pyautogui.write('git push origin main')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(50, 50, clicks=0)
    time.sleep(0.2)
    pyautogui.click(400, 325, clicks=1)
    time.sleep(1)
    
def gitWriteAutoCredentials():
    pyautogui.write(GITHUB_USERNAME)
    pyautogui.press('tab')
    pyautogui.write(GITHUB_PASSWORD)
    pyautogui.press('enter')
    
def gitStoreCredentialsDay():
    pyautogui.write("git config credential.helper store")
    pyautogui.press('enter')
    pyautogui.write("git config credential.helpter 'cache --timeout=9.776.160.000'")                  
    pyautogui.press('enter')
    time.sleep(1)

def gitClear():
    pyautogui.write('clear')
    pyautogui.press('enter')
    time.sleep(1)

if __name__ == "__main__":
    time.sleep(1)
    # WRITE YOUR FOLDER HERE
    cdFolder('/e/git/Projects')
    gitPull()
    gitStatus()
    gitAddAll()
    gitCommit()
    gitPush()
    # UNCOMMENT LINE BELLOW BEFORE RUNNING THE PROGRAM:
    gitWriteAutoCredentials()
    gitStoreCredentialsDay()
