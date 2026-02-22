ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Brazil!")
ft_set = {"Hello", "São Paulo!"}
ft_dict = {"Hello": "42SP!"}

# this is needed to order the set
# this DS is converted to a hash to fast lookup, so it becomes unordered
ordered_set = sorted(ft_set)

if __name__ == "__main__":

    print(ft_list)
    print(ft_tuple)
    print(ordered_set)
    print(ft_dict)
