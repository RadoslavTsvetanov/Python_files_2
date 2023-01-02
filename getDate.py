from datetime import date
from datetime import time
today = date.today()


def date(arr):
    now = today.strftime("%d/%m/%Y %H:%M:%S")
    clock = time()
    arr.append(str(now))
