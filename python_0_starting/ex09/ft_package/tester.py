from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
print(count_in_list([1, 2, 3, 42, 42, 4, 5, 6, 42], 42))  # output: 3
