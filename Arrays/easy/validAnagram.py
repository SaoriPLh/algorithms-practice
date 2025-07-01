def isAnagram(s, t):
    diccionarioT = {}
    for letra in t:
        if letra in diccionarioT:
            diccionarioT[letra] += 1
        else:
            diccionarioT[letra] = 1

    diccionarioS = {}
    for letra in s:
        if letra in diccionarioS:
            diccionarioS[letra] += 1
        else:
            diccionarioS[letra] = 1

    return diccionarioS == diccionarioT
