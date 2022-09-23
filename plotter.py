#ici on accede a la bdd en json, on la parse et on affiche les donnees grace a plotly

# il faudra donner le nom du fichier json a ouvrir en parametre
import json
from os import path 
import matplotlib.pyplot as plot
import pandas as pd
from json.decoder import JSONDecodeError

class Candidat : 
    def __init__(self,name,grade):
        self.name = name 
        self.grade = grade 
    #fonction qui sert a mettre en format dic pour integration facile dans le json 
    def toData(c): 
        data ={   
            'Name': c.name, 
            'Grade' :c.grade 
        }
        return data
    

class Test : 
    def __init__(self,name,nbQuestions):
        self.name = name 
        self.nbQuestions = nbQuestions
    #fonction qui sert a mettre en format dic pour integration facile dans le json 
    def toData(t):
        data ={   
            'Name': t.name, 
            'nbQuestions' : t.nbQuestions
        }
        return data

# ce test fonctionne 
# if "Test 1" in dict :
#     print("is present")
# else :
#     print("not present")


#il faut que cette fonction prenne en compte que le json existe mais soit vide aussi 
#on peut aussi check si la table existe deja, et la creer si ce n'est pas le cas
#au lieu d'avoir result comme nom de table j'aimerais que ca soit le nom du test
def write_json(data,table,filename='sample.json'):
    print("writing")
    dict = {
        table : [{
        "Name" : data[0],
        "Grade" : data[1]  
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
                if table in dict :
                    print("The table",table,"is in the dictionnary")
                    dict = {
                        "Name" : data[0],
                        "Grade" : data[1]  
                    }

                print("Appending")
                # First we load existing data into a dict.
                jsonStr = json.load(infile)
                jsonStr[table].append(dict)
                #jsonStr["Result"] = dict
                print(jsonStr)
                
                #jsonStr["Result"].append(dict)

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
        
    # xAxis = [key for key, value in data.items()]
    # yAxis = [value for key, value in data.items()]

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


y = ["Omar",5]
x = ["man",3]
p = ["patrick",9]
o = ["pat",18]


# #print(y)
write_json(y,"Test 1")
write_json(x,"Test 1")
write_json(p,"Test 1")
write_json(o,"Test 2")

jsonPlot("sample.json")

