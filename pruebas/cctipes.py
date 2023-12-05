import Cython

def c_to_asm(c_code):
  """
  Traduce código C a lenguaje ensamblador utilizando Cython.

  Args:
    c_code: Código C a traducir.

  Returns:
    Código ensamblador equivalente.
  """

  # Creamos un objeto de la clase Cython.

  c_to_asm = Cython.C_to_ASM()

  # Convertimos el código C a código ensamblador.

  asm_code = c_to_asm.convert(c_code)

  return asm_code


if __name__ == "__main__":
  c_code = """
  int main() {
    int a = 1;
    int b = 2;

    a = a + b;a

    return 0;
  }
  """

  asm_code = c_to_asm(c_code)

  print(asm_code)
