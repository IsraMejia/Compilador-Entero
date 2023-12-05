 
class Generador:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.encabezado = ""
        self.code = ""

    def generar(self, code):
        self.code += code

    def lineaGenerada(self, code):
        self.code += code + '\n'

    def encabezadoLinea(self, code):
        self.encabezado += code + '\n'

    def generaArchivo(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.encabezado + self.code)
    
    def generaStringCode(self):
        codec = self.encabezado + self.code
        return codec


