import pyautogui
import time
import pyperclip

#v taskbaru: win,proj,explorer,firefox,WA
#v firefoxu: slovenscina.eu do vrha poscrollana prvi tab
#WA: navadn
    
def poslusam():
    oseba=""
    pyautogui.click(170,1050)
    time.sleep(0.2)
    pyautogui.click(150,15)
    time.sleep(0.2)
    pyautogui.click(1380,340)
    time.sleep(10)
    pyautogui.click(1380,340)
    time.sleep(6)
    pyautogui.click(500,730)
    time.sleep(0.2)
    pyautogui.hotkey("ctrlleft", "a")
    pyautogui.hotkey("ctrlleft", "c")
    data=pyperclip.paste()
    seznam_besed=data.split()
    index=0
    while(oseba==""):
        if(seznam_besed[index]=="pokliči"):
            oseba=seznam_besed[index+1]
        else:
            index=index+1
    print("poklical bom: "+oseba)
    return oseba

#170,1050
#150, 15
#1380,340
#400,680



def WA_sporocilo(prejemnik):
    pyautogui.click(220,1050)
    time.sleep(1)
    pyautogui.click(350,70)
    time.sleep(1)
    pyautogui.typewrite(prejemnik)
    time.sleep(1)
    pyautogui.click(430,250)
    time.sleep(1)
    pyautogui.typewrite("Pokliči me, Lp")
    #pyautogui.hotkey("enter")
#WA: 220,1050
#new chat: 350,70
#tipkas
#klik na chat: 430,250
#tipkas
#enter

def WA_klic(prejemnik):
    pyautogui.click(220,1050)
    time.sleep(1)
    pyautogui.click(350,70)
    time.sleep(1)
    pyautogui.typewrite(prejemnik)
    time.sleep(1)
    pyautogui.click(430,250)
    time.sleep(1)
    pyautogui.click(1840,70)
#isto kot sporocilo, da odpre chat
#klic: 1840,70

oseba_glavna=poslusam()
#WA_sporocilo(oseba_glavna)
WA_klic(oseba_glavna)