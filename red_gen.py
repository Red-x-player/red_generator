#!/usr/bin/python3.7
# Author: Mozzamil Eltayeeb (red-x)
# Last Updated: 29/03/20
# v1.0

#~~~~~~~~~~~~~~~~~import libs~~~~~~~~~~~~~~~~~~~~~#
import sys,os,time

#~~~~~~~~~~~~~~~~~print colors~~~~~~~~~~~~~~~~~~~~#
w="\033[1;37m"
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
yellow="\033[1;33m"
b="\033[1;34m"

#~~~~~~~~~~~~~~~~~~  banner  ~~~~~~~~~~~~~~~~~~~~~#
os.system("clear")
print(r+"         .---.        .-----------")
print(r+"        /     \  __  /    ------     "+w+"Red_Generator")
print(r+"       / /     \(  )/    -----       "+w+"Author: red-x")
print(r+"      //////   ' \/ `   ---          "+w+"Twitter: @mozzamil_redx")
print(r+"     //// / // :    : ---            "+w+"Version: 1.0")
print(r+"    // /   /  /`    '--              "+w+"https://github.com/red-x-player/red_generator")
print(r+"   //          //..\\")
print(r+"          "+yellow+"===="+b+"UU"+yellow+"===="+b+"UU"+yellow+"====")
print(r+"              '//||\\`")
print(r+"                 ''``"+w)
time.sleep(0.9)
print(g+"[+] "+y+"Welcome to red generator tool")
time.sleep(0.9)
print(g+"[+] "+r+"[warning]"+y+" Two words will create more than 10 million passwords")

#~~~~~~~~~~~~~~~~~~~ read common symbol ~~~~~~~~~~#
def read_common():
    common_word = ""
    f = open("common.txt","r")
    for word in f:
        common_word = common_word+","+word.replace("\n","")
    common_word = common_word[1::].strip().split(",")
    return common_word

#~~~~~~~~~~~~~~~~~~ Get input from user ~~~~~~~~~~#
def get_user_input():
    time.sleep(0.9)
    input_type = input(g+"[+]"+y+" Enter file[1] words[2]: "+w)
    if (int(input_type) == 1):
        #Full file path with no replace
        time.sleep(0.9)
        filePath= input(g+"[+] "+y+"Enter your file path: "+w)
        words = ""
        f = open(filePath,"r")
        for line in f:
            words = words +","+line.replace("\n","")
        words = words[1::].strip().split(",")
        return words
    else :
        time.sleep(0.9)
        print(g+"[+]"+y+" Enter the words to create wordlist [finsh with 0]")
        words = ""
        while 1:
            user_input = input(g+"[+] "+y)
            if(user_input == "0"):
                words = words[1::].split(",")
                return words
            else:
                words = words+","+user_input.strip()
#~~~~~~~~~~~~~~~~~create wordlist method~~~~~~~~~~~~~~~~~~~~~#
def create_wordlist(words,common):
    i,j,k,l,m,x = 0,0,0,0,0,1
    #=====================[set file name]===================
    wordlist_name = "wordlist.txt"
    while 1:
        if(os.path.exists(wordlist_name)):
            wordlist_name = "wordlist{0}.txt".format(x)
            x = x + 1
        else:
            break
    #====================[level1 to create wordlist]=================
    ofile = open(wordlist_name,"a")
    while i<len(words):
        while j<len(words):
            password = words[i]+words[j]
            if(len(password)<8):
                pass
            else:
                ofile.write(password+"\n")
            j=j+1
        i,j = i+1,0
    i,j = 0,0
    #====================[level2 to create wordlist]=================
    while i<len(common):
        while j<len(words):
            while k<len(common):
                while l<len(words):
                    while m<len(common):
                        password = common[i]+words[j]+common[k]+words[l]+common[m]
                        if(len(password)<8):
                            pass
                        else:
                            ofile.write(password+"\n")
                        m = m +1
                    l,m =l+1,0
                k,l=k+1,0
            j,k = j+1,0
        i,j = i+1,0
    ofile.close()
    print(g+"[+] "+y+"The wordlist saved into "+w+wordlist_name)
    time.sleep(0.9)
    print(g+"[+]"+y+" done!!")

common_words = read_common()        
user_inputs = get_user_input()
time.sleep(0.9)
print(g+"[+]"+y+" Wait moments...")
create_wordlist(user_inputs,common_words)
