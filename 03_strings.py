### Strings ###

my_string = "Mi otro String"
my_other_string = "Mi otro SString"

print(len(my_string))
print(len(my_other_string))

print(my_string+" "+my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_new_tab_string = "Este es un String\tcon tabulacion"
print(my_new_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

# Formateo

name,surname,age = "Juan Manuel","Illazquez",22

print("Mi nombre es %s %s y mi edad es %d"%(name,surname,age))
print("Mi nombre es "+name+" "+surname+" y mi edad es "+str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(e)

# Division

language_slice = language[1:3]
print(language_slice)

#Reverse 

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("p"))
