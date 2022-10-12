# CandidateEvaluation
Le but de ce projet est de recuperer les solutions d'un candidats depuis un depot git, tester ses resultats et les stocker.
L'objectif etant de pouvoir comparer les differents resultats et notes obtenus des candidats 

Utilisation : 


Mode Graphique 
    python ./main
Terminal 
    python ./main term repoLink repoName candidateName solutionFile testFile database 
    term : option terminal 
    repoLink : Lien vers le depot git du candidat 
    repoName : Le nom de ce repo 
    candidateName : "Doe_John"
    solutionFile : Nom du fichier du candidat qu'il faut tester 
    testFile : Fichier qui lancera des tests sur solutionFile 
    database : Nom d'une bdd nouvelle ou existante (json)