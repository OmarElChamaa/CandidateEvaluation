#ici on accede a la bdd en json, on la parse et on affiche les donnees grace a plotly

# il faudra donner le nom du fichier json a ouvrir en parametre
import json
from os import path 
import matplotlib.pyplot as plot
import pandas as pd
from json.decoder import JSONDecodeError
# import sqlite3

listObj = []

def dataSimul() :

    dict = {
        "Test 1" :
        [{
            'Name': "Omar", 
            'Grade' : 3 , 
        }]
    }
    simData=json.dumps(dict)
    with open("sample.json", "w") as outfile:
        outfile.write(simData)



#il faut que cette fonction prennes en compte que le json existe mais soit vide aussi 
def write_json(data,table,filename='sample.json'):
    print("writing")

    dict = {
        "Result" : [{
        "Test" : data[0],
        "Name" : data[1],
        "Grade" : data[2]  
        }]
    }
        
    if path.isfile(filename) is False: #on creer le json s'il n'existe pas  
        print("Creating json")
        
        jsonStr =  json.dumps(dict)
        with open("sample.json", "w") as outfile: 
            outfile.write(jsonStr)
    else :
        with open(filename) as infile:
            #on verifie si le json est vide ou pas 
            if path.getsize(filename) == 0 :
                print("The file is empty: ")
                
            else:
                # First we load existing data into a dict.
                jString = json.load(infile)
                
                jString = jString["Result"].append(dict)

            jString =  json.dumps(dict)
        with open("sample.json", "w") as outfile: 
            outfile.write(jString)

# def write_json(data,table, filename='sample.json'):
#     print("writing")
#     dict = {}
#     jString=[]
#     if path.isfile(filename) is False: #on creer le json s'il n'existe pas  
#         print("Creating json")
#         dict = {
#             "Result" : [{
#                 "Test" : data[0],
#                 "Name" : data[1],
#                 "Grade" : data[2]  
#             }]
#         }
#         jsonStr =  json.dumps(dict)
#         with open("sample.json", "w") as outfile: 
#             outfile.write(jsonStr)       
#     else :
#         with open(filename) as infile:
#             # First we load existing data into a dict.
#             jString = json.load(infile)
#             try:
#                 dict = {
#                     "Test" : data[0],
#                     "Name" : data[1],
#                     "Grade" : data[2]  
#                 }
#                 print("here")
#                 jString.append(dict)

#                 with open(filename,'w') as outfile :
#                     jString = json.dumps(dict)
#                     outfile.write(jString) 

#             except JSONDecodeError:
#                 print("here 3")
#                 pass
            
            # Join new_data with file_data inside emp_details
        

    #dict[table].update(data)
    #dict[table] = data
        # convert back to json.
    # with open(filename, 'w') as f:
    #         json.dump(dict, f,indent =4)
    




def jsonPlot(fileName) :
    data = json.load(open(fileName, 'r'))
    #print( data['candidats'])

    #data = data['candidats']


    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]

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
#dict = dataSimul()

y = ["Test 1","Omar",5]
x= ["Test 1","man",3]
p= ["Test 1","patrick",9]


print(y)
write_json(y,"Result")
write_json(x,"Result")
# write_json(p,"Result")

# ce test fonctionne 
# if "Test 1" in dict :
#     print("is present")
# else :
#     print("not present")
# y = {   
#     'Name': "Khaled", 
#     'Grade' :4 , 
#     }



#jsonPlot("sample.json")


#Tentative sqlite #################################################################


# #Cette fonction se connecte a la bdd si elle existe, sinon elle la creer 
# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except sqlite3.Error as e:
#         print(e)
#         print("Creating database")
#         create_connection(r"pythonsqlite.db")
#         conn = sqlite3.connect(db_file)
#     return conn 
    
    # finally:
    #     if conn:
    #         conn.close()


# if __name__ == '__main__':
#     create_connection(r"pythonsqlite.db")

# #Verifie si les 3 tables existent ,les creer si elle n'existent pas 
# def checkTable(conn) :
#     c = conn.cursor()
    
    ## POUR QUIZZ
    # c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Quizz' ''')
    # if c.fetchone()[0]==1 : {
	#     print('Quizz Table exists.')
    # }
    # else :
    #     print('Creating Table')
    # c.execute(''' CREATE TABLE Quizz() )
        
    # ##Pour candidat 

    # c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Candidat' ''')
    # if c.fetchone()[0]==1 : 
    #     print('Candidat Table exists.')
    # else :
    #     print('Creating Table')

    # ##POUR GRADE

    # c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Grade' ''')
    # if c.fetchone()[0]==1 : 
    #     print('Grade Table exists.')
    # else :
    #     print('Creating Table')



        

# def writeData (data,table,bdd) :
#     print("writing")
#     conn = create_connection(bdd)
