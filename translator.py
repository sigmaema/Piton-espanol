import re
import sys
import os

class SiPlusPlus:
    def __init__(self):
        self.translations = {
            'si' : 'if',
            'sino_si' : 'elif',
            'sino' : 'else',
            'mientras' : 'while',
            'para' : 'for',  # Added missing 'para' -> 'for'
            'en' : 'in',
            'romper' : 'break',
            'continuar' : 'continue',
            'pasar' : 'pass',
            'definir' : 'def',
            'retornar' : 'return',
            'clase' : 'class',
            'importar' : 'import',
            'desde' : 'from',
            'como' : 'as',
            'intentar': 'try',
            'excepto': 'except',
            'finalmente': 'finally',
            'con': 'with',
            'y': 'and',
            'o': 'or',
            'no': 'not',
            'es': 'is',
            'Verdadero': 'True',
            'Falso': 'False',
            'Nada': 'None',
            'decir': 'print',
            'imprimir': 'print',  # Added this since your sample code uses 'imprimir'
            'entrada': 'input',
            'longitud': 'len',
            'rango': 'range',
            'texto': 'str',
            'número': 'int',
            'decimal': 'float',
            'lista': 'list',
            'diccionario': 'dict',
            'abrir': 'open',
        }
    
    def translate_line(self, line):
        # If line is empty or just whitespace, return as-is
        if not line.strip():
            return line
            
        # If line is a comment, return as-is
        if line.strip().startswith('#'):
            return line
        
        # Preserve the original line ending
        line_ending = ''
        if line.endswith('\n'):
            line_ending = '\n'
            line = line[:-1]  # Remove the newline for processing
        
        # Preserve leading whitespace (indentation)
        leading_space = len(line) - len(line.lstrip())
        stripped_line = line.strip()
        
        # Translate the line
        translated_line = stripped_line
        for spanish, english in self.translations.items():
            pattern = r'\b' + re.escape(spanish) + r'\b'
            translated_line = re.sub(pattern, english, translated_line)
        
        # Reconstruct the line with original indentation and line ending
        return ' ' * leading_space + translated_line + line_ending
    
    def translate_file(self, input_file, output_file=None):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            translated_lines = [self.translate_line(line) for line in lines]
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.writelines(translated_lines)
                print(f"Translated file saved as {output_file}")
            else:
                base_name = os.path.splitext(input_file)[0]
                output_file = base_name + '_translated.py'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.writelines(translated_lines)
                print(f"Translated file saved as: {output_file}")
            
            return output_file
            
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
            return None
        except Exception as e:
            print(f"Error translating file: {e}")
            return None
    
    def translate_and_execute(self, input_file):
        translated_file = self.translate_file(input_file)
        if translated_file:
            print(f"\nExecuting translated code:")
            print("-" * 40)
            try:
                exec(open(translated_file).read())
            except Exception as e:
                print(f"Error executing code: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_file.txt> [output_file.py]")
        print("   or: python translator.py <input_file.txt> --run")
        return
    
    translator = SiPlusPlus()
    input_file = sys.argv[1]
    
    if len(sys.argv) > 2:
        if sys.argv[2] == '--run':
            translator.translate_and_execute(input_file)
        else:
            output_file = sys.argv[2]
            translator.translate_file(input_file, output_file)
    else:
        translator.translate_file(input_file)

if __name__ == "__main__":
    main()

sample_code = """# Ejemplo en Python Español
definir saludar(nombre):
    decir(f"¡Hola, {nombre}!")
    retornar "Saludado"

para i en rango(5):
    si i % 2 == 0:
        decir(f"Número par: {i}")
    sino:
        decir(f"Número impar: {i}")

nombre = entrada("¿Cómo te llamas? ")
resultado = saludar(nombre)

si longitud(nombre) > 5:
    decir("Tienes un nombre largo")
sino_si longitud(nombre) == 0:
    decir("No ingresaste un nombre")
sino:
    decir("Tienes un nombre corto")

"""

if __name__ == "__main__":
    if len(sys.argv) == 1:  
        with open('ejemplo_espanol.txt', 'w', encoding='utf-8') as f:
            f.write(sample_code)
        print("Sample Spanish Python file created: ejemplo_espanol.txt")
        print("\nTo translate and run:")
        print("python translator.py ejemplo_espanol.txt --run")
        print("\nTo just translate:")
        print("python translator.py ejemplo_espanol.txt")
    else:
        main()