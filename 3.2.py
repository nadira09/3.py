# # задача 2
#
# name,surname,year,city,email,number=input('введите имя: '),input('введите фамилию: '),input('введите год рождения: '),input('введите город: '),input('введите email: '),input('введите номер телефона: ')
def func_data(name,surname,year,city,email,number):
    print(name,surname,year,city,email,number)
func_data('Надира,','Ахметова,',2000,'Санкт-Петербург','sill.a@mail.ri','+78126164535')

# # сделать словарем
#
# # def my_func(**kparams):
# #     return kparams
# #
# # print(my_func(el_1=10, el_2=20, el_3="text"))
#
# # или
# # def my_func(v2,v1,v3):
# #     print(f'v2-{v2},v3-{v3},v1-{v1}')
# # my_func(v1=10,v2=11,v3=13)

# или
# # def my_func(**kwargs):
# #     return kwargs
# # print(my_func(el_1=10, el_2=20, el_3="text"))
# # Результат:
# # {'el_1': 10, 'el_2': 20, 'el_3': 'text'}