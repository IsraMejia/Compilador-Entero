import clang

def clang_to_asm(c_code):
  """
  Traduce código C a lenguaje ensamblador utilizando Clang.

  Args:
    c_code: Código C a traducir.

  Returns:
    Código ensamblador equivalente.
  """

  # Creamos un analizador léxico y sintáctico de Clang.

  c_parser = clang.cindex.Parser()

  # Parseamos el código C.

  translation_unit = c_parser.parse(c_code)

  # Obtenemos el código ensamblador del analizador.

  asm_code = translation_unit.get_assembly()

  return asm_code


if __name__ == "__main__":
  c_code = """
  int main() {
    int a = 1;
    int b = 2;

    a = a + b;

    return 0;
  }
  """

  asm_code = clang_to_asm(c_code)

  print(asm_code)
