def external(name):
    dic = {'Roger': 47, 'Mateus': 42, 'Marco': 40}
    def internal(name):
        idade = dic[name]
        print(f'{name} tem {idade} anos')
    return internal(name)

external("Roger")
