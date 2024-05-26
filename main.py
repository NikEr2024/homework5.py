immutable_var_ = 1, 2, 'a', 'b'

print('Immutable tuple: ', immutable_var_)

#immutable_var_[0] = 3 Ошибка типа: объект «кортеж» не поддерживает назначение элементов

mutable_list_ = [1, 2, 'c', 'd']
mutable_list_[3] = 'Modified'
print('Mutable list: ', mutable_list_)