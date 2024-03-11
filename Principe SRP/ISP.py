#Exemple sans ISP

class Machine:
    def print(self):
        pass
    
    def scan(self):
        pass

class MultiFunctionPrinter(Machine):
    def print(self):
        # print document
        pass
    
    def scan(self):
        # Scan document
        pass

#Refactorisation de l'exemple avec ISP

class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self):
        # print document
        pass
    
    def scan(self):
        # Scan document
        pass
