# from doctest import testfile
from email import parser
# from fileinput import filename
import os 
import git 
import argparse
import logging





#init parser 
parser = argparse.ArgumentParser (description='Evaluate a candidate.')


parser.add_argument('repoLink',metavar = 'repoLink',type = str ,help="Valid link to candidate git repo")
parser.add_argument('repoName',metavar = 'repoName',type = str ,help="Valid name of the candidate git repo")
parser.add_argument('candidateName',metavar ='candidateName',type = str ,help="Candidate name")
parser.add_argument('solutionFile',metavar ='solutionFile',type = str ,help="Name of the candidates solution file")
parser.add_argument('testFile'    ,metavar = 'testFile',type = str,help="Name of the test file")
parser.add_argument('database',metavar = 'database',type = str ,help="Name of new or existing database")




logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)


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
logging.debug("Command line arg is : %s", commandLineArg)


repo = git.Repo.clone_from(repoLink,repoName)

#On deplace le fichier de solution du candidat pour faciliter son import plus tard dans test.py
os.replace(".\\"+repoName+"\\" +solutionFile , ".\\" +solutionFile)

def test_solution() : 
   logging.info("Checking candidate's solution \n")
   os.system(commandLineArg)

test_solution()
