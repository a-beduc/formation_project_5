def main():
    students = {
        'Alice': {
            'Mathematiques': 90,
            'Francais': 80,
            'Histoire': 95
        },
        'Bob': {
            'Mathematiques': 75,
            'Francais': 85,
            'Histoire': 70
        },
        'Charlie': {
            'Mathematiques': 88,
            'Francais': 92,
            'Histoire': 78
        }
    }

    student_name = input("Entrez le nom de l’étudiant : ").capitalize()
    if student_name in students.keys():
        print(f"Notes de {student_name}")
        for key, value in students[student_name].items():
            print(f"{key}: {value}")
        grades_sum = sum(students[student_name].values())
        average = grades_sum / len(students[student_name])
        print(f"Moyenne de {student_name} : {round(average, 2)}")
    else:
        print(f"L'étudiant {student_name} n'existe pas dans la liste.")


if __name__ == '__main__':
    main()
