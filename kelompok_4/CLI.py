from logika import is_prima

if __name__ == "__main__":
    print("=== ~~~ CLI CEK BILANGAN PRIMA ~~~ ===")

    try:
        angka = int(input("Masukkan angka untuk dicek: "))

        if is_prima(angka):
            print(f"{angka} Q_Q adalah bilangan prima :)")
        else:
            print(f"{angka} Q_Q bukan bilangan prima:P")

    except ValueError:
        print("Input harus berupa angka...")
