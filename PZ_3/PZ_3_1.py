while True:
  try: # Обработчик исключений
    a = int(input('Введите число: ')) #ввод данных с клавиатуры
    if len(str(a)) == 3: #считает количество цифр в числе
      print('Данное число является нечетным трехзначным:', a%2 == 1 and a>=100 and a<=999) #Вывод данных на консоль и проверка истинности высказывания
      break #применяется для прерывания текущей итерации
    else:
      print('Вы ввели не целое положительное трёхзначное число!')
      double_var = input('Повторить ввод?("да"/"нет")') # повторный ввод данных
    if double_var.lower() in ['да']:
      continue #передаёт элемент управления в следующую итерацию ближайшего внешнего оператора
    else:
      print('Выполнение завершено')
      break #применяется для прерывания текущей итерации
  except ValueError: # проверка формата введенных данных
    print('Вы ввели не число!')
    double_var = input('Повторить ввод?("да"/"нет")') # повторный ввод данных
    if double_var.lower() in ['да']:
      continue #передаёт элемент управления в следующую итерацию ближайшего внешнего оператора
      print('Данное число является нечетным трехзначным:', a%2 == 1 and a>=100 and a<=999) #Вывод данных на консоль и проверка истинности высказывания
    else:
      print('Выполнение завершено')
      break #применяется для прерывания текущей итерации