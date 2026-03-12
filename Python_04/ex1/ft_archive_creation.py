
def archive_creation(file_name: str) -> None:
    print(f"Initializing new storage unit: {file_name}")
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("[ENTRY 001] New quantum algorithm discovered\n")
            file.write("[ENTRY 002] Efficiency increased by 347%\n")
            file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("Storage unit created successfully...\n")
        return True
    except Exception as error:
        print(error)
        return False


def reading_archive(file_name: str) -> bool:
    print("Inscribing preservation data...")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read())
        return True
    except Exception as error:
        print(error)
        return False


if __name__ == "__main__":
    file_name: str = "new_discovery.txt"
    print("=== CYBER ARCHIVES- PRESERVATION SYSTEM ===\n")
    if archive_creation(file_name) and reading_archive(file_name):
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
