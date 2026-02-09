def garden_operations(action: str) -> None:
    if action == "all":
        try:
            1 / 0
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")

    try:
        if action == "value":
            int("abc")
        elif action == "zero":
            1 / 0
        elif action == "file":
            open("missing.txt")
        elif action == "key":
            dico = {"test1": "nothing1",
                    "test2": "nothing2"}
            dico["test3"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    except KeyError:
        print("Caught KeyError: 'test3'\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    garden_operations("value")
    print("Testing ZeroDivisionError...")
    garden_operations("zero")
    print("Testing FileNotFoundError...")
    garden_operations("file")
    print("Testing KeyError...")
    garden_operations("key")
    print("Testing multiple errors together...")
    garden_operations("all")


if __name__ == "__main__":
    test_error_types()
