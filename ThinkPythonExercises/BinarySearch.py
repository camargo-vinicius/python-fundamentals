def binary_search(list_words: list[str], item: str) -> int | None:

    loop = 0 # contador de loops

    # cria uma copia da lista de palavras
    new_list = list_words[:]

    while len(new_list) > 1:
        
        # print(f'Loop: {loop}\n')
        middle_index = len(new_list) // 2 if len(new_list) % 2 == 0 else (len(new_list) // 2) + 1

        # faz a divisão da lista new_list em duas partes, dependendo se a palavra buscada for menor ou maior que o item do meio da lista
        # se for menor, procura na primeira metade da lista
        # se for maior, procura na segunda metade
        # vão acontencendo divisoes sucessivas até que reste um único elemento
        if item < new_list[middle_index]:
            new_list = new_list[:middle_index]

        elif item > new_list[middle_index]:
            new_list = new_list[middle_index:]

        else:
            # aqui só terá um único elemento na lista, que deverá ser a palavra, caso ela existir
            return list_words.index(new_list[0])
            # print(f'Word {item} find at index {list_words.index(new_list[0])} using {loop} loops')
            # break

        loop += 1

    # else:
    #     print(f'Word not found. It required {loop} loops')

if __name__ == '__main__':
    with open('../words.txt') as file:
        words = file.read().split('\n')[:-1]

    words_test = ['ringing', 'zorillos', 'vinicius']

    for word in words_test:

        search = binary_search(words, word)

        if isinstance(search, int):
            print(f'{word} found at {search} index')

        else:
            print(f'{word} not found.')