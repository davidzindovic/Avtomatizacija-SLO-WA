import pyautogui
import time
import pyperclip

#v taskbaru: win,proj,explorer,firefox,WA
#v firefoxu: slovenscina.eu do vrha poscrollana prvi tab
#WA: navadn
    
def snemanje_start_stop1(firefox):
    if firefox==1:
        pyautogui.click(170,1050) #klik na firefox v taskbaru
        time.sleep(0.2)
    pyautogui.click(150,15) # klik na tab v firefoxu
    time.sleep(0.2)
    pyautogui.click(1380,340) #klik na gumb za snemanje

def snemanje_procesiranje1():
    pyautogui.click(150,15)
    time.sleep(0.2)
    pyautogui.click(500,730)
    time.sleep(0.5)
    pyautogui.hotkey("ctrlleft", "a")
    pyautogui.hotkey("ctrlleft", "c")
    data=pyperclip.paste()
    seznam_besed=data.split()
    print(seznam_besed)
    return seznam_besed

#170,1050
#150, 15
#1380,340
#400,680

def snemanje_start_stop2():
    #pyautogui.click(170,1050)
    #time.sleep(0.2)
    pyautogui.click(370,15)
    time.sleep(0.2)
    pyautogui.click(1380,340)

def snemanje_procesiranje2():
    pyautogui.click(370,15)
    time.sleep(0.2)
    pyautogui.click(500,730)
    time.sleep(0.5)
    pyautogui.hotkey("ctrlleft", "a")
    pyautogui.hotkey("ctrlleft", "c")
    data=pyperclip.paste()
    seznam_besed=data.split()
    print(seznam_besed)
    return seznam_besed



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

"""
def komande(seznam_besed[]):
    oseba=""    
    index=0
    while(oseba==""):
        if(seznam_besed[index]=="pokliči"):
            oseba=seznam_besed[index+1]
        else:
            index=index+1
    print("poklical bom: "+oseba)
    return oseba
"""
#oseba_glavna=poslusam()
#WA_sporocilo(oseba_glavna)
#WA_klic(oseba_glavna)

once=0
delay_med_intervali=20
while True:
    if(once==0):
        snemanje_start_stop1(1)
        time.sleep(delay_med_intervali)
        once=1
        snemanje_start_stop1(0)
        snemanje_start_stop2()
    time.sleep(delay_med_intervali)
    snemanje_start_stop2()
    snemanje_procesiranje1()
    snemanje_start_stop1(0)
    time.sleep(delay_med_intervali)
    snemanje_start_stop1(0)
    snemanje_procesiranje2()
    snemanje_start_stop2()
