# Задача настолько простая, что комментарии излишни. Программа выводит YES, если точки находятся в одной координатной четверти, если же не в одной - выводит NO
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("YES")
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("YES")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("YES")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("YES")
else:
    print("NO")