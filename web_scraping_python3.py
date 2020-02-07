import requests 
from bs4 import BeautifulSoup 
import csv


def clean_a(val):
    l=[]
    l.append(val.contents[1])
    l.append(val.contents[2].text)
    return(l)



#28th
URL="https://www.drikpanchang.com/planet/position/planetary-positions-sidereal.html?date=28/01/2020&time=09:15:00"

#27th
#URL = "https://www.drikpanchang.com/planet/position/planetary-positions-sidereal.html?geoname-id=1275339&date=27/01/2020&time=09:15:00"

#24th
#URL = "https://www.drikpanchang.com/planet/position/planetary-positions-sidereal.html?date=24/01/2020&time=09:15:00"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html.parser') 
data=soup.prettify()
t=soup.find_all('span')


#Asc
val1a=t[24]   #degrees less than 30 and zodiac
val1b=t[36]   #total degrees
#val1c not present
val1d=t[26]   #Nakshatra
val1e=t[34]   #Nakshatra lord 
asc=clean_a(val1a)
asc.append(val1b.text)
asc.append('-')
asc.append(val1d.text)
asc.append(val1e.text)

#Sun
val2a=t[38]   #degrees less than 30 and zodiac
val2b=t[52]   #total degrees
val2c=t[48]   #Residing in 
val2d=t[40]   #Nakshatra
val2e=t[50]   #Nakshatra lord 
sun=clean_a(val2a)
sun.append(val2b.text)
sun.append(val2c.text)
sun.append(val2d.text)
sun.append(val2e.text)

#Moon
val3a=t[54]   #degrees less than 30 and zodiac
val3b=t[68]   #total degrees
val3c=t[64]   #Residing in 
val3d=t[56]   #Nakshatra
val3e=t[66]   #Nakshatra lord 
moon=clean_a(val3a)
moon.append(val3b.text)
moon.append(val3c.text)
moon.append(val3d.text)
moon.append(val3e.text)

#Mars
val4a=t[70]   #degrees less than 30 and zodiac
val4b=t[83]   #total degrees
val4c=t[79]   #Residing in 
val4d=t[72]   #Nakshatra
val4e=t[81]   #Nakshatra lord 
mars=clean_a(val4a)
mars.append(val4b.text)
mars.append(val4c.text)
mars.append(val4d.text)
mars.append(val4e.text)

#Mercury
val5a=t[85]   #degrees less than 30 and zodiac
val5b=t[98]   #total degrees
val5c=t[94]   #Residing in 
val5d=t[87]   #Nakshatra
val5e=t[96]   #Nakshatra lord 
mercury=clean_a(val5a)
mercury.append(val5b.text)
mercury.append(val5c.text)
mercury.append(val5d.text)
mercury.append(val5e.text)

#Jupiter
val6a=t[100]   #degrees less than 30 and zodiac
val6b=t[113]   #total degrees
val6c=t[109]   #Residing in 
val6d=t[102]   #Nakshatra
val6e=t[111]   #Nakshatra lord 
jupiter=clean_a(val6a)
jupiter.append(val6b.text)
jupiter.append(val6c.text)
jupiter.append(val6d.text)
jupiter.append(val6e.text)

#Venus
val7a=t[115]   #degrees less than 30 and zodiac
val7b=t[128]   #total degrees
val7c=t[124]   #Residing in 
val7d=t[117]   #Nakshatra
val7e=t[126]   #Nakshatra lord 
venus=clean_a(val7a)
venus.append(val7b.text)
venus.append(val7c.text)
venus.append(val7d.text)
venus.append(val7e.text)

#Saturn
val8a=t[130]   #degrees less than 30 and zodiac
val8b=t[143]   #total degrees
val8c=t[139]   #Residing in 
val8d=t[132]   #Nakshatra
val8e=t[141]   #Nakshatra lord 
saturn=clean_a(val8a)
saturn.append(val8b.text)
saturn.append(val8c.text)
saturn.append(val8d.text)
saturn.append(val8e.text)

#Rahu
val9a=t[145]   #degrees less than 30 and zodiac
val9b=t[157]   #total degrees
#val9c not present
val9d=t[147]   #Nakshatra
val9e=t[155]   #Nakshatra lord 
rahu=clean_a(val9a)
rahu.append(val9b.text)
rahu.append('-')
rahu.append(val9d.text)
rahu.append(val9e.text)

#Ketu
val10a=t[159]   #degrees less than 30 and zodiac
val10b=t[171]   #total degrees
#val10c not present
val10d=t[161]   #Nakshatra
val10e=t[169]   #Nakshatra lord 
ketu=clean_a(val10a)
ketu.append(val10b.text)
ketu.append('-')
ketu.append(val10d.text)
ketu.append(val10e.text)


asc_final=['Asc']
asc_final.extend(asc)
sun_final=['Sun']
sun_final.extend(sun)
moon_final=['Moon']
moon_final.extend(moon)
mars_final=['Mars']
mars_final.extend(mars)
mercury_final=['Mercury']
mercury_final.extend(mercury)
jupiter_final=['Jupiter']
jupiter_final.extend(jupiter)
venus_final=['Venus']
venus_final.extend(venus)
saturn_final=['Saturn']
saturn_final.extend(saturn)
rahu_final=['Rahu']
rahu_final.extend(rahu)
ketu_final=['Ketu']
ketu_final.extend(ketu)

print(soup.title.text[:36])
print('Asc: ')
print(*asc_final, sep = ", ")

print('Sun: ')
print(*sun_final, sep = ", ")
print('Moon: ')
print(*moon_final, sep = ", ")
print('Mars: ')
print(*mars_final, sep = ", ")
print('Mercury: ')
print(*mercury_final, sep = ", ")
print('Jupiter: ')
print(*jupiter_final, sep = ", ")
print('Venus: ')
print(*venus_final, sep = ", ")
print('Saturn: ')
print(*saturn_final, sep = ", ")
print('Rahu: ')
print(*rahu_final, sep = ", ")
print('Ketu: ')
print(*ketu_final, sep = ", ")
'''

with open(soup.title.text[:10]+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Planet','Angle less than 30','Zodiac','Total angle','Residing in','Nakshatra','Nakshtra lord'])
    writer.writerow(asc_final)
    writer.writerow(sun_final)
    writer.writerow(moon_final)
    writer.writerow(mars_final)
    writer.writerow(mercury_final)
    writer.writerow(jupiter_final)
    writer.writerow(venus_final)
    writer.writerow(saturn_final)
    writer.writerow(rahu_final)
    writer.writerow(ketu_final)
'''
