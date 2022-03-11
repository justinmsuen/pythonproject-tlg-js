#!/usr/bin/python3
#***Document Sanitizer***

import fileinput
import sys

#Requests for inputs from user such as what word/phrase they would like to replace and how many#times
def user_inputs(filename):
    user_word = input("What word/phrase (Case sensitive) would you like to replace? > ")
    if (wordFinder(filename, user_word)) == 0:
        print("There are no instances of the word/phrase you would like to replace. ")
        user_inputs(filename)
    else:        
        print("1. Would you like to replace all occurrences of this word/phrase with ***?")
        print("2. Or specify the occurrences you'd like to replace?")
        user_option = int(input("Please select 1 or 2. > "))
        if user_option == 1:
            replaceAll(filename, user_word)
        elif user_option == 2:
            replaceSome(filename, user_word) 
        else:
            print("Incorrect output.")
            user_inputs(filename)


#Search for term to see if there is anything to replace
def wordFinder(filename, user_word):
    count = 0
    with open(filename, "r") as testfile:
        for line in testfile:
            if user_word in line:
                count += 1
    return count

#Go through document line by line and ask user if they want to replace each instance 
def replaceSome(filename, user_word):    
    new_file = []
    with open(filename, "r") as testfile:     
        for num, line in enumerate(testfile, 1):
            if user_word in line:
                print(line, f"(line {num})") 
                choice = input("Replace? (Y/N) ")
                if choice.upper() == "Y":
                    replace_line = line.replace(user_word, "***")
                    print(replace_line)
                    new_file.append(replace_line)
                else:
                    new_file.append(line)
            else:
                new_file.append(line)
    with open(filename, "w") as testfile2:
        testfile2.writelines(new_file)

#    with open(filename, "r+") as testfile:
#        file_lines = testfile.readlines()
        #print(file_lines)
#        for line in file_lines:
#            print(line)
#            if user_word in line:
#                print(line)
#                choice = input("Replace? (Y/N) ")
#                if choice.upper() == "Y":
                    #file_lines[line].replace(user_word, "***")
#                    file_lines.write(line.replace(user_word, "***"))
                    #file_lines.index(line).replace(user_word, "***")
#        print(file_lines)

#Replace all instances of word/phrase with ***
def replaceAll(filename, user_word):
    with open(filename, "r") as testfile:
        file_lines = testfile.read()

    new_file = file_lines.replace(user_word, "***")

    with open(filename, "w") as testfile2:
        testfile2.write(new_file)
    
#Describes program and asks for name of file to scan
def main():
    print("****This is the Document Sanitizer!****")
    print("This program allows you to sanitize a file document by replacing any/all instances of words or phrases that you choose with ****, keeping parts of it selectively secret should it fall into the wrong hands.")
    init_input=input("Enter the name of the file, or type exit to end the program: ")
    #try:
    #test = open(init_input, "r")
    #test.close()
    if init_input.lower() == "exit":
        print("Exiting now")
        exit()
    user_inputs(init_input)
    #except:
   #     print("Invalid file name")


if __name__  == "__main__":
    main()
    
