from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import json
import requests
import matplotlib.pyplot as plt 
import io

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)


img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 36)

dates =[]
power =[]
weather =[]
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://pvoutput.org/service/r2/getoutput.jsp?key=4d57028d8a05f4c6a593d97a5a5bfe48f4cb261e&sid=41079")
# Print the status code of the response.
dataencode = response.content.decode('utf-8')
data = dataencode.split(";")
daysago = 5
index =0
for day in data:
    index += 1
    daydata = day.split(",")
    date  = daydata[0][6]+daydata[0][7]+"/"+daydata[0][4]+daydata[0][5]+"/"+daydata[0][0]+daydata[0][1]+daydata[0][2]+daydata[0][3]
    dates.append(str(date))
    power.append(int(daydata[1]))
    weather.append(daydata[7])
    print("Date: {0}, Power : {1}, Weather : {2}".format(date, daydata[1], daydata[7])) 
    if index == daysago:
        break


# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = power
  
# labels for bars 
tick_label = dates

# heights of bars 
#height = [10, 24, 36, 40, 5] 
  
# labels for bars 
#tick_label = ['one', 'two', 'three', 'four', 'five'] 

plt.figure(figsize=(8, 6), dpi=50)
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
#plt.show() 

plt.savefig('test.png')
#buf = io.BytesIO()
#plt.savefig(buf, format='png')
#buf.seek(0)
#im = Image.open(buf)
img = Image.open("test.png")
inky_display.set_image(img)
inky_display.show()


#message = "Hi Pam"
#w, h = font.getsize(message)
#x = (inky_display.WIDTH / 2) - (w / 2)
#y = (inky_display.HEIGHT / 2) - (h / 2)

#draw.text((x, y), message, inky_display.RED, font)
#inky_display.set_image(im)
#inky_display.show()
#buf.close()
