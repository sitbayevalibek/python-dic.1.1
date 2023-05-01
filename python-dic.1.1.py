# restoran menyusini lug'at ko'rinishida tuzamiz
menu = {"lag'mon": 15000, 'manti': 30000, 'shashlik': 25000, 'osh': 18000, 'norin': 16000, 
        'somsa': 8000, 'chuchvara': 12000, 'kabob': 22000, 'lavash': 27000, "sho'rva": 14000}

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

buyurtma_miqdorlari = []
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
        buyurtma_miqdorlari.append(menu[buyurtma])
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")

if len(buyurtma_miqdorlari) > 0:
    jami_hisob = sum(buyurtma_miqdorlari)
    print(f"Sizning jami hisobingiz {jami_hisob} so'm.")

