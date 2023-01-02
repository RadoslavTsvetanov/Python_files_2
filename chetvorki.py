def chetvorki(File, arr):
    with open(File, 'r', encoding="utf-8") as data:
        grades_to_display = []
        file_lenght = 0
        for i in data:
            grades_to_display.append(i)
            file_lenght += 1
        chetvorki = 0
        for i in range(0, file_lenght, 1):
            if(grades_to_display[i][-2] == '4'):
                chetvorki += 1
        print(f"Uchenici s chevorki:{chetvorki}")
        arr.append(f"Uchenici s chevorki:{chetvorki}")
