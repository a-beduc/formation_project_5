def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


def main():
    # Exemple d'utilisation de la fonction
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print("La moyenne est :", average)


if __name__ == "__main__":
    main()
