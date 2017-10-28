#import all the needed packages
import sys
import pyttsx3
import PyPDF2

path = sys.argv[1]

#files = open(path,'r')

#matter = files.read()
#print (matter)

pdfFileObj = open(path, 'rb') #open the the need pdf file path
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #read the pdf file path
a=pdfReader.numPages #find the number of pages in the file path
print(a) #print the number of pages
x=1
c=1

#Reads the PDF

def read(page): #create the read pdf function

    page_content= pdfReader.getPage(int(page)) #get the needed page index
    b = page_content.extractText() #collect text of pdf and store in variable b
    print(b) #print the text of the pdf
    #begin runing the text to speach function
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(b)
    engine.say("Page number "+str(page)+" is completed") #display when the page is done
    engine.runAndWait()
    engine.stop()

# The main code
while(x): #start the while function to read the pdf continously
    page = input("Enter the page number to read :") #ask the user for the page read desired

    read(page) #calls the read function and passes in the users desired page to read
    c=int(input("Do you want to continue? (1)Yess (2)No")) #ask the user to continue
    if(c==2): #if the user picks (2)No then the x variable then becomes 0 and the while function stops
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
