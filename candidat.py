class Candidat : 
    def __init__(self,name,grade,test):
        self.name = name 
        self.grade = grade 
        self.test = test
    def toData(self):
        dict = {
            "Name" : self.name,
            "Grade" : self.grade 
        }
        return dict