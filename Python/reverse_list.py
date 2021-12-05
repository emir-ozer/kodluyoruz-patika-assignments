'''
Kodluyoruz-Patika Pyhton Temel Eğitimi Kapsamında
Yapılan Bitirme Ödevidir.
'''
#Soru 2: Reverse List

input_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(x):
    x.reverse()
    for i in x:
        if type(i)==list:
            i.reverse()

reverse_list(input_list)
print(input_list)

