#El siguiente codigo simula la operacion de un cajero automatico
#************************Operaciones**************************
# 1. Consultar saldo
# 2. Retirar dinero
# 3. Depositar dinero
# 4. Salir de cajero
# manejo de saldos en tipo de datos "float"


print ('ATM City')

balance =29000.0 # saldo inicial
goOut= False  # esta variable es para controlar si el usuario quiere salir del cajero

# Bucle While que se ejecuta mientras el usuario no seleccione la opcion de "salir"
while not goOut:
    print(f'''Operations you can perform:
            1. Check balance
            2. Withdraw
            3. deposit
            4. exit''')

    option =int(input("Select a option: ")) # aqui el usuario selecciona una opcion

    if option ==1: # Aqui el usuario selecciona consultar el saldo
        print(f'Your current balance is: {balance:.2f}\n')
    elif option ==2: # Aqui el usuario selecciona retirar dinero
        withdraw = float(input(f'Enter the amount to withdraw:'))

        # Esta validacion es para verificar que el monto a retirar sea menor al saldo disponible
        if withdraw < balance:
            balance -= withdraw  # Se resta el monto retirado del saldo actual
            print(f'Your current balance is: {balance:.2f}\n')
        else:
            print(f'Your current balance is not sufficient')
    elif option==3: # Aqui el usuario deposita dinero
        deposit=float(input(f'Enter the amount to deposit: $'))
        balance += deposit # Se suma el monto depositado al saldo actual
        print(f'Your current balance is $: {balance:.2f}\n')
    elif option==4: # Aqui el usuario selecciona la opcion para salir
        print('Coming out of the ATM. Bye!!!')
        goOut=True # Se cambiar el valor de la variable para salir del bucle


