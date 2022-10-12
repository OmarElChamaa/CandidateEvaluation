import os
import git
from interface import Interface
import argparse
import logging
import sys




def main() -> int:
    logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug("in main ")

    parser = argparse.ArgumentParser (description='Evaluate a candidate.')
    #So the user can choose to have a gui or not, when gui is enabled, ignore all other arguments if there are any
    subparser = parser.add_subparsers(dest='option')

    term = subparser.add_parser('term')

   #  term.add_argument('--gui',action = 'store_true',help="Enable a graphical interface for input")
    term.add_argument('repoLink',metavar = 'repoLink',type = str ,help="Valid link to candidate git repo")
    term.add_argument('repoName',metavar = 'repoName',type = str ,help="Valid name of the candidate git repo")
    term.add_argument('candidateName',metavar ='candidateName',type = str ,help="Candidate name")
    term.add_argument('solutionFile',metavar ='solutionFile',type = str ,help="Name of the candidates solution file")
    term.add_argument('testFile'    ,metavar = 'testFile',type = str,help="Name of the test file")
    term.add_argument('database',metavar = 'database',type = str ,help="Name of new or existing database")

    args = parser.parse_args()


    if (args.option == '--term'):
        logging.debug("terminal mode ")
        repoLink = args.repoLink
        repoName = args.repoName
        candidateName = args.candidateName
        solutionFile = args.solutionFile
        testFile = args.testFile
        database = args.database
        commandLineArg = ".\\" + testFile + " " + candidateName + " " + database + " " + testFile
    else:
        logging.debug("graphical mode")
        gui = Interface()
        gui.mainloop()
        commandLineArg = gui.return_fields[0]
        repoLink = gui.return_fields[1]
        repoName = gui.return_fields[2]
        solutionFile = gui.return_fields[3]

    # on utilise les liens ssh pour clone les projets des candidats
    # repoLink = 'git@github.com:thrichert/capcode-candidate.git'
    # repoName = 'capcode-candidate'



    logging.debug("Command line arg in main is : %s", commandLineArg)

    repo = git.Repo.clone_from(repoLink, repoName)

    # On deplace le fichier de solution du candidat pour faciliter son import plus tard dans test.py
    os.replace(".\\" + repoName + "\\" + solutionFile, ".\\" + solutionFile)
    logging.info("Checking candidate's solution \n")
    os.system(commandLineArg)

    return 0


if __name__ == "__main__":
    sys.exit(main())
