# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]


def flatten(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))  # Eğer liste ise yine düzleştir.
        else:
            flattened_list.append(item)  # Liste değilse direk ekle.
    return flattened_list

# Test
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten(input_list)
print(output_list)


def reverse_nested(lst):
    reversed_list = []
    for item in reversed(lst):  # İlk olarak dıştaki listeyi ters çeviriyoruz.
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))  # Eğer liste ise içindekileri de ters çeviriyoruz.
        else:
            reversed_list.append(item)  # Liste değilse direk ekliyoruz.
    return reversed_list

# Test
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested(input_list)
print(output_list)
