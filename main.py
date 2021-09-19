num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69 , 113, 166]
runs = 0
odd = []



while len(odd) < 5:
    if num_list[runs] %2 != 0:
        odd.append(num_list[runs])
    runs+=1

sum_odds = sum(odd)      
print(f"La cantidad de números impares es: {runs} y La suma total de los números impares es: {sum_odds}")