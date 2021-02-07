import os,sys

def listfpd(dir):
    return [os.path.abspath(os.path.join(dir, i)) for i in os.listdir(dir)[1:]]
def listfpnd(dir):
    return [os.path.abspath(os.path.join(dir, i)) for i in os.listdir(dir)[1:] 
    if os.path.isdir(os.path.abspath(os.path.join(dir, i)))==False]
def jpf(dir):
    return [i for i in os.listdir(dir)[1:] if i[-3:]=='jpg' or i[-3:]=='png']    
def sps(string):
    return [i for i in string if i==" "].count(" ")
def remv(str):
    return [i for i in str if i in ['a','e','i','o','u']]
   
def prwf(str):
    return [i for i in str.replace(",","").split() if len(i)<4]
def lews(str):
    return {i:len(i) for i in str.replace(",","").replace(":","").replace(".","").split()}    

print(listfpd('.'))
print(listfpnd('.'))
print(jpf('.'))
print(sps("How many   s p a c e s in this   string? ?"))
print(remv("Remove and print all vowels from this string"))
print(prwf("print all words that have less than four characters from this string: ball, bat, cat, apple, pc, pen, foe, hue, cold"))
print(lews("Print the length of each word in this sentence,\
 by using a dictionary in Python. The word and the word's length should be printed."))

