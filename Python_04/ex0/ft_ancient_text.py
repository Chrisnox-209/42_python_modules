def text_recovery(file_txt: str) -> None:
    print("RECOVERED DATA:")
    try:
        with open(file_txt, "r", encoding="utf-8") as content:
            print(content.read())
    except Exception as error:
        print(error)


if __name__ == "__main__":
    file_txt: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES- DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_txt}\nConnection established...\n")
    text_recovery(file_txt)
    print("\nData recovery complete. Storage unit disconnected.")
