import colorsys
import os
import webbrowser
import os.path
import click
from pathlib import Path
import subprocess as sp




@click.command()
@click.option('--name','-n',prompt = 'Enter the filename',help = '--Enter The File Name')

def  create( name ):
    print("The file name is"  + name + ":")
    if(os.path.exists(name)):
        print('exists')
        programName = "notepad.exe"
        fileName = name
        sp.Popen([programName, fileName])
        url="http://google.com"
        print(webbrowser.open(url))   
        programName = r"C:\Program Files\Sublime Text 3\subl.exe"
        fileName = name
        sp.Popen([programName, fileName]) 
        programName = r"C:\Users\Naveengowda\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        fileName = name
        sp.Popen([programName, fileName])
        os.system("start cmd")
          
    else:
        print("the file does not exists")
        f=open(name,'w')
        print("and the file is:",f.name)
        with open(name, 'w') as f:
            f.write("open this file \n")
            f.write("and please save this file") 
            f = open(name, "r")
        print("Your project is opened and\n project name is:", f.name)
        while True:
            name1=input("Enter the name of application to open[browser,editor,console]:")
            if name1 =="browser":
                url="http://google.com"
                print(webbrowser.open(url))
            elif name1 =="editor":
                print("1: notepad\n")
                print("2: VisualStudioCode\n")
                print("3: SublimeText\n")
                inp = int(input("Enter a number: "))
                if inp == 1:
                    programName = "notepad.exe"
                    fileName = name
                    sp.Popen([programName, fileName])
                elif inp == 2:
                     programName = r"C:\Users\Naveengowda\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                     fileName = name
                     sp.Popen([programName, fileName])
                elif inp == 3:
                    programName = r"C:\Program Files\Sublime Text 3\subl.exe"
                    fileName = name
                    sp.Popen([programName, fileName]) 
                else:
                    print("Invalid input!")    
            elif name1 =="console":
                    os.system("start cmd")
                     
                   
            else:
                print("Done with it")
                
        f.close()    
   


if __name__ == '__main__':
    create()

    
