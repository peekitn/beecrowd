nome = input()
slr_fixo = float(input())
tl_vendas = float(input())

bonus = tl_vendas * 0.15
total = slr_fixo + bonus

print(f"TOTAL = R$ {total:.2f}")