from PIL import Image, ImageDraw, ImageFont
import random
from datetime import datetime

defaultDict = {}
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
for num in range(1, 1000):
    defaultDict.update({f'{1000-num}': f'{num}'})

print(defaultDict)
now1 = datetime.now()
dt_string1 = now1.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
print(defaultDict['511'])