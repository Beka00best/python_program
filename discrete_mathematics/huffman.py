#! /usr/bin/env python
# -*- coding: utf-8 -*-
string = input('Enter the text если питон версии выше 3.7.8: ') #ввод    :)

text = []
for x in string:					#ввод массив до точки 
	if x != '.':
		text.append(x)
	else:
		break

if len(text) == 0:					#если ничего не ввели выход
	exit(0)

if len(text) == 1:					#если слово из одного символа
	print (" Symbol | Freq  | Huffman code ")
	print ("----------------------------------") 
	print("%-6r | %5d | %15d |" %(text[0], 1, 0))
	print ("----------------------------------")
	print(0)
	exit(0)

l = len(text)
k = 0
i = 0
c = text[0]
for ch in text:
    if c == text[i]:
        k = k + 1
    i = i + 1
if k == l:
    print (" Symbol | Freq  | Huffman code ")
    print ("----------------------------------") 
    print("%-6r | %5d | %15d |" %(text[0], 1, 0))
    print ("----------------------------------")
    print(0)
    exit(0)

set_text = set(text)
Frequency = [(text.count(char), char) for char in set_text]				#наша частота
Frequency = sorted(Frequency)

def make_tree(Frequency):
    while len(Frequency) > 1:
        getTwo = Frequency[0:2] 										# взять по два для конкатенации
        other = Frequency[2:] 											#остальное
        combFreq = getTwo[0][0] + getTwo[1][0] 							# комбинация freq
        Frequency = other + [(combFreq,getTwo)] 						# добавить в конец
        Frequency = sorted(Frequency, key=lambda x: x[0]) 				# сортировка 
    return Frequency[0]

def cutTree (tree) :
    ch = tree[1] 														# Нужно взять только буквы без цифр 
    if type(ch) is str: 													# Если строка
        return ch 														
    else: 
        return (cutTree(ch[0]), cutTree(ch[1]))							# разделим на лево и право

dict_haf = {}

def haf_cod (node, binst=''):											#коды букв
    global dict_haf
    if type(node) is str:
        dict_haf[node] = binst                
    else:                                
        haf_cod(node[0], binst + "0")    		
        haf_cod(node[1], binst + "1")
		
def textHaf(text):														#целый код хаффмана 
	global dict_haf
	comp_res = ''
	for ch in text:
		comp_res = comp_res + dict_haf[ch]
	return comp_res

tree = make_tree(Frequency)
tre = cutTree(tree)
haf_cod(tre)
textByHaf = textHaf(text)
Frequency = reversed(Frequency)											#Переворот 
print (" Symbol | Freq  | Huffman code ")
print ("----------------------------------")
for frequen, symbol in Frequency:
    print (" %-6r | %5d | %15s |" % (symbol, frequen, dict_haf[symbol]))
print ("----------------------------------")
print("".join(text))
print(textByHaf)
print('Длина = ' + str(len(textByHaf)))
