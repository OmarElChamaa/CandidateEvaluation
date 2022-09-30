import sys
import solution 
import plotter 
import logging


#on recupere le chemin vers le fichier solution du candidat   
# solution = sys.argv[1]

#on recupere le nom du candidat
candidate = sys.argv[2]

bdd = sys.argv[3]

logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)
logging.info("in test.py")

testName = "Test 1"
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


#on creer un nouveau candidat 
c = plotter.Candidat(candidate,testSolution(),"Test 1")
c2 = plotter.Candidat("C2",10,"Test 1")
c3 = plotter.Candidat("C3",9,"Test 1")
c4 = plotter.Candidat("C2",2,"Test 2")

t = plotter.Test(testName,tests)

c.write_json()
c2.write_json()
c3.write_json()
c4.write_json()

t.write_json()