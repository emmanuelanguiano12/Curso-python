def eliminarEspacios(texto):
    res = ""
    for char in texto:
        res += char
    return res.strip().replace(" ", "").lower()

# print("Abba", es_palindromo("Abba"))

def reverse(text):
    texto_al_reves = ""
    for char in text:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo(text):
    text = eliminarEspacios(text)
    reverse_word = reverse(text)
    return text == reverse_word

print("abba", es_palindromo("abba"))
print("Emmanuel", es_palindromo("Emmanuel"))
print("somos o no somos", es_palindromo("somos o no somos"))