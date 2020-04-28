from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import json
import requests
import matplotlib.pyplot as plt 

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
    daydata = day.split(",");
    date  = daydata[6]+daydata[7]+"/"+daydata[4]+daydata[5]+"/"+daydata[0]+daydata[1]+daydata[2]+daydata[3]
    dates.apppend(date)
    power.append(daydata[1])
    weather.apppend(daydata[7])
    print("Date: {0}, Power : {1}, Weather : {2}".format(date, daydata[1], daydata[7])) 
    if index == daysago:
        break


# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = power
  
# labels for bars 
tick_label = dates
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 

message = "Hi Pam"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()