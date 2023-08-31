def kelas(th):
    if th > 0:
        print("Kelas kamu ada di ", th)
        kelas(th - 1)
    else:
        print("Kamu telah mencapai inti bumi.")


kelas(5)
