def square(a):
    try:
        return a * a
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None


def main():
    a = -4.046046
    b = 'a'
    c = [4, 6]
    d = {"a": 12}
    print(square(a))
    print(square(b))
    print(square(c))
    print(square(d))


if __name__ == '__main__':
    main()
