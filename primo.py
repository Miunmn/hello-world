num = int (input ("Ingresar numero positivo: \n"))
if num>1:
  for i in range (2,num):
    if (num%i)==0:
      print(num, "No es numero primo \n\n")
      break
    else: 
        print(num,"Es numero primo")
else: 
    print(num, "No es primo")
