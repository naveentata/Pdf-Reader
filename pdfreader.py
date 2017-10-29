import sys #importing sys module
import pyttsx3 #importing pytttsx3 module
import PyPDF2#importing PyPDF2 module

path = sys.argv[1] #taking command line arguments from the terminal

#files = open(path,'r')

#matter = files.read()
#print (matter)

pdfFileObj = open(path, 'rb') # creating a Pdf file object from the given path in read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a=pdfReader.numPages
print(a)
x=1
c=1


def read(page): 
    """
    Function to read a particular page in a pdf 
    """
    page_content= pdfReader.getPage(int(page))
    b = page_content.extractText()  #using module function extractText() to read the entire page data in string format
    print(b)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(b)
    engine.say("Page number "+str(page)+" is completed")
    engine.runAndWait()
    engine.stop()

#Client code to read user given page number from a pdf
while(x):
    page = input("Enter the page number to read :")
    
    read(page)
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
