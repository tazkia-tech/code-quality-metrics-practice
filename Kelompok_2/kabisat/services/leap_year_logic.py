def is_leap(year):
    if year % 400 == 0:
        return "tahun kabisat"
    if year % 100 == 0:
        return "bukan tahun kabisat"
    if year % 4 == 0:
        return "tahun kabisat"
    return "bukan tahun kabisat"
