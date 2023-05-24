# Задача 47.
# У вас есть код, который вы не можете менять(так бывает, когда код в глубине программы и 
# используется множество раз и вы не хотите ничего сломать).
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# или любой другой список
# transformed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством использования функции transformation.
# Однако вы поняли,что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values

values = [1, 23, 42, 'asdrfg']
transformation = lambda x: x
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print ('ok')
else:
    print ('fail')