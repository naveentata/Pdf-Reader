import sys
import pyttsx3
import PyPDF2

path = sys.argv[1]  # path to file

#files = open(path,'r')

#matter = files.read()
#print (matter)

pdfFileObj = open(path, 'rb')  # File object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # pdf file reader
a=pdfReader.numPages  # Number of pages in the pdf file
print(a)
x=1  # Flag for loop continuation
c=1  # User's choice for continuing program 1=Yes, 2=No

# Reads out the specified page of the pdf
def read(page):

    page_content= pdfReader.getPage(int(page))  # Page object of page to be read
    b = page_content.extractText()  # Generating a unicode string of text on the page
    print(b)
    engine = pyttsx3.init()  # Defining text to speech engine
    
    #Setting speech rate to 150 words per minute
    rate = engine.getProperty('rate') 
    engine.setProperty('rate', rate-50)
    
    #Reading out text
    engine.say(b)
    engine.say("Page number "+str(page)+" is completed")
    
    #Wait until all text has been read out and stops the engine
    engine.runAndWait()
    engine.stop()

# The loop which interacts with the user to read out their desired page of the file
while(x):
    # User input for page number
    page = input("Enter the page number to read :")
    
    read(page)
    
    # Continuation prompt
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
