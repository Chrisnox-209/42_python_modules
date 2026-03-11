
def extraction(file_extraction: str) -> bool:
    print("Initiating secure vault access..")
    try:
        with open(file_extraction, "r", encoding="utf-8") as content:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(content.read())
            print()
            return True
    except Exception as error:
        print(error)
        return False


def preservation(file_preservation: str) -> bool:
    string: str = "[CLASSIFIED] New security protocols archived\n"
    try:
        with open(file_preservation, "a", encoding="utf-8") as content:
            print("SECURE PRESERVATION:")
            content.write(string)
        print(f"{string}Vault automatically sealed upon completion\n")
        return True
    except Exception as error:
        print(error)
        return False


if __name__ == "__main__":
    file_extraction: str = "classified_data.txt"
    file_preservation: str = "security_protocols.txt"
    if extraction(file_extraction) and preservation(file_preservation):
        print("All vault operations completed with maximum security.")
