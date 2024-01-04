#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_1 = dir(hidden_4)
    names_2 = [name for name in names_1 if not name.startswith("__")]
    names_3 = sorted(names_2)
    for name in names_3:
        print(name)
