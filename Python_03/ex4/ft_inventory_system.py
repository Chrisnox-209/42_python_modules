import sys

def ft_split(string: str):
    dico = {}
    cle: str = ""
    valeur: str = ""
    flag_cle = 0
    end = chaine[len(chaine) - 1]
    for lettre in chaine:
        if lettre == ":":
            if cle != "" and flag_cle == 0:
                flag_cle = 1
        elif flag_cle == 0:
            cle += lettre
        elif flag_cle == 1:
                valeur += lettre
    dico[cle] = valeur
    return dico

def parse():
    argument: list = sys.argv[1:]
    if len(argument) < 1:
        print("Error: you must add at least one item !")
        sys.exit()
    else:
        for arg in argument:


if __name__ == "__main__":
