from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

encImagePath = ""
decImagePath = ""
filedirectory = ""

root = Tk()
root.title("ImageIntext")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

radioValue = StringVar()
encrypt = ttk.Radiobutton(mainframe, text='Hide Text', variable=radioValue, value='encrypt')
decrypt = ttk.Radiobutton(mainframe, text='Unhide Text', variable=radioValue, value='decrypt')

encrypt.grid(column=2, row=1, sticky=(W))
decrypt.grid(column=3, row=1, sticky=(E))

path = "pp.png"
firstPhoto = Image.open(path)
labelWidth = labelHeight = 500
maxsize = (labelWidth, labelHeight)

firstPhoto = firstPhoto.resize(maxsize)
ph = ImageTk.PhotoImage(firstPhoto)


encImage = Label(mainframe, image = ph)
encImage.photo = ph # WHY ARE WE USIMG THIS?
encImage.grid(column=1, row=2)

decImage = Label(mainframe, image = ph)
decImage.photo = ph
decImage.grid(column=4, row=2)

# textbox
message = Text(mainframe, height = 5)
message.insert('1.0', 'Enter the text to hide in the left image in this box. After hiding, the modified image \
will be saved in the original image\'s directory')
message.grid(column=1, row=3, columnspan=4, padx = 5, pady =5)

def insertImage(radioValue,fileName):
    newPhoto = Image.open(fileName)
    newPhoto = newPhoto.convert(mode = "RGBA")
    newPhoto = newPhoto.resize(maxsize)
    nph = ImageTk.PhotoImage(newPhoto)

    if radioValue.get() == 'encrypt':
        global encImage
        encImage.configure(image = nph)
        encImage.image = nph
        global encImagePath
        encImagePath = fileName
    else:
        global decImage
        decImage.configure(image = nph)
        decImage.image = nph
        global decImagePath
        decImagePath = fileName

def openfiledialog():
    # filedialog.askopenfilename()
    filename = filedialog.askopenfilename(title = "Select file")
    global filedirectory
    filedirectory = os.path.dirname(filename)
    insertImage(radioValue, filename)

def processImage(whattodo):
    if whattodo == 'encrypt':
        stringToEncrypt = str(message.get('1.0', 'end'))

        asciiValueString = []
        # print(type(asciiValueString))
        # j = 0
        for c in stringToEncrypt:
            asciiValueString.append(ord(c))

        # print("the value of asciiValueString is " + str(asciiValueString))

        fileName = encImagePath
        # print ('filename is ' + fileName)
        newPhoto = Image.open(fileName)
        newPhoto = newPhoto.convert(mode = "RGBA")
        x,y = newPhoto.size
        a = newPhoto.getdata()
        b = list(a)
        c = [list(elem) for elem in b]
        # print(c[:10])
        i = 0
        for i in range(len(asciiValueString) + 1):
            # print('entered')
            if i == 0:
               c[0] = [0,0,0,0]
               i = i+1
               continue
            c[i][3] = asciiValueString[i-1]
            i = i+1
            if(i == len(asciiValueString)):
                # print('boss')
                c[len(asciiValueString)] = [0,0,0,0]
                break
    
        # print (c[:len(asciiValueString)+ 1])

        d = [tuple(l) for l in c]
        # print(d[:10])
        new_im = Image.new("RGBA", (x,y))
        new_im.putdata(d)
        x = filedirectory + '/decrypted.png'
        new_im.save(x)
        # /Users/kushagraagarwal/Documents/GITRepositoriesMine/TextInImage/dist/final.app/Contents/Resources/decrypted.png
    else:
        fileName = decImagePath
        newPhoto = Image.open(fileName)
        newPhoto = newPhoto.convert(mode = "RGBA")
        a = newPhoto.getdata()
        b = list(a)

        # print (b[:10])
        # print("The hidden is : " + str(b[0][3]))

        if ((b[0][0] + b[0][1] + b[0][2] + b[0][3]) != 0):
            message.replace('1.0','end', 'OOPS! You should use the image which has been encrypted with this!')
            return
        string = []
        i = 0
        for x in range(len(b)):
            if i==0:
                i = i+1
                continue
            # print(b[i])
            if ((b[i][0] + b[i][1] + b[i][2] + b[i][3]) == 0):
                break
            string.append(b[i][3])
            i = i+1
        s = ''.join(chr(i) for i in string)

        # print(s)

        hiddenMessage = "The hidden message from the image is " + "'" + s + "'"
        message.replace('1.0','end', hiddenMessage)
        # print(s[:20])
        # print(len(s[:20]))

uploadButton = ttk.Button(mainframe, text='Upload', command = lambda: openfiledialog())
uploadButton.grid(column=2, row=4, columnspan=2)

proceedButton = ttk.Button(mainframe, text='Hide/Unhide', command = lambda : processImage(radioValue.get()))
proceedButton.grid(column=2, row=2, columnspan=2)

# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()