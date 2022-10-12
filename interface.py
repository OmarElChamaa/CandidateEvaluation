import sys
import tkinter as tk
import logging

logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG)

fields = 'First Name', 'Last Name', 'Repo Link', 'Repo Name', 'Candidate File', \
         'Test File', 'Database (json)'


class Interface(tk.Tk):
    def __init__(self, root, return_fields=[]):
        self.root = root
        root.title("CapCode")
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))

        root.bind('<Return>', (lambda event, e=entries: self.getUserInput(e)))
        b1 = tk.Button(root, text='OK',
                       command=(lambda e=entries: self.getUserInput(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Quit', command=self.quit)
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        # on utilisera return fields pour stocker les infos rentrees pour pouvoir les utilsier dans main
        self.return_fields = return_fields

    def showMessage(self,message):
        master = tk.Tk()
        msg = tk.Message(master, text=message)
        msg.config(bg='red', font=('times', 24, 'italic'))
        msg.pack()
        tk.mainloop()

    # def getArgs(self):
    #     return self.return_fields

    def getUserInput(self, entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            if text == "":
                logging.debug(field + "is empty ")
                self.showMessage("PLease fill in all fields")
                exit(1)
        firstName = entries[0][1].get()
        logging.debug('first name is ' + firstName)

        lastName = entries[1][1].get()
        logging.debug('lastName is ' + lastName)

        repoLink = entries[2][1].get()
        logging.debug('repoLink is ' + repoLink)

        repoName = entries[3][1].get()
        logging.debug('repoName is ' + repoName)

        solutionFile = entries[4][1].get()
        logging.debug('solutionFile is ' + solutionFile)

        testFile = entries[5][1].get()
        logging.debug('testFile is ' + testFile)

        database = entries[6][1].get()
        logging.debug('database is ' + database)

        commandLineArg = ".\\" + testFile + " " + firstName + lastName + " " + database + " " + testFile
        logging.debug("Command line arg is : %s", commandLineArg)
        print(commandLineArg)

        self.return_fields = [commandLineArg, repoLink, repoName, solutionFile]
        self.quit 
        return

    # def createFields(self, fields):
    #     entries = []
    #     for field in fields:
    #         row = tk.Frame(self)
    #         lab = tk.Label(row, width=15, text=field, anchor='w')
    #         ent = tk.Entry(row)
    #         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    #         lab.pack(side=tk.LEFT)
    #         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    #         entries.append((field, ent))
    #     return entries

