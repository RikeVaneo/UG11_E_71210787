import random

def cekHasil(pilihan):
    jawaban = 0
    inputansalah = False
    stringsoal = ""
    if pilihan == "1":
        angka1 = random.randint(20, 50)
        angka2 = random.randint(20, 50)
        choice = random.choice(operasi)
        stringsoal = f"{angka1} {choice} {angka2}"
        print("Berapakah hasil dari ", angka1, choice, angka2)
        if choice == '-':
            jawaban = angka1 - angka2
        elif choice == '+':
            jawaban = angka1 + angka2
        elif choice == '/':
            jawaban = angka1 / angka2
        elif choice == '*':
            jawaban = angka1 * angka2
    elif pilihan == "2":
        angka1 = random.randint(20, 70)
        angka2 = random.randint(20, 70)
        angka3 = random.randint(20, 70)
        choice = random.choice(operasi)
        choice2 = random.choice(operasi)
        stringsoal = f"{angka1} {choice} {angka2} {choice2} {angka3}"
        print("Berapakah hasil dari ", angka1, choice, angka2, choice2, angka3)
        if choice == '-':
            if choice2 == '-':
                jawaban = angka1 - angka2 - angka3
            elif choice2 == '+':
                jawaban = angka1 - angka2 + angka3
            elif choice2 == '/':
                jawaban = angka1 - angka2 / angka3
            elif choice2 == '*':
                jawaban = angka1 - angka2 * angka3
        elif choice == '+':
            if choice2 == '-':
                jawaban = angka1 + angka2 - angka3
            elif choice2 == '+':
                jawaban = angka1 + angka2 + angka3
            elif choice2 == '/':
                jawaban = angka1 + angka2 / angka3
            elif choice2 == '*':
                jawaban = angka1 + angka2 * angka3
        elif choice == '/':
            if choice2 == '-':
                jawaban = angka1 / angka2 - angka3
            elif choice2 == '+':
                jawaban = angka1 / angka2 + angka3
            elif choice2 == '/':
                jawaban = angka1 / angka2 / angka3
            elif choice2 == '*':
                jawaban = angka1 / angka2 * angka3
        elif choice == '*':
            if choice2 == '-':
                jawaban = angka1 * angka2 - angka3
            elif choice2 == '+':
                jawaban = angka1 * angka2 + angka3
            elif choice2 == '/':
                jawaban = angka1 * angka2 / angka3
            elif choice2 == '*':
                jawaban = angka1 * angka2 * angka3
    elif pilihan == "3":
        angka1 = random.randint(20, 100)
        angka2 = random.randint(20, 100)
        angka3 = random.randint(20, 100)
        angka4 = random.randint(20, 100)
        choice = random.choice(operasi)
        choice2 = random.choice(operasi)
        choice3 = random.choice(operasi)
        stringsoal = f"{angka1} {choice} {angka2} {choice2} {angka3} {choice3} {angka4}"
        print("Berapakah hasil dari ", angka1, choice, angka2, choice2, angka3, choice3, angka4)
        if choice == '-':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = angka1 - angka2 - angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 - angka2 - angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 - angka2 - angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 - angka2 - angka3 * angka4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = angka1 - angka2 + angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 - angka2 + angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 - angka2 + angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 - angka2 + angka3 * angka4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = angka1 - angka2 / angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 - angka2 / angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 - angka2 / angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 - angka2 / angka3 * angka4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = angka1 - angka2 * angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 - angka2 * angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 - angka2 * angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 - angka2 * angka3 * angka4
        elif choice == '+':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = angka1 + angka2 - angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 + angka2 - angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 + angka2 - angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 + angka2 - angka3 * angka4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = angka1 + angka2 + angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 + angka2 + angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 + angka2 + angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 + angka2 + angka3 * angka4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = angka1 + angka2 / angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 + angka2 / angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 + angka2 / angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 + angka2 / angka3 * angka4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = angka1 + angka2 * angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 + angka2 * angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 + angka2 * angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 + angka2 * angka3 * angka4
        elif choice == '/':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = angka1 / angka2 - angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 / angka2 - angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 / angka2 - angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 / angka2 - angka3 * angka4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = angka1 / angka2 + angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 / angka2 + angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 / angka2 + angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 / angka2 + angka3 * angka4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = angka1 / angka2 / angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 / angka2 / angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 / angka2 / angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 / angka2 / angka3 * angka4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = angka1 / angka2 * angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 / angka2 * angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 / angka2 * angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 / angka2 * angka3 * angka4
        elif choice == '*':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = angka1 * angka2 - angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 * angka2 - angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 * angka2 - angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 * angka2 - angka3 * angka4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = angka1 * angka2 + angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 * angka2 + angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 * angka2 + angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 * angka2 + angka3 * angka4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = angka1 * angka2 / angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 * angka2 / angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 * angka2 / angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 * angka2 / angka3 * angka4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = angka1 * angka2 * angka3 - angka4
                elif choice2 == '+':
                    jawaban = angka1 * angka2 * angka3 + angka4
                elif choice2 == '/':
                    jawaban = angka1 * angka2 * angka3 / angka4
                elif choice2 == '*':
                    jawaban = angka1 * angka2 * angka3 * angka4
    else:
        print("inputan salah")
        inputansalah = True
    if not inputansalah:
        jawabananda = float(input("Masukkan jawaban anda: "))
        if (jawaban == jawabananda or jawabananda == ("%.3f" % jawaban)):
            print("Jawaban anda benar !")
        else:
            print("Jawaban Anda Masih Salah")
            print("Hasil dari ", stringsoal, " = %.3f" % jawaban)


operasi = ['+','-','/','*']
print("======Program test aritmatika dasar======")
print("Pilihan level yang tersedia :")
print("1. Easy")
print("2. Medium")
print("3. Hard")
pilihan=str(input("Masukkan tingkatan yang ingin anda coba :"))
cekHasil(pilihan)



