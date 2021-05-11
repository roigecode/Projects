import os,sys,time,pyautogui

path = "C:\Program Files\Git\git-bash.exe"
os.startfile(path)

def cdFolder(fdirectory):
    pyautogui.write('cd ' + fdirectory)
    pyautogui.press('enter')
    
def gitPull():
    pyautogui.write('git pull')
    pyautogui.press('enter')
    time.sleep(1.5)

def gitStatus():
    pyautogui.write('git status')
    pyautogui.press('enter')
    time.sleep(1)

def gitAddAll():
    pyautogui.write('git add .')
    pyautogui.press('enter')
    time.sleep(1)

def gitCommit():
    pyautogui.write('git commit -m "New Commit"')
    pyautogui.press('enter')
    time.sleep(1)

if __name__ == "__main__":
    time.sleep(1)
    cdFolder('/e/git/Projects')
    gitPull()
    gitStatus()
    gitAddAll()
    gitCommit()