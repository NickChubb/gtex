#-----generate.py-----#
#
# Thi   s is the main py
# file that generates
# the LaTeX files
#
# To-Do -> Generate LaTeX for project types
#
#---------------------#

#----Dependencies----#
import sys
import fileinput
import os
import shutil

import pylatex

from datetime import date

#---Global Variables---#

#More types: Formula Sheet, .........   ?

def createFolder(projectData):

    projectTitle = projectData["title"]

    os.mkdir(projectTitle)
    os.mkdir(projectTitle + "/src")
    os.mkdir(projectTitle + "/img")
    os.mkdir(projectTitle + "/tex")

    infoFile = open(projectTitle + "/project_info.txt", "w+")

    infoFile.write("Type: " + projectData["type"] + "\n")
    infoFile.write("Author: " + projectData["author"] + "\n")
    infoFile.write("Date: " + projectData["date"] + "\n")
    infoFile.write("Course: " + projectData["course"] + "\n")
    infoFile.write("Prof: " + projectData["prof"] + "\n")
    infoFile.write("\n")
    infoFile.write("This file was generated automatically by G-TeX on " + date.today().strftime("%B %d, %Y"))



#----Generates Project---#

def generate(projectData):

    createFolder(projectData)

    #createFiles(projectData)

    # DONE !




#--------Main--------#
def main():

    projectData = {}
    
    print("Welcome to G-TeX v.1")
    print("ctrl-c if you would not like to create a LaTeX project file in your current directory")
    print("Current project types are: report (r), assignment (a), notes (n)")

    projectData["type"] = input("Enter the type of project you want to make: ")
    projectData["author"] = input("Enter your name: ")
    projectData["title"] = input("Enter the title of the project: ")
    projectData["date"] = input("Enter the due date or current date: ")
    projectData["course"] = input("Enter the course name: ")
    projectData["prof"] = input("Enter the professor's name: ")

    generate(projectData)
    




if __name__ == "__main__":
    main()