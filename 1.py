k = int(input("Введите количество котлет, которые можно уместить в сковородке: ")) # не до конца понял какой смысл имеет наличие этой переменной, если
m = int(input("Введите время(в минутах), требуемое на обжарку котлеты с одной стороны: "))
n = int(input("Введите количество котлет: "))
time = (m*2)*n
if k > 32000 or m > 32000 or n > 32000:
    print("Значения k/m/n не должны превышать 32000")
    exit()
# elif n > k:
#   time = (m*2)*(n-k)
#   print(time)
# Условие не совсем полное, поэтому я и не до конца его понял. Если количество котлет превышает допустимое, то что тогда? Оставшиеся выбрасываются? Если нет, то это дополнительное условие и не нужно вовсе, ведь в любом случае будет считаться общее время, необходимое для жарки котлет, пусть даже в 2 или 3 захода
else:
    print(time)
