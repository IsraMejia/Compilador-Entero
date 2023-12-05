import sys
from scanner import *
from token_an import *
from generador import *

class Parser:

    def __init__(self, scanner, generador):
        self.scanner = scanner
        self.generador = generador

        self.simbolos = set()    
        self.etiquetasdeclarada = set() 
        self.etiquetasGotoed = set() 
 
        self.tokenActual = None
        self.tokenObservandose = None
        self.siguienteToken()
        self.siguienteToken()    

    
    def revisarToken(self, kind):
        return kind == self.tokenActual.tipoToken

    
    def analizarToken(self, kind):
        return kind == self.tokenObservandose.tipoToken

    
    def comparaToken(self, kind):
        if not self.revisarToken(kind):
            self.Abortar("Esperando " + kind.name + ", encontro " + self.tokenActual.tipoToken.name)
        self.siguienteToken()

    
    def siguienteToken(self):
        self.tokenActual = self.tokenObservandose
        self.tokenObservandose = self.scanner.caracterAToken()
        

    
    def revisaOperadorComparacion(self):
        return self.revisarToken(TipodeTokens.MAYOR) or self.revisarToken(TipodeTokens.MAYORIGUAL) or self.revisarToken(TipodeTokens.MENORQUE) or self.revisarToken(TipodeTokens.MENORIGUAL) or self.revisarToken(TipodeTokens.IGUAL) or self.revisarToken(TipodeTokens.DISTINTOA)

    def Abortar(self, message):
        sys.exit("Error: " + message)


    

    
    def programa(self):
        print("programa")
        self.generador.encabezadoLinea("#include <stdio.h>")
        self.generador.encabezadoLinea("int main(void){") 
       
        while self.revisarToken(TipodeTokens.NUEVA_LINEA):
            self.siguienteToken()

        
        while not self.revisarToken(TipodeTokens.FIN_DE_LINEA):
            self.declaracion()

        self.generador.lineaGenerada("return 0;")
        self.generador.lineaGenerada("}")
        
        for etiqueta in self.etiquetasGotoed:
            if etiqueta not in self.etiquetasdeclarada:
                self.Abortar("intentando ir a una etiqueta no declarada: " + etiqueta)


    
    def declaracion(self):
        

        if self.revisarToken(TipodeTokens.IMPRIMIR):
            print("Imprimiendo declaración")
            self.siguienteToken()

            if self.revisarToken(TipodeTokens.STRING):
                self.generador.lineaGenerada("printf(\"" + self.tokenActual.caracterToken + "\\n\");")               
                self.siguienteToken()

            else:
                self.generador.generar("printf(\"%" + ".2f\\n\", (float)(")
                self.expression()
                self.generador.lineaGenerada("));")

       
        elif self.revisarToken(TipodeTokens.IF):
            print("declarando IF")
            self.siguienteToken()
            self.generador.generar("if(")
            self.comparacion()

            self.comparaToken(TipodeTokens.THEN)
            self.nl()
            self.generador.lineaGenerada("){")

           
            while not self.revisarToken(TipodeTokens.ENDIF):
                self.declaracion()

            self.comparaToken(TipodeTokens.ENDIF)
            self.generador.lineaGenerada("}")

        
        elif self.revisarToken(TipodeTokens.WHILE):
            print("declarando WHILE")
            self.generador.generar("while(")
            self.siguienteToken()
            self.comparacion()

            self.comparaToken(TipodeTokens.REPETIR)
            self.nl()
            self.generador.lineaGenerada("){")
           
            while not self.revisarToken(TipodeTokens.ENDWHILE):
                self.declaracion()

            self.comparaToken(TipodeTokens.ENDWHILE)
            self.generador.lineaGenerada("}")



        elif self.revisarToken(TipodeTokens.LABEL):
            print("declarando etiqueta")
            self.siguienteToken()

            if self.tokenActual.caracterToken in self.etiquetasdeclarada:
                self.Abortar("etiqueta ya existente: " + self.tokenActual.caracterToken)
            self.etiquetasdeclarada.add(self.tokenActual.caracterToken)

            self.generador.lineaGenerada(self.tokenActual.caracterToken + ":")
            self.comparaToken(TipodeTokens.VARIABLE)

        
        elif self.revisarToken(TipodeTokens.GOTO):
            print("declaracion-GOTO")
            self.siguienteToken()
            self.etiquetasGotoed.add(self.tokenActual.caracterToken)
            self.generador.lineaGenerada("goto " + self.tokenActual.caracterToken + ";")
            self.comparaToken(TipodeTokens.VARIABLE)

        
        elif self.revisarToken(TipodeTokens.LET):
            print("declaracion-Numerica LET")
            self.siguienteToken()

           
            if self.tokenActual.caracterToken not in self.simbolos:
                self.simbolos.add(self.tokenActual.caracterToken)
                self.generador.encabezadoLinea("float " + self.tokenActual.caracterToken + ";")

            self.generador.generar(self.tokenActual.caracterToken + " = ")
            self.comparaToken(TipodeTokens.VARIABLE)
            self.comparaToken(TipodeTokens.IGUAL)
            
            self.expresion()
            self.generador.lineaGenerada(";")

        
        elif self.revisarToken(TipodeTokens.ENTRADA):
            print("declaracion-Entrada")
            self.siguienteToken()

            
            if self.tokenActual.caracterToken not in self.simbolos:
                self.simbolos.add(self.tokenActual.caracterToken)
                self.generador.encabezadoLinea("float " + self.tokenActual.caracterToken + ";")

             
            self.generador.lineaGenerada("if(0 == scanf(\"%" + "f\", &" + self.tokenActual.caracterToken + ")) {")
            self.generador.lineaGenerada(self.tokenActual.caracterToken + " = 0;")
            self.generador.generar("scanf(\"%")
            self.generador.lineaGenerada("*s\");")
            self.generador.lineaGenerada("}")
            self.comparaToken(TipodeTokens.VARIABLE)

         
        else:
            self.Abortar("declaracion invalida " + self.tokenActual.caracterToken + " (" + self.tokenActual.tipoToken.name + ")")

        
        self.nl()


    
    def comparacion(self):
        print("comparacion")

        self.expresion()
        
        if self.revisaOperadorComparacion():
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()
            self.expresion()
        else:
            self.Abortar("Operador de comparación esperado en: " + self.tokenActual.caracterToken)

       
        while self.revisaOperadorComparacion():
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()
            self.expresion()


    
    def expresion(self):
        print("expresion")

        self.terminoMat()
        
        while self.revisarToken(TipodeTokens.SUMA) or self.revisarToken(TipodeTokens.RESTA):
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()
            self.terminoMat()


    
    def terminoMat(self):
        print("terminoMat")
        self.unario()        
        while self.revisarToken(TipodeTokens.ASTERISCO) or self.revisarToken(TipodeTokens.DIAGONAL):
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()
            self.unario()


    
    def unario(self):
        print("unario")
        if self.revisarToken(TipodeTokens.SUMA) or self.revisarToken(TipodeTokens.RESTA):
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()        
        self.primario()


    
    def primario(self):
        print("primario (" + self.tokenActual.caracterToken + ")")
        if self.revisarToken(TipodeTokens.NUMERO): 
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()

        elif self.revisarToken(TipodeTokens.VARIABLE):            
            if self.tokenActual.caracterToken not in self.simbolos:
                self.Abortar("Variable de referencia antes de la asignación: " + self.tokenActual.caracterToken)
            
            self.generador.generar(self.tokenActual.caracterToken)
            self.siguienteToken()
        else:
            self.Abortar("Token inesperado en " + self.tokenActual.caracterToken)

    
    def nl(self):
        print("Nueva Linea")        
        self.comparaToken(TipodeTokens.NUEVA_LINEA)        
        while self.revisarToken(TipodeTokens.NUEVA_LINEA):
            self.siguienteToken()