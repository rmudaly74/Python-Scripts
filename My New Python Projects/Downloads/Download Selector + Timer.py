import pyautogui
import time

print("#Download Selector")
time.sleep(1)
print("How many downloads to start? ")
myDownloadCount = int(input())
time.sleep(1)
print("How long until download start ?")
myTimeAmount = int(input())

time.sleep(myTimeAmount)

if myDownloadCount == 1:
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')
    #double click and close vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    pyautogui.alert("Done started 1 download and closed vlc.")

elif myDownloadCount == 2:
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')
    #double click and close vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    #done start download 1
    pyautogui.moveTo(849, 229)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(892, 411)
    pyautogui.click(button='left')
    #done start download 2
    pyautogui.alert("Done started 2 downloads and closed vlc.")

elif myDownloadCount == 3:
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')
    #double click and close vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    #done start download 1
    pyautogui.moveTo(849, 229)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(892, 411)
    pyautogui.click(button='left')
    #done start download 2
    pyautogui.moveTo(847, 249)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(895, 436)
    pyautogui.click(button='left')
    #done start download 3
    pyautogui.alert("Done started 3 downloads and closed vlc.")

elif myDownloadCount == 4:
    '''pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')'''
    #double click and closes vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    #done start download 1
    pyautogui.moveTo(849, 229)
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.moveTo(892, 411)
    pyautogui.click(button='left')
    #done start download 2
    pyautogui.moveTo(847, 249)
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.moveTo(895, 436)
    pyautogui.click(button='left')
    #done start download 3
    pyautogui.moveTo(857, 273)
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.moveTo(931, 456)
    pyautogui.click(button='left')
    #done start download 4
    pyautogui.alert("Done started 4 downloads and closed vlc.")

elif myDownloadCount == 5:
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')
    #double click and closes vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    #done start download 1
    pyautogui.moveTo(849, 229)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(892, 411)
    pyautogui.click(button='left')
    #done start download 2
    pyautogui.moveTo(847, 249)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(895, 436)
    pyautogui.click(button='left')
    #done start download 3
    pyautogui.moveTo(857, 273)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(931, 456)
    pyautogui.click(button='left')
    #done start download 4
    pyautogui.moveTo(854, 283)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(904, 483)
    pyautogui.click(button='left')
    #done start download 5
    pyautogui.alert("Done started 5 downloads and closed vlc.")

elif myDownloadCount == 6:
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(520, 876)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(509, 825)
    pyautogui.click(button='left')
    #double click and closes vlc
    time.sleep(2)
    pyautogui.moveTo(587, 877)
    pyautogui.click(button='left')
    #opens utorrent on taskbar
    pyautogui.moveTo(801, 515)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    #deselect downloads
    pyautogui.moveTo(842, 212)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(928, 405)
    pyautogui.click(button='left')
    #done start download 1
    pyautogui.moveTo(849, 229)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(892, 411)
    pyautogui.click(button='left')
    #done start download 2
    pyautogui.moveTo(847, 249)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(895, 436)
    pyautogui.click(button='left')
    #done start download 3
    pyautogui.moveTo(857, 273)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(931, 456)
    pyautogui.click(button='left')
    #done start download 4
    pyautogui.moveTo(854, 283)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(904, 483)
    pyautogui.click(button='left')
    #done start download 5
    pyautogui.moveTo(839, 305)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(926, 492)
    pyautogui.click(button='left')
    #done start download 6
    pyautogui.alert("Done started 6 downloads and closed vlc.")