import sys
import pyttsx3
import PyPDF2

path = sys.argv[1]

#files = open(path,'r')

#matter = files.read()
#print (matter)

pdfFileObj = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a=pdfReader.numPages
print(a)
x=1
c=1

#Reads the PDF

def read(page):

    page_content= pdfReader.getPage(int(page))
    b = page_content.extractText()
    print(b)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(b)
    engine.say("Page number "+str(page)+" is completed")
    engine.runAndWait()
    engine.stop()

# The main code
while(x):
    page = input("Enter the page number to read :")
    
    read(page)
    c=int(input("Do you want to continue? (1)Yess (2)No"))
    if(c==2):
        x=0
        print("Thank you")
    
     



    
 





#engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-50)

#engine.say(matter)
#engine.runAndWait()
#engine.stop()


#engine.say('The quick brown fox jumped over the lazy dog.')







#pdfFileObj = open('/home/naveentata/Downloads/0132678209.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#a=pdfReader.numPages
#print(a)
#page_content= pdfReader.getPage(0)
#b = page_content.extractText()
#print(b)
