peca1, nmr_peca1, vlr_uni1 = input().split()
peca2, nmr_peca2, vlr_uni2= input().split()

peca1 = int(peca1)
nmr_peca1 = int(nmr_peca1)
vlr_uni1 = float(vlr_uni1)

peca2 = int(peca1)
nmr_peca2 = int(nmr_peca2)
vlr_uni2 = float(vlr_uni2)

calc = nmr_peca1 * vlr_uni1 + nmr_peca2 * vlr_uni2

print(f"VALOR A PAGAR: {calc:.2f}")
