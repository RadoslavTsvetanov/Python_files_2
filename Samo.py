def print_only_6_grade(Source_file, arr):
    with open(Source_file, 'r', encoding="utf-8") as data:
        grades_to_display = []
        arr.append("Uchenici s 6:")
        file_lenght = 0
        for i in data:
            grades_to_display.append(i)
            file_lenght += 1
        for i in range(0, file_lenght, 1):
            if(grades_to_display[i][-2] == '6'):
                if(grades_to_display[i][1] == ' '):
                    print(grades_to_display[i][2:-2])
                    arr.append(grades_to_display[i][2:-2])
                else:
                    print(grades_to_display[i][3:-2])
                    arr.append(grades_to_display[i][3:-2])
