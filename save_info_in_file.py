def save_info_into_file(name, arr):
    with open(name, 'w', encoding="utf-8") as File:
        for i in arr:
            File.write(str(i))
            File.write('\n')
