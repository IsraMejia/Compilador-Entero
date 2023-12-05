import enum 

class Token:   
    def __init__(self, caracterToken, tipoToken):
        self.caracterToken = caracterToken  
        self.tipoToken = tipoToken   

    @staticmethod
    def ifPalabraReservada(caracterToken):
        for tipoToken in TipodeTokens: 
            if (tipoToken.name == caracterToken):
                return tipoToken
        return None

  
class TipodeTokens(enum.Enum):
	FIN_DE_LINEA = -1
	NUEVA_LINEA = 0
	NUMERO = 1
	VARIABLE = 2
	STRING = 3 
	# PalabrasReservadas 
	LABEL = 101
	GOTO = 102
	IMPRIMIR = 103
	ENTRADA = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPETIR = 110
	ENDWHILE = 111
    
     # Operadores
	IGUALIGUAL = 201 
	SUMA = 202 
	RESTA = 203
	ASTERISCO = 204
	DIAGONAL = 205
	IGUAL = 206
	DISTINTOA = 207
	MENORQUE = 208
	MENORIGUAL = 209
	MAYOR = 210
	MAYORIGUAL = 211