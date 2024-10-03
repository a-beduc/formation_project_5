def log_decorator(func):
    print("Message before function.")
    func()
    print("Message after function.")


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


def main():
    function_test()


if __name__ == '__main__':
    main()
