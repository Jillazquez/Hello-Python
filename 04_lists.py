### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1,2,3,4,5]

print(len(my_list))

my_other_list = [22,1.89,"Juan Manuel","Illazquez"]

print(my_other_list)
print(type(my_list))

print(my_list[1])
print(my_list[2])
print(my_list[-1])

edad,altura,nombre,apellido = my_other_list

print(edad)

print(my_list+my_other_list)

my_list = "Hola Python" #Ahora my_list es string
#print(my_list+my_other_list) TypeError no se puede concatenar str y list


my_other_list.append("Añado valores al final de la lista")
my_other_list.insert(1, "Azul")
my_other_list.remove("Azul")

del my_other_list[1]

print(my_other_list)
print(my_list)

my_list=my_other_list.copy()
print(my_list)

# print in console in python
