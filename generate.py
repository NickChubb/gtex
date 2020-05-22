#-----generate.py-----#
#
# This is the main py
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

def createFolder(projectData):

    projectTitle = projectData["title"]

    os.mkdir(projectTitle)
    os.mkdir(projectTitle + "/src")
    os.mkdir(projectTitle + "/img")
    os.mkdir(projectTitle + "/tex")

    infoFile = open(projectTitle + "/project_info.txt", "w+")

    infoFile.write("Type: " + projectData["type"] + "\n")
    infoFile.write("Author: " + projectData["author"] + "\n")
    infoFile.write("Student Number: " + projectData["studentnum"] + "\n")
    infoFile.write("Date: " + projectData["date"] + "\n")
    infoFile.write("School: " + projectData["school"] + "\n")
    infoFile.write("Course: " + projectData["course"] + "\n")
    infoFile.write("Prof: " + projectData["prof"] + "\n")
    infoFile.write("\n")
    infoFile.write("This file was generated automatically by G-TeX on " + date.today().strftime("%B %d, %Y"))

    infoFile.close()

    



#----Generates Project---#

def generate(projectData):

    createFolder(projectData)

    #createFiles(projectData)

    # DONE !




#--------Main--------#
def main():

    projectData = {"type": ""}
    
    print("Welcome to G-TeX v.1")
    print("ctrl-c if you would not like to create a LaTeX project file in your current directory")
    print("Current project types are: report (r), assignment (a), notes (n)")

    while projectData["type"] != "r" and projectData["type"] != "a" and projectData["type"] != "n":
        projectData["type"] = input("Enter the type of project you want to make: ")

        if projectData["type"] != "r" and projectData["type"] != "a" and projectData["type"] != "n":
            print("ERROR: value must be either r, a, n or ctl-c to quit")
    
    projectData["author"] = input("Enter your name: ")
    projectData["studentnum"] = input("Enter your student number: ")
    projectData["title"] = input("Enter the title of the project: ")
    projectData["date"] = input("Enter the due date or current date: ")
    projectData["university"] = input("Enter your school's name: ")
    projectData["course"] = input("Enter the course name: ")
    projectData["prof"] = input("Enter the professor's name: ")

    generate(projectData)
    




if __name__ == "__main__":
    main()