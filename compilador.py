from scanner import *
from generador import *
from parse import * 
import subprocess

def c_code_to_asm(c_code):
    # Crear un archivo temporal con el código C
    with open('temp.c', 'w') as f:
        f.write(c_code)

    # Llamar a gcc para compilar el código C y generar el ensamblador
    subprocess.run(['gcc', '-S', 'temp.c'])

    # Leer el contenido del archivo ensamblador generado
    with open('temp.s', 'r') as f:
        asm_code = f.read()

    return asm_code



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
    generador = Generador("codigo_Objeto.c")
    parser = Parser(scanner, generador)

    parser.programa() # Start the parser.
    generador.generaArchivo() # Write the output to file.
    
    
    asm_code = c_code_to_asm(generador.generaStringCode()) 
    archivo = open("codigoASM.asm", "w")
    archivo.write(asm_code)
    archivo.close()


    print(" \n\t\tFin del Compilador PERRON\n")  
     
main()
