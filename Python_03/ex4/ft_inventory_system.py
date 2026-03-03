import sys

def ft_split(string: str):
    word: str = ""
    for char in string:
        if char == ":":
            
        else:
            word += char

def parse():
    argument: list = sys.argv[1:]
    if len(argument) < 1:
        print("Error: you must add at least one item !")
        sys.exit()
    else:
        for arg in argument:
            

if __name__ == "__main__":
    