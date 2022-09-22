from fileinput import filename
import os 
import git 
import sys 
import subprocess



#je suppose qu'on a un fichier test.py qui testera les solution des candidats
# repoLink = sys.argv[1]
# repoName = sys.argv[2]
testFile = sys.argv[3]
solutionFile = sys.argv[4]
candidateName = sys.argv[5]
#nom de la bdd sur laquelle on compte stocker les infos (une bdd pour tous les test ou une pour chacun ?)
bdd = sys.argv[6]

# if len(sys.argv) < 7 :
#    raise TypeError("Pas assez d'arguments, il en faut 6")

# if len(sys.argv) > 7  : 
#    print("Trop d'arguments, seulement les 5 premiers seront pris en compte  ")


#on utilise les liens ssh pour clone les projets des candidats 
repoLink = 'git@github.com:OmarElChamaa/EvaluationCandidats.git'
repoName = 'EvaluationCandidats'

repo = git.Repo.clone_from(repoLink,repoName)

def test_solution(testFile,solutionFile,candidateName,bdd) : 
   print("Checking candidate's solution \n")
   #os.system("python",testFiletestFile)
   subprocess.call([testFile,solutionFile,candidateName,bdd])



#Je pourrais ici uniquement recuperer le fichier dont on a besoin avec
#cloned_repo = repo.clone(os.path.join(rw_dir, 'to/this/path'))
#assert cloned_repo.__class__ is Repo     # clone an existing repository


#mon programme prendra comme argument: le nom dun candidat , le nom du fichier rendu par le candidat et son lien github et le nom d'un fichier contenant les test
#en sortie, on aura le nombre de test reussis que j'ajouterais a une bdd en json (?)
# avec ces infos je pourrais avoir des stats que je pourrais modeliser grace a plotly

# Retrieve a file from the commit tree
# You can use the path helper to get the file by filename

#targetfile = commit.tree / 'some_file.md'

# Retrieve contents of targetfile

#with io.BytesIO(targetfile.data_stream.read()) as f:
 # print(f.read().decode('utf-8'))
# fonction test qui me renvera un tuple avec le nombre de tests reussi et (?)
# et me creer un json avec toutes les donnees
# data = {

       # 'name' : candidate_name,
      #  'exam' : test_results ,
   #}
   #dataDb = json.dumps(data)
#
