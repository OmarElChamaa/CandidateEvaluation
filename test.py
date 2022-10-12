import os
import shutil
import solution 
import plotter 
import logging
import candidat
import argparse
import stat
from subprocess import call 


parser = argparse.ArgumentParser (description='Test Candidate answers.')
parser.add_argument('repoName',metavar ='repoName',type = str ,help="Repo name")
parser.add_argument('candidateName',metavar ='candidateName',type = str ,help="Candidate name")
parser.add_argument('database',metavar = 'database',type = str ,help="Name of new or existing database")
parser.add_argument('testFile'    ,metavar = 'testFile',type = str,help="Name of the test file")
args = parser.parse_args()

repoName = args.repoName 
candidateName = args.candidateName
database = args.database 
testFile = args.testFile

class Test : 
    def __init__(self,name,nbQuestions):
        self.name = name 
        self.nbQuestions = nbQuestions
    def toData(self):
        dict = {
            "Name" : self.name,
            "nbQuestions" : self.nbQuestions 
        }
        return dict
    #from stack overflow to delete .git files in the cloned directory 
    
    


logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)
logging.info("in test.py")

tests = 4 

def testSolution() :
    testsPassed = 0
    if solution.addition(1,1)==2 : 
        testsPassed+=1
    if solution.soustraction(2,1)==1 : 
        testsPassed+=1
    if solution.mult(5,5)==25 : 
        testsPassed+=1
    if solution.div(2,1)==1 :
        testsPassed+=1
    return testsPassed 



c = candidat.Candidat(candidateName,testSolution(),testFile)
data = c.toData()
logging.info("converted data is ", data)
plotter.Plotter.write_json(data,c.test,database)

t = Test(testFile,tests)
data = t.toData()
plotter.Plotter.write_json(data,testFile,database)


def on_rm_error(func,path,exe_info) :    
    os.chmod(path,stat.S_IWRITE)
    os.unlink(path)

def removeRepo(dir):
    for i in os.listdir(dir) :
        if i.endswith('git'):
            tmp = os.path.join(dir,i)
    while True : 
        call(['attrib','-H',tmp])
        break 
    shutil.rmtree(tmp,onerror = on_rm_error)

removeRepo(repoName)
shutil.rmtree(repoName)
os.remove('solution.py')