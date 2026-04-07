texto = "  WiLlIAn dOS  SAntOs  lIMA  caMpOS  "

print(texto)

texto = texto.strip().upper().replace("  ", " ")

print(texto)

#upper => Deixa tudo em maiusculo
#lower => Deixa tudo em minusculo
#strip => Remove os espaços nos começo e no fim da string
#replace => Substitui palavras ou até mesmo espaços no texto