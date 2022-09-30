from doctest import testfile
from email import parser
from fileinput import filename
import os 
import git 
import argparse



#je suppose qu'on a un fichier test.py qui testera les solution des candidats
# repoLink = sys.argv[1]
# repoName = sys.argv[2]
# testFile = sys.argv[3]
# solutionFile = sys.argv[4]
# candidateName = sys.argv[5]
# #nom de la bdd sur laquelle on compte stocker les infos (une bdd pour tous les test ou une pour chacun ?)


# solutionFile = "solution.py"
# testfile = "test.py"
# bdd = 'sample.json'

# if len(sys.argv) < 7 :
#    raise TypeError("Pas assez d'arguments, il en faut 6")

# if len(sys.argv) > 7  : 
#    print("Trop d'arguments, seulement les 5 premiers seront pris en compte  ")

#init parser 
parser = argparse.ArgumentParser (description='Evaluate a candidate.')


parser.add_argument('repoLink',metavar = 'repoLink',type = str ,help="Valid link to candidate git repo")
parser.add_argument('repoName',metavar = 'repoName',type = str ,help="Valid name of the candidate git repo")
parser.add_argument('candidateName',metavar ='candidateName',type = str ,help="Candidate name")
parser.add_argument('solutionFile',metavar ='solutionFile',type = str ,help="Name of the candidates solution file")
parser.add_argument('testFile'    ,metavar = 'testFile',type = str,help="Name of the test file")
parser.add_argument('database',metavar = 'database',type = str ,help="Name of new or existing database")

args = parser.parse_args()

repoLink = args.repoLink
repoName = args.repoName
candidateName = args.candidateName
solutionFile = args.solutionFile
testFile = args.testFile
database = args.database 

#on utilise les liens ssh pour clone les projets des candidats 
# repoLink = 'git@github.com:thrichert/capcode-candidate.git'
# repoName = 'capcode-candidate'

commandLineArg =".\\" +testFile + " " + ".\\" +solutionFile + " " + candidateName + " " + database
print("Command line arg is : ", commandLineArg)


repo = git.Repo.clone_from(repoLink,repoName)

#On deplace le fichier de solution du candidat pour faciliter son import plus tard dans test.py
os.replace(".\\"+repoName+"\\" +solutionFile , ".\\" +solutionFile)

def test_solution() : 
   print("Checking candidate's solution \n")
   os.system(commandLineArg)

test_solution()
