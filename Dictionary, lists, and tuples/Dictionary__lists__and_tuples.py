"""
cars_brand = ['Mercedes', 'BMW', 'Audi', 'Ferrari']
cars_models = [' Amg One', ' X5M', ' R8', ' F8 Tributo']
cars_full = [brand + model for brand, model in zip(cars_brand, cars_models)]
print("You have these cars in your garage: ", cars_full)
cars_price = [1_500_000, 85_000, 60_000, 2_200_000]
cars_full.append("Lamborghini Gallardo")
cars_price.append(180_000)

total_price = dict(zip(cars_full, cars_price))

print(total_price)

total_price.update({"Koenigsegg Jesko":2_500_000, "Pagani Huayra R": 1_400_00})

print("You have just bought these cars: ", total_price,'\n')

print(total_price.get("Mercedes Amg One")) # gets the value of the key
student_names = ['Bahodir', 'Aziz', 'Asror']
ages = [ 18, 17,17]
student_ages = dict(zip(student_names,ages))
print('\n',student_ages)

# Inner dictionaries
works_of_art = {'The_Starry_Night': {'author': 'Van Gogh', 'year': 1889, 'style': 'post-impressionist'},
                'The_Birth_of_Venus': {'author': 'Sandro Botticelli', 'year': 1480, 'style': 'renaissance'},
                'Guernica': {'author': 'Pablo Picasso', 'year': 1937, 'style': 'cubist'},
                'American_Gothic': {'author': 'Grant Wood', 'year': 1930, 'style': 'regionalism'},
                'The_Kiss': {'author': 'Gustav Klimt', 'year': 1908, 'style': 'art nouveau'}}

print(works_of_art)

my_morotbike = {'brand' : 'Ducatti', 'engine_volume': 1.6, 'price': 25000, 'manufactured_year': 2017}
other_morotbike = {'manufactured_year': 2017, 'engine_volume': 1.6, 'price': 25000,'brand' : 'Ducatti'}
print(my_morotbike == other_morotbike) # True, because the order of keys and values in dictionary doesn't matter!!!
print(my_morotbike['brand']) # Ducatti
my_morotbike['price'] = 20000 # changing the value of key
print(my_morotbike)
"""
 # Task 1
# my_dict = {}
# for i in range(3):
#     temp = input("Enter the key of dictionary " + str(i + 1) + ': ')
#     value = input("Enter the value of dictionary " +  str(i + 1) + ': ')
#     my_dict[temp] = value
    
# print(my_dict)

# Task 2

# my_set = {1,2,5,8,9,7,8,93}
# my_set.add(3)
# new_set = {1,3,6,7,4,53,56}
# intersection_set = my_set.intersection(new_set)
# print(intersection_set)

# Task 3


def merge_list_to_dict(lst1, lst2):
    new_dict_foo = dict(zip(lst1, lst2))
    return new_dict_foo


foo_lst1 = list(input("Enter a list 1: "))
foo_lst2 = list(input("Enter a list 2: "))

if(True):
    raise TypeError("What the fuck!")    
print(merge_list_to_dict(foo_lst1, foo_lst2))



