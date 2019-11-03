price1 = int(input())
price2 = int(input())
padenie = False
while price2 != 0:
    if padenie:
        if price1 > price2:
            prodazha = price2
            break
    else:
        if price1 < price2:
            kuplya = price2
            padenie = True
    price1 = price2
    price2 = int(input())
print(kuplya, prodazha, prodazha - kuplya)
