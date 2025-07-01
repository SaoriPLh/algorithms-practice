# def containsNearbyDuplicate(nums, k):
#     #vamos primero a checar que haya duplicados antes de verificar que cumplan la condicion

#     noDuplicados = set()

#     for i, numero in enumerate(nums):
#         if numero in noDuplicados:
#             #si ya esta el numero dentro del array osea si existe un duplicado vamos a obtener la posicion que seria

#             #aca quiero que en la posicion en la que vamos quiero restarla con la (posicion en la q esta el elemento duplicado + 1  ) para saber la distancia entre los dos 
#             if (i-noDuplicados <= k):
#                 return True
#             

#         noDuplicados.add(numero)

#     return False 


def containsNearbyDuplicate(nums, k):

    #diccionario para guardar los indices ya que truve un error al pensar que el set tenia indices 

    indices = {}

    for i, numero in enumerate(nums):
        if numero in indices:
            if i -indices[numero]<= k:
                return True
        indices[numero] = i
    
    return False