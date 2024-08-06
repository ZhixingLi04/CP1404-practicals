# #
# # names = ["Ada", "Alan", "Bill", "John"]
# #
# #
# # print(",".join(names))
# #
# # while True:
# #
# #     names_to_remove = input("Who do you want to remove? (or type 'exit' to stop) ")
# #
# #     if names_to_remove.lower() == 'exit':
# #         break
# #     try:
# #         if names_to_remove in names:
# #             names.remove(names_to_remove)
# #             print(f"{names_to_remove} has been removed.")
# #         else:
# #             print(f"{names_to_remove} is not in the list.")
# #     except:
# #         print("error")
# #     print("Updated names: " + ", ".join(names))
#
#
# # print(names)
#
#
# # things =[True,1.2,"Good",[1,10]]
# # print(things[-2])
# # print("%".join([things[2][1:-1]]))
# # print([str(t)[0] for t in things])
# # print([len(str(t)) for t in things])
# # print([t for t in things if type(t)in(float,int)])
# # print([t for t in things if isinstance(t, int)])
#
# # with open("number.txt", "r") as input_file:
# #     numbers = input_file.readlines
# #     sum_of_number = 0
# #     for number in numbers:
# #         sum_of_number += float(number)
# #     print(f"Total sum of number is {sum_of_number}")
#
#
#
# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
#
# def get_numbers():
#     input_str = input("Enter numbers separated by commas: ")
#     number_list = [float(num.strip()) for num in input_str.split(',')]
#     return number_list
#
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#
#
# def display_numbers(numbers):
#     output = '..'.join(str, numbers)
#     print(output)
#
#
# main()
#

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
def print_names_with_values(data):
    for i in data:
        name, value = i
        print(f"{name}={value}")


print_names_with_values(data)

