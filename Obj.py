class objeto():
    def __init__(self):
        self.vertices = []
        self.faces=[]
    def readObj(self,filename):
        #Lee el archivo y separa las lineas en una lista
        with open(filename) as f:
            self.lines=f.read().splitlines()
        #Lee linea por linea
        for linea in self.lines:
            if linea:
                #revisa cual es el inicio de la linea
                prefix, valor = linea.split(" ",1)
                #inicio de linea de vertice
                if prefix=="v":
                    self.vertices.append(list(map(float,valor.split(" "))))
                #inicio de la linea de cara
                elif prefix=="f":
                    cadenas=valor.split(" ")
                    #verticesAU=[]
                    lol=[]
                    for cadena in cadenas:
                        #solo toma el valor que dice que vertice se esta trabajando
                        #v,r=cadena.split("/",1)
                        #verticesAU.append(int(v))
                        lol.append(list(map(int,cadena.split("/"))))
                    #guarda todos los vertices que se trabajan
                    self.faces.append(lol)
