#programme qui prend en entrée un message crypté par shifting et qui affiche chaque traduction possible avec la clé correspondante
input = input("Entrez le message crypté : ")
input = input.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for key in range(len(alphabet)):
    newAlphabet = alphabet[key:] + alphabet[:key]
    output = ""
    for i in range(len(input)):
        index = alphabet.find(input[i])
        if index < 0:
            output += input[i]
        else:
            output += newAlphabet[index]
    print("Key " + str(key) + ": " + output)


