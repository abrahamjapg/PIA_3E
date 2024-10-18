def cifrar_cesar(texto, desplazamiento):
    # Inicializa una cadena vacía para almacenar el resultado cifrado
    resultado = ""
    
    for letra in texto:
        # Cifrar mayúsculas
        if letra.isupper():
            # Aplica el desplazamiento y ajusta el valor para que se mantenga dentro del rango de letras mayúsculas
            resultado += chr((ord(letra) + desplazamiento - 65) % 26 + 65)
        # Cifrar minúsculas
        elif letra.islower():
            # Aplica el desplazamiento y ajusta el valor para que se mantenga dentro del rango de letras minúsculas
            resultado += chr((ord(letra) + desplazamiento - 97) % 26 + 97)
        else:
            # No cifrar caracteres que no son letras
            resultado += letra  
    return resultado

def cifrar_archivo(input_file, output_file, desplazamiento):
    try:
        # Abre el archivo de entrada en modo lectura
        with open(input_file, 'r', encoding='utf-8') as archivo_entrada:
            texto = archivo_entrada.read()  # Lee todo el contenido del archivo
        
        # Llama a la función de cifrado César para cifrar el texto leído
        texto_cifrado = cifrar_cesar(texto, desplazamiento)
        
        # Abre el archivo de salida en modo escritura
        with open(output_file, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_cifrado)  # Escribe el texto cifrado en el archivo de salida
        
        # Mensaje de confirmación
        print(f'El archivo "{input_file}" ha sido cifrado y guardado como "{output_file}".')
    except FileNotFoundError:
        # Manejo de errores si el archivo de entrada no se encuentra
        print(f'Lo siento, no se pudo encontrar el archivo "{input_file}".')

def main():
    # Solicita al usuario el nombre del archivo de texto a cifrar
    input_file = input("Introduce el nombre del archivo de texto (incluyendo la extensión .txt): ")
    # Solicita al usuario el desplazamiento para el cifrado
    desplazamiento = int(input("Introduce el desplazamiento para el cifrado (un número entero): "))
    # Define el nombre del archivo de salida, añadiendo "_cifrado" al nombre original
    output_file = f"{input_file.split('.')[0]}_cifrado.txt"
    
    # Llama a la función para cifrar el archivo
    cifrar_archivo(input_file, output_file, desplazamiento)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
