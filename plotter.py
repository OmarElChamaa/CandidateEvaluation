#ici on accede a la bdd en json, on la parse et on affiche les donnees grace a plotly

# il faudra donner le nom du fichier json a ouvrir en parametre
import json
from os import path 
import matplotlib.pyplot as plot
import pandas as pd
from json.decoder import JSONDecodeError

class Candidat : 
    def __init__(self,name,grade,test):
        self.name = name 
        self.grade = grade 
        self.test = test 
    def write_json(self,filename='sample.json'):
        print("writing")
        dict = {
            self.test : [{
            "Name" : self.name,
            "Grade" : self.grade 
            }]
        }
        if path.isfile(filename) is False: #on creer le json s'il n'existe pas  
            print("Creating json")
            jsonStr =  json.dumps(dict)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr)
        else :
            with open(filename,'r+') as infile:
                #on verifie si le json est vide ou pas 
                if path.getsize(filename) == 0 :
                    print("The file is empty: ")
                    jsonStr = dict 
                    jsonStr =  json.dumps(jsonStr)
                else: #il faudra tester ici si la tale existe deja ou pas 
                    jsonStr = json.load(infile)
                    if self.test in jsonStr :
                        print("The table",self.test,"is in the dictionnary")
                        dict = {
                            "Name" : self.name,
                            "Grade" : self.grade 
                        }
                        print("Appending")
                        jsonStr[self.test].append(dict)
                    else : 
                        jsonStr.update(dict)
                        infile.seek(0)
                    print(jsonStr)
                    jsonStr =  json.dumps(jsonStr)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr)
    
    

class Test : 
    def __init__(self,name,nbQuestions):
        self.name = name 
        self.nbQuestions = nbQuestions
    #fonction qui sert a mettre en format dic pour integration facile dans le json 
    def toData(self):
        data = [self.name, self.nbQuestions]
        return data
    def write_json(self,table='Test',filename='sample.json'):
        print("writing")
        dict = {
            table : [{
            "Name" : self.name,
            "nbQuestions" : self.nbQuestions  
            }]
        }
        if path.isfile(filename) is False: #on creer le json s'il n'existe pas  
            print("Creating json")
            jsonStr =  json.dumps(dict)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr)
        else :
            with open(filename,'r+') as infile:
                #on verifie si le json est vide ou pas 
                if path.getsize(filename) == 0 :
                    print("The file is empty: ")
                    jsonStr = dict 
                    jsonStr =  json.dumps(jsonStr)
                else: #il faudra tester ici si la tale existe deja ou pas 
                    jsonStr = json.load(infile)
                    if table in jsonStr :
                        print("The table",table,"is in the dictionnary")
                        dict = {
                            "Name" : self.name,
                            "nbQuestions" : self.nbQuestions
                        }
                        print("Appending")
                        jsonStr[table].append(dict)
                    else :
                        jsonStr.update(dict)
                        infile.seek(0)                        
                    print(jsonStr)
                    jsonStr =  json.dumps(jsonStr)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr) 
    

def jsonPlot(fileName,table='Test 1') :
    data = json.load(open(fileName, 'r'))
    print("data is ",data[table] )
    data = data[table] 
    xAxis=[]
    yAxis=[]
    for result in data :
        print ("Candidate",result['Name'],"Grade",result['Grade'])
        xAxis.append(result['Name'])
        yAxis.append(result['Grade'])


    plot.grid(True)
    print(xAxis)

    ## BAR GRAPH o##
    #fig = plot.figure()
    plot.bar(xAxis,yAxis, color='maroon')
    plot.xlabel('Name')
    plot.ylabel('grade')

    print(yAxis)
    total = 0
    for i in yAxis:
        total = i + total

    average = total/ len(data)
    print("la moyenne de ce test est de : " ,average)
    plot.axhline(y=average, color ='r',linestyle='-')
    plot.show()
