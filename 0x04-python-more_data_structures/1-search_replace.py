#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search_list = []
    for i in my_list:
        if i == search:
            search_list.append(replace)
        else:
            search_list.append(i)
    return search_list
