
def lost_file(file_name: str) -> bool:
    try:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        with open(file_name, "r", encoding="utf-8") as content:
            print(content.read())
        return True
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        return False
    except Exception as error:
        print(error)
        return False
    finally:
        print("STATUS: Crisis handled, system stable\n")


def permission_file(file_name: str) -> bool:
    try:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        with open(file_name, "r", encoding="utf-8") as content:
            print(content.read())
        return True
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        return False
    except Exception as error:
        print(error)
        return False
    finally:
        print("STATUS: Crisis handled, security maintained\n")


def good_file(file_name: str) -> bool:
    try:
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        with open(file_name, "r", encoding="utf-8") as content:
            print(f"SUCCESS: Archive recovered - ''{content.read()}''")
            return True
    except (PermissionError, FileNotFoundError):
        print("RESPONSE: Security protocols deny access or Archive "
              "not found in storage matrix")
        return False
    except Exception as error:
        print(error)
        return False
    finally:
        print("STATUS: Normal operations resumed\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    if (not lost_file("lost_archive.txt")
        and not permission_file("classified_vault.txt")
            and good_file("standard_archive.txt")):
        print("All crisis scenarios handled successfully. Archives secure.")
