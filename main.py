from Samo import print_only_6_grade
from chetvorki import chetvorki
from sredno import sredno
from save_info_in_file import save_info_into_file
from getDate import date


def main():
    arr = []
    print_only_6_grade("data.txt", arr)
    chetvorki("data.txt", arr)
    a = sredno("data.txt", arr)
    date(arr)
    save_info_into_file("newFile.txt", arr)
    print("__________________________________")
    print(arr)


main()
