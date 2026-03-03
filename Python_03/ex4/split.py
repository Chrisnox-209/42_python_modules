
def ft_split(chaine: str, char: str) -> list:
    list_mots: list = []
    mot: str = ""

    for lettre in chaine:
        if lettre == char:
            if mot != "":
                list_mots = list_mots + [mot]
                mot = ""
        else:
            mot += lettre

    if mot != "":
        list_mots = list_mots + [mot]
    return list_mots


if __name__ == "__main__":
    ma_str: str = "    Je    test    le   split   en    python     "
    char: str = " "
    print(ft_split(ma_str, char))
