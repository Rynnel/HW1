n = int(input("Введите число: "))  # вводим число n


if n % 10 == 1 and n % 100 != 11:  # если n заканчивается на 1, но не заканчивается на 11
    print(n, "korova")  
elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:  # если n заканчивается на 2, 3 или 4, но не заканчивается на 12, 13 или 14
    print(n, "korovy")  
else:  
    print(n, "korov")  

