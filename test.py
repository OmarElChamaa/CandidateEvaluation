#Prend 1 seul argument, la solution du candidats a tester 

import sys
import plotter 

#on recupere le nom du fichier 
solution = sys.argv[1]

#on recupere le nom du candidat
candidate = sys.argv[2]

bdd = sys.argv[3]

import solution 

print("in test.py")

def testSolution() :
    testsPassed = 0
    tests = 4   
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
c = plotter.Candidat(candidate,testSolution())

c.write_json()