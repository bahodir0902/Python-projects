
def image_info(dictionary):
    for values, keys in dictionary.items():
        if(keys == '' or values == ''):
            raise TypeError("Error, please try again to input the keys of dictionary!")
            return f"Image '{keys}' has id {values}"

'''
my_dict = {}
x = int(input("How many keys and value do you want in dictionary? "))
for i in range(x):
    key = input("Input the image id: ")
    value = input("Input the image title: ")
    my_dict[key] = value

try:
    print(image_info(my_dict))
except TypeError as error:
    print(error)
'''
my_dict = {'name': 'Bahodir', 'age': 18}
for key in my_dict:
    print(f"{key}: {my_dict[key]}")    
       

print("The program ended succesfully")
