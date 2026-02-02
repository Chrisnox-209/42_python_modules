days = input("Days until harvest: ")


def ft_count_harvest_recursive(days):

    ft_count_harvest_recursive_helper(days, 0)
    print("Harvest time!")


def ft_count_harvest_recursive_helper(days, i):
    if i >= int(days):
        return
    print(f"Day {i + 1}")
    ft_count_harvest_recursive_helper(days, i + 1)
