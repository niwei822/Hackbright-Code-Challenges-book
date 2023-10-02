n = 'oh hi there'.count('h')
print(n)

word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True

#The extend() method in Python does not return a new list. Instead, it modifies the original list in-place and returns None
my_list = [1, 2, '3', True]
my_list.extend([100, 200])
my_list.insert(2, '!!!')
print(my_list)

a = ' '.join(['hello', 'world'])
print(a)
b = 'hello'
c = 'there'
print(' '.join([b, c]))

basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

print([1,2,3].pop())
my_list.pop()
my_list.remove(2)
print(my_list)

alist = [1,2,5,3]
#Mutates list
alist.sort()
print(alist)
alist.sort(reverse=True)
print(alist)
alist.reverse()
print(alist)

#new list created
blist = [1,2,5,3]
new_bllist = sorted(blist)
print(new_bllist)

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

