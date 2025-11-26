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

student_name = input("\nEntrez le nom de l'étudiant : ")

if student_name in students : 
    print(f"\nNotes de {student_name} :\n")
    total = 0
    for matiere in students[student_name] :
     print(f"{matiere} : {students[student_name][matiere]}")
     
     total += students[student_name][matiere]
     length = len(students[student_name])

    moyenne = total/length
    print(f"Moyenne de {student_name} : {moyenne}")
else :
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
