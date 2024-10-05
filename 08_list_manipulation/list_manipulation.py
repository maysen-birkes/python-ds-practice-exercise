def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)
        else:
            return None      
    elif command == "add":
        if location == "end":
            lst.append(value)
            return lst
        elif location == "beginning":
            lst.insert(0, value)
            return lst
        else:
            return None
    else:
        return None


lst_remove = [1, 2, 3]

# remove
    
print(list_manipulation(lst_remove, 'remove', 'end'))
print(list_manipulation(lst_remove, 'remove', 'beginning'))
print(f"Manipulated List: {lst_remove}")

lst_add = [1, 2, 3]

# add

print(list_manipulation(lst_add, 'add', 'beginning', 20))
print(list_manipulation(lst_add, 'add', 'end', 30))
print(f"Manipulated List: {lst_add}")

lst_invalid = [1, 2, 3]

# invalid

print(list_manipulation(lst_invalid, 'foo', 'end') is None)
print(list_manipulation(lst_invalid, 'add', 'dunno') is None)