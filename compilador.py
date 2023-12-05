from scanner import *
from generador import *
from parse import *


def main():
    print(" \n\t\tCompilador PERRON\n") 

    source = '''
        IMPRIMIR "Compilador pro"
        IMPRIMIR "cuantas veces quiere ser saludado?"
        ENTRADA s 
        LET a = 0
        WHILE a < s REPETIR
            IMPRIMIR "Hola" 
            LET a = a + 1 
        ENDWHILE

        IMPRIMIR "Fin del programa"
    '''

    # Initialize the scanner, generador, and parser.
    scanner = Scanner(source)
    generador = Generador("out.c")
    parser = Parser(scanner, generador)

    parser.programa() # Start the parser.
    generador.generaArchivo() # Write the output to file.
    
    
    print(" \n\t\tFin del Compilador PERRON\n") 

main()
