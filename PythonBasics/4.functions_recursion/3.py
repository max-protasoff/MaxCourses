input_list = ['2018-01-01', 'yandex', 'cpc', 100]

def list_to_dict(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return {lst[0] : list_to_dict(lst[1:])}

print(list_to_dict(input_list))
