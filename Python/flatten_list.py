'''
Kodluyoruz-Patika Pyhton Temel Eğitimi Kapsamında
Yapılan Bitirme Ödevidir.
'''
#Soru 1: Flatten List

input_list =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = []


def flatten_list(x):
    for element in x:
        if type(element) == list:
            flatten_list(element)
        else:
            output_list.append(element)
    
flatten_list(input_list)
print(output_list)
