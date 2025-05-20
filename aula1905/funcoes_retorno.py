def validarEmail(email):
    if("@" in email and email.endswith(".com") and "gmail.com" in email):
        return True
    else:
        return False
    
if(validarEmail("g@hotmail.com")):
    print("Email válido!")

def somar(x, y):
    return (x + y)

resultado = somar(10, 5)
print(resultado)