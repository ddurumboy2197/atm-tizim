class ATM:
    def __init__(self):
        self.balans = 0
        self.pul = 0

    def pul_yechish(self, summa):
        if summa > self.balans:
            print("Sizning balansi yetarli emas.")
        else:
            self.balans -= summa
            self.pul += summa
            print(f"Siz {summa} so'm yechdingiz.")

    def balansni_ko'rsatish(self):
        print(f"Sizning balansi {self.balans} so'm.")

    def pul_qo'shish(self, summa):
        self.balans += summa
        self.pul += summa
        print(f"Siz {summa} so'm qo'shdingiz.")

    def pul_yechish_karta(self, summa):
        if summa > self.balans:
            print("Sizning balansi yetarli emas.")
        else:
            self.balans -= summa
            self.pul += summa
            print(f"Siz {summa} so'm yechdingiz.")

    def balansni_ko'rsatish_karta(self):
        print(f"Sizning balansi {self.balans} so'm.")

    def pul_qo'shish_karta(self, summa):
        self.balans += summa
        self.pul += summa
        print(f"Siz {summa} so'm qo'shdingiz.")


atm = ATM()

while True:
    print("1. Balansni ko'rsatish")
    print("2. Pul qo'shish")
    print("3. Pul yechish")
    print("4. Chiqish")
    print("5. Balansni ko'rsatish karta")
    print("6. Pul qo'shish karta")
    print("7. Pul yechish karta")
    print("8. Chiqish karta")

    savol = input("Izoh: ")

    if savol == "1":
        atm.balansni_ko'rsatish()
    elif savol == "2":
        summa = int(input("Qo'shish summasini kiriting: "))
        atm.pul_qo'shish(summa)
    elif savol == "3":
        summa = int(input("Yechish summasini kiriting: "))
        atm.pul_yechish(summa)
    elif savol == "4":
        break
    elif savol == "5":
        atm.balansni_ko'rsatish_karta()
    elif savol == "6":
        summa = int(input("Qo'shish summasini kiriting: "))
        atm.pul_qo'shish_karta(summa)
    elif savol == "7":
        summa = int(input("Yechish summasini kiriting: "))
        atm.pul_yechish_karta(summa)
    elif savol == "8":
        break
    else:
        print("Izoh: Xato savol.")
