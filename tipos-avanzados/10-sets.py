# Set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo)
# print(primer & segundo) # Devuelve los que se encuentren en los dos sets
# print(primer - segundo) # Devuelve los que no se encuentran en los dos sets, solo en el set izquierdo
print(primer ^ segundo) # Quita los que se encuentren en los dos sets y solo ponen los que no están en los dos sets
