import json
from difflib import get_close_matches
from googletrans import Translator
import tkinter as tk

translator=Translator(service_urls=['translate.googleapis.com'])
data=json.load(open("Data.json"))

def jsonmatches(w):
    w=w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean {} instead? Enter Y if yes, or N if no: ".format((get_close_matches(w,data.keys())[0]).upper()))

        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

root=tk.Tk()
root.title("LINGO HUB")
root.geometry("900x375")
root.configure(bg="red")

word=tk.StringVar()
word1=tk.StringVar()
word2=tk.StringVar()
word3=tk.StringVar()
word4=tk.StringVar()

def submit(word_var,definition_var):
    definition_var.delete(0)
    word_val=word_var.get()
    translated_word_val=translator.translate(word_val,dest='en')
    print("The Translated Word: ",translated_word_val.text)

    '''
    translator.translate()
    Input: sentence = Der Himmel ist blau und ich mag Bananen
    Output: Object of the form 
            Translated(src=de, dest=en, text=The sky is blue and I like bananas, pronunciation=The sky is blue and I like bananas, extra_data="{'translat...")

    To obtain the translated text we will have to access the 'text' paramter in the Translated object and it can be done as sentence.text
    '''
    output=jsonmatches(translated_word_val.text)

    if type(output)==list:
        definition_var.insert(0,"\n".join(output))
    else:
        definition_var.insert(0,output)

name_label=tk.Label(root, text = 'Enter a word: ', bg='cyan',font=('calibre',12))
name_entry=tk.Entry(root,textvariable = word,bg='cyan', font=('calibre',12,'normal'))

name_label1=tk.Label(root, text = 'Enter a word: ',bg='cyan', font=('calibre',12))
name_entry1=tk.Entry(root,textvariable = word1,bg='cyan', font=('calibre',12,'normal'))

name_label2=tk.Label(root, text = 'Enter a word: ',bg='cyan', font=('calibre',12))
name_entry2=tk.Entry(root,textvariable = word2, bg='cyan', font=('calibre',12,'normal'))

name_label3=tk.Label(root, text = 'Enter a word: ',bg='cyan', font=('calibre',12))
name_entry3=tk.Entry(root,textvariable = word3,bg='cyan',  font=('calibre',12,'normal'))

name_label4=tk.Label(root, text = 'Enter a word: ',bg='cyan', font=('calibre',12))
name_entry4=tk.Entry(root,textvariable = word4, bg='cyan', font=('calibre',12,'normal'))

definition_label=tk.Label(root, text="Its Meaning: ",bg='yellow', font=('calibre',12))
definition=tk.Entry(root,width=80,bg='yellow', font=('calibre',12,'normal'))

sub_btn=tk.Button(root,text = 'Submit',command=lambda : submit(word,definition))

definition_label1=tk.Label(root, text="Its Meaning: ",bg='yellow', font=('calibre',12))
definition1=tk.Entry(root,width=80,bg='yellow',font=('calibre',12,'normal'))
sub_btn1=tk.Button(root,text = 'Submit',command=lambda : submit(word1,definition1))

definition_label2=tk.Label(root, text="Its Meaning: ", bg='yellow',font=('calibre',12))
definition2=tk.Entry(root,width=80,bg='yellow',font=('calibre',12,'normal'))
sub_btn2=tk.Button(root,text = 'Submit',command=lambda : submit(word2,definition2))

definition_label3=tk.Label(root, text="Its Meaning: ",bg='yellow', font=('calibre',12))
definition3=tk.Entry(root,width=80,bg='yellow',font=('calibre',12,'normal'))
sub_btn3=tk.Button(root,text = 'Submit',command=lambda : submit(word3,definition3))

definition_label4=tk.Label(root, text="Its Meaning: ",bg='yellow', font=('calibre',12))
definition4=tk.Entry(root,width=80,bg='yellow',font=('calibre',12,'normal'))
sub_btn4=tk.Button(root,text = 'Submit',command=lambda : submit(word4,definition4))

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
definition_label.grid(row=1,column=0)
definition.grid(row=1,column=1)

sub_btn.grid(row=2,column=1)

name_label1.grid(row=3,column=0)
name_entry1.grid(row=3,column=1)
definition_label1.grid(row=4,column=0)
definition1.grid(row=4,column=1)

sub_btn1.grid(row=5,column=1)

name_label2.grid(row=6,column=0)
name_entry2.grid(row=6,column=1)
definition_label2.grid(row=7,column=0)
definition2.grid(row=7,column=1)

sub_btn2.grid(row=8,column=1)

name_label3.grid(row=9,column=0)
name_entry3.grid(row=9,column=1)
definition_label3.grid(row=10,column=0)
definition3.grid(row=10,column=1)

sub_btn3.grid(row=11,column=1)

name_label4.grid(row=12,column=0)
name_entry4.grid(row=12,column=1)
definition_label4.grid(row=13,column=0)
definition4.grid(row=13,column=1)

sub_btn4.grid(row=14,column=1)

root.mainloop()

# from googletrans import Translator
# translator = Translator(service_urls=['translate.googleapis.com'])
# s = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
# print(s)
