nit=input("Ingrese nit: ")

mtr1=int(nit[0])*41
mtr2=int(nit[1])*37
mtr3=int(nit[2])*29
mtr4=int(nit[3])*23
mtr5=int(nit[4])*19
mtr6=int(nit[5])*17
mtr7=int(nit[6])*13
mtr8=int(nit[7])*7
mtr9=int(nit[8])*3

suma=mtr1+mtr2+mtr3+mtr4+mtr5+mtr6+mtr7+mtr8+mtr9

modulo11=suma % 11
modulo11m=11-modulo11
if modulo11 <= 2:
    print(nit,"-",modulo11)
else:
    print(nit,"-",modulo11m)


