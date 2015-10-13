import Image
import ImageEnhance
import ImageFilter
import sys
from pytesseract import *

threshold=140
table=[]
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)
rep={'O':'0','I':'1','L':'1','Z':'2','S':'8'};

def  getverify1(name):  

	im = Image.open(name)  
	imgry = im.convert('L')  
	imgry.save('g'+name)  
	out = imgry.point(table,'1')  
	out.save('b'+name)  
	text = image_to_string(out)  
	text = text.strip()  
	text = text.upper();  

	for r in rep:  
		text = text.replace(r,rep[r])  

#out.save(text+'.jpg')  
	print text  
	return text  
getverify1('v1.jpg')  
getverify1('v2.jpg')  
getverify1('v3.jpg')  
getverify1('v4.jpg')
