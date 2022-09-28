from doctest import testfile
from fileinput import filename
import os 
import git 
import sys 
import subprocess



#je suppose qu'on a un fichier test.py qui testera les solution des candidats
# repoLink = sys.argv[1]
# repoName = sys.argv[2]
# testFile = sys.argv[3]
# solutionFile = sys.argv[4]
# candidateName = sys.argv[5]
# #nom de la bdd sur laquelle on compte stocker les infos (une bdd pour tous les test ou une pour chacun ?)


solutionFile = "solution.py"
testfile = "test.py"
bdd = 'sample.json'

# if len(sys.argv) < 7 :
#    raise TypeError("Pas assez d'arguments, il en faut 6")

# if len(sys.argv) > 7  : 
#    print("Trop d'arguments, seulement les 5 premiers seront pris en compte  ")



#on utilise les liens ssh pour clone les projets des candidats 
repoLink = 'git@github.com:thrichert/capcode-candidate.git'
repoName = 'capcode-candidate'

commandLineArg =".\\" +testfile + " " + ".\\" +solutionFile + " " + "Omar" + " " + "sample.json"
print("Command line arg is : ", commandLineArg)


repo = git.Repo.clone_from(repoLink,repoName)

#On deplace le fichier de solution du candidat pour faciliter son import plus tard dans test.py
os.replace(".\\"+repoName+"\\" +solutionFile , ".\\" +solutionFile)

def test_solution() : 
   print("Checking candidate's solution \n")
   os.system(commandLineArg)

test_solution()
