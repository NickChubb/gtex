#!/usr/bin/env python3

#-----generate.py-----#
#
# This is the main py
# file that generates
# the LaTeX files
#
#---------------------#

#----Dependencies----#
import sys
import fileinput
import os
import shutil

import pylatex

from datetime import date

def createReport(projectData):
    # Types: name, studentnum, date, prof, course, title, school

    fileName = projectData["title"] + "/main.tex"

    shutil.copyfile("templates/report.tex", fileName)

    # Read in the file
    with open(fileName, "r") as file :
        f = file.read()

    # Replace the target string
    f = f.replace("&NAME&", projectData["name"])
    f = f.replace("&STUDENTNUM&", projectData["studentnum"])
    f = f.replace("&DATE&", projectData["date"])
    f = f.replace("&PROF&", projectData["prof"])
    f = f.replace("&COURSE&", projectData["course"])
    f = f.replace("&TITLE&", projectData["title"])
    f = f.replace("&SCHOOL&", projectData["school"])

    # Write the file out again
    with open(fileName, "w") as file:
        file.write(f)
    

def createNotes(projectData):
   # Types: name, date, prof, course, title

    fileName = projectData["title"] + "/main.tex"

    shutil.copyfile("templates/notes.tex", fileName)

    # Read in the file
    with open(fileName, "r") as file :
        f = file.read()

    # Replace the target string
    f = f.replace("&NAME&", projectData["name"])
    f = f.replace("&DATE&", projectData["date"])
    f = f.replace("&PROF&", projectData["prof"])
    f = f.replace("&COURSE&", projectData["course"])
    f = f.replace("&TITLE&", projectData["title"])

    # Write the file out again
    with open(fileName, "w") as file:
        file.write(f)


def createAssignment(projectData):
    # Types: name, studentnum, date, prof, course, title

    fileName = projectData["title"] + "/main.tex"

    shutil.copyfile("templates/assignment.tex", fileName)

    # Read in the file
    with open(fileName, "r") as file :
        f = file.read()

    # Replace the target string
    f = f.replace("&NAME&", projectData["name"])
    f = f.replace("&STUDENTNUM&", projectData["studentnum"])
    f = f.replace("&DATE&", projectData["date"])
    f = f.replace("&PROF&", projectData["prof"])
    f = f.replace("&COURSE&", projectData["course"])
    f = f.replace("&TITLE&", projectData["title"])

    # Write the file out again
    with open(fileName, "w") as file:
        file.write(f)


def createFolder(projectData):

    projectTitle = projectData["title"]

    os.mkdir(projectTitle)
    os.mkdir(projectTitle + "/src")
    os.mkdir(projectTitle + "/img")
    os.mkdir(projectTitle + "/tex")

    infoFile = open(projectTitle + "/project_info.txt", "w+")

    infoFile.write("Type: " + projectData["type"] + "\n")
    infoFile.write("Title: " + projectData["title"] + "\n")
    infoFile.write("Name: " + projectData["name"] + "\n")
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

    if projectData["type"] == "r":
        createReport(projectData)
    elif projectData["type"] == "n":
        createNotes(projectData)
    elif projectData["type"] == "a":
        createAssignment(projectData)
    else:
        print("ERROR: no document type selected, please restart.")

    print("Success! Created project directory: " + projectData["title"])




#--------Main--------#
def main():

    projectData = {"type": "", "name": "", "studentnum": "", "title": "", "date": "", "school": "", "course": "", "prof": ""}
    
    print("Welcome to G-TeX v.1")
    print("ctrl-c if you would not like to create a LaTeX project file in your current directory")
    print("Current project types are: report (r), assignment (a), notes (n)")

    while projectData["type"] != "r" and projectData["type"] != "a" and projectData["type"] != "n":
        projectData["type"] = input("Enter the type of project you want to make: ")
        if projectData["type"] != "r" and projectData["type"] != "a" and projectData["type"] != "n":
            print("ERROR: value must be either r, a, n or ctl-c to quit")
    
    while projectData["name"] == "":
        projectData["name"] = input("Enter your name: ")
        if projectData["name"] == "":
            print("ERROR: must enter valid name")

    while projectData["studentnum"] == "":
        projectData["studentnum"] = input("Enter your student number: ")
        if projectData["studentnum"] == "":
            print("ERROR: must enter valid student number")

    while projectData["title"] == "":
        projectData["title"] = input("Enter the title of the project: ")
        if projectData["title"] == "":
            print("ERROR: must enter valid title")

    while projectData["date"] == "":
        projectData["date"] = input("Enter the due date or current date: ")
        if projectData["date"] == "":
            print("ERROR: must enter valid date")
    
    while projectData["school"] == "":
        projectData["school"] = input("Enter your school's name: ")
        if projectData["school"] == "":
            print("ERROR: must enter valid school")
    
    while projectData["course"] == "":
        projectData["course"] = input("Enter the course name: ")
        if projectData["course"] == "":
            print("ERROR: must enter valid course")

    while projectData["prof"] == "":
        projectData["prof"] = input("Enter the professor's name: ")
        if projectData["prof"] == "":
            print("ERROR: must enter valid prof")

    generate(projectData)
    




if __name__ == "__main__":
    main()
