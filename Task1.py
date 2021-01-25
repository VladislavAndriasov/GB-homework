import sys
production, rate, bonus = sys.argv[1:]
ZP = int(production) * int(rate) + int(bonus)
print(f' Заработная плата: {ZP}')
