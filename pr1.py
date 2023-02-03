num_one = float (input ("Первое число = "))

while True:
    print ("Выберите действие: ")
    deistvie = input()

    if deistvie in ('-', '+','*',':','^'):

        if deistvie == '-':
            num_two = float(input ("Второе число = "))
            num_one = num_one - num_two
            print(num_one)
        
        if deistvie == '+':
            num_two = float(input ("Второе число = "))
            num_one = num_one + num_two
            print(num_one)
        
        if deistvie == '*':
            num_two = float(input ("Второе число = "))
            num_one = num_one * num_two
            print(num_one)
        
        if deistvie ==':':

            num_two = float(input ("Второе число = "))

            if num_two == 0:
                print("Делить на ноль нельзя!")
            elif num_two > 0:
                num_one = num_one / num_two
            print(num_one)

        if deistvie =='^':
            num_two = float(input ("Второе число = "))
            num_one = pow(num_one, num_two)
            print(num_one)

    else:
        print("Не работает... Кажется, ты что-то сделал не так.")