class Contact:
    def __init__(self, name, surname, phone_num, fav=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        self.fav = fav
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if str(self.fav) == 'False':
            str_fav = 'No'
        else:
            str_fav = 'Yes'

        out_str_kwargs = ''
        for key, value in self.kwargs.items():
            out_str_kwargs = out_str_kwargs + '\t' + key + ': ' + value + '\n'

        out_str_args = ''
        for value in self.args:
            out_str_args = '\t' + out_str_args + value

        return ('Name: ' + self.name + '\n' +
                'Surname: ' + self.surname + '\n' +
                'Phone: ' + self.phone_num + '\n' +
                'Favourites: ' + str_fav + '\n' +
                'Additional info: ' + '\n' +
                    out_str_kwargs + out_str_args)
