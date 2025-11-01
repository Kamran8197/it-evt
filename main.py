students = {
    1: "Ramil",
    2: "Huseyn",
    3: "Aysel"
}

for id, name in students.items():
    print(id, ":", name)


id_input = int(input("Axtardığınız tələbənin id-sini daxil edin: "))

if id_input in students:
    print("Tələbə:", students[id_input])
else:
    print("Tapılmadı")


id_input = int(input("Silinəcək tələbənin id-sini daxil edin: "))

if id_input in students:
    del students[id_input]
    print("Tələbə silindi.")
else:
    print("Elə açar yoxdur.")

print("Yenilənmiş dictionary:", students)


id_input = int(input("Tələbənin id-sini daxil edin: "))
name_input = input("Tələbənin adını daxil edin: ")

students[id_input] = name_input  
print("Yenilənmiş dictionary:", students)


id_input = int(input("Tələbənin id-sini daxil edin: "))
name_input = input("Tələbənin adını daxil edin: ")

print("Dictionary-də elementlərin sayı:", len(students))

sorted_names = sorted(students.values())
print("Əlifba sırasına görə adlar:", sorted_names)

reversed_students = {name: id for id, name in students.items()}
print("Tərs dictionary:", reversed_students)

students = {
    "Aysel": 95,
    "Huseyn": 88,
    "Ramil": 76,
    "Leyla": 90
}

highest = max(students, key=students.get)
lowest = min(students, key=students.get)
average = sum(students.values()) / len(students)

print("Ən yüksək qiymət:", highest, "-", students[highest])
print("Ən aşağı qiymət:", lowest, "-", students[lowest])
print("Orta qiymət:", average)


