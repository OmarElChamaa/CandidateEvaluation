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





def write_json(data,table, filename='sample.json'):
    print("writing")
    dict = {}
    if path.isfile(filename) is False: #on creer le json s'il n'existe pas
        with open("sample.json", "w") as outfile:
            data ={
                table :
                [{
                    data
                }]
            }
            json.dump(dict, outfile,indent =4)
            outfile.write(data)
            
    else :
        #with open(filename) as file:
        with open(filename, 'a+') as infile, open(filename, 'w') as outfile:
            # First we load existing data into a dict.
            # dict = json.load(file)
            try:
                dict = json.load(infile)
                dict[table].append(data)
                json.dump(dict, outfile)

            except JSONDecodeError:
                pass
            
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

y = {   
    'Name': "Khaled", 
    'Grade' :4 , 
    }
write_json(y,"Test 1")

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
