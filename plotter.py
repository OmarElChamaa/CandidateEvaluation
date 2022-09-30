import json
from os import path 
import matplotlib.pyplot as plot
import logging

logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)


class Plotter : 
    def __init__(self) -> None:
        pass
    def jsonPlot(fileName,table='Test 1') :
        data = json.load(open(fileName, 'r'))
        logging.debug("data is ",data[table] )
        data = data[table] 
        xAxis=[]
        yAxis=[]
        for result in data :
            logging.info ("Candidate",result['Name'],"Grade",result['Grade'])
            xAxis.append(result['Name'])
            yAxis.append(result['Grade'])


        plot.grid(True)
        ## BAR GRAPH o##
        #fig = plot.figure()
        plot.bar(xAxis,yAxis, color='maroon')
        plot.xlabel('Name')
        plot.ylabel('grade')
        total = 0
        for i in yAxis:
            total = i + total

        average = total/ len(data)
        logging.info("la moyenne du test ", table ,"est de : " ,average)
        plot.axhline(y=average, color ='r',linestyle='-')
        plot.show()
        
    def write_json(data,table,filename):
        logging.debug("writing")
        dict = {
            table : [data]
        }
        if path.isfile(filename) is False: #on creer le json s'il n'existe pas  
            logging.debug("Creating json")
            jsonStr =  json.dumps(dict)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr)
        else :
            with open(filename,'r+') as infile:
                #on verifie si le json est vide ou pas 
                if path.getsize(filename) == 0 :
                    logging.debug("The file is empty: ")
                    jsonStr = dict 
                    jsonStr =  json.dumps(jsonStr)
                else: #il faudra tester ici si la tale existe deja ou pas 
                    jsonStr = json.load(infile)
                    if table in jsonStr :
                        logging.info("The table %s is in the dictionnary",table)
                        logging.debug("Appending")
                        jsonStr[table].append(data)
                    else : 
                        jsonStr.update(dict)
                        infile.seek(0)
                    logging.debug(jsonStr)
                    jsonStr =  json.dumps(jsonStr)
            with open("sample.json", "w") as outfile: 
                outfile.write(jsonStr)
