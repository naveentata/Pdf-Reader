#Python3.x
#Installs necessary modules
import sys
import pyttsx3
import PyPDF2

path = sys.argv[1]

#Opens the file in read mode
pdfFileObj = open(path, 'rb')

#Using PyPDF2 to read the PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a=pdfReader.numPages
print(a)
x=1
c=1

#Function Definition
#Reads specific pages from the PDF
def read(page):
	

    page_content= pdfReader.getPage(int(page))
    
    #Generates a string of texton the page
    b = page_content.extractText()
    print(b)

    # Text to Speech Engine
    engine = pyttsx3.init()

    # Setting the speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(b)
    engine.say("Page number "+str(page)+" is completed")
    
    # Waits until all the text has been read out 
    engine.runAndWait()

    #Stops the engine
    engine.stop()

#Main code - Executed First
while(x):
	
	# Reads input from user
    page = input("Enter the page number to read :")

    #Function call
    read(page)

    # Reads input from user and converts to type: integer 
    c=int(input("Do you want to continue? (1)Yes (2)No"))

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
