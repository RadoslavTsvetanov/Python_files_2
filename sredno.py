def sredno(Source_file, arr):
    with open(Source_file, 'r', encoding="utf-8") as data:
        grades_to_display = []
        file_lenght = 0
        sredno = 0
        for i in data:
            grades_to_display.append(i)
            file_lenght += 1
        for i in range(0, file_lenght, 1):
            sredno += int(grades_to_display[i][-2])
        print(sredno / file_lenght)
        arr.append(sredno / file_lenght)
        if(sredno / file_lenght) > 4.5:
            arr.append("lesno e")
        else:
            arr.append("trudno e")
