def cifra_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char

    return resultado


def decifrar_cesar(texto, deslocamento):
    return cifra_cesar(texto, -deslocamento)


mensagem = input("Digite o texto: ")
shift = int(input("Digite o deslocamento (ex: 3): "))

criptografado = cifra_cesar(mensagem, shift)
print("Texto criptografado:", criptografado)

descriptografado = decifrar_cesar(criptografado, shift)
print("Texto descriptografado:", descriptografado)