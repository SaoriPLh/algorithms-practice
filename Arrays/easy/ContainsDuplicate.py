

def containsDuplicate(array):
    
    vistos  = set() 
    for n in array:
        if n in vistos:
            return True
        vistos.add(n)
    return False



