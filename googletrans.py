from googletrans import Translator
x = Translator()
text1 = input("enter you sentence:")
text2 = input("enter the language to be translated:")
res = x.translate(text1,dest=text2)
print("the original text:",text1)
print("translated text:",res)