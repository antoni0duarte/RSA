## Valores por região ##
  ## P= 5kg / M= 7kg ##

print("########### GRUPOS ############")
print("# GRUPO 1 = PE/PB/AL/SE/BA/TO #")
print("# GRUPO 2 = AC/AM/RR/RO/MT/AP #")
print("# GRUPO 3 = AC/AM/RR/RO/MT/AP #")
print("# GRUPO 4 = AC/AM/RR/RO/MT/AP #")
print("###############################")

group1_p = 23.40

group_select = int(input("Selecione seu grupo:\n"))

box_size = int(input("Você vai usar mais de um tamanho de caixa?\n"))
if box_size == 1:
  box = True
else:
  box = False
  amout_box = int(input("Quantas caixas?\n"))
  size = int(input("Qual tamanho?\n1 = P / 2 = M\n"))
  
