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

#Tuple unpacking allows you to assign each item in a collection to a variable.
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

x, y = [1, 2]
x, y = y, x
print(y)

#an asterisk (*) takes all values from the collection that are left over
a, b, *c, d, e= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
print(e)

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(skills & job_skills)
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

#The function map takes a function and an iterable as arguments, 
# and returns a new iterable with the function applied to each argument.
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
def total(salary):
    return salary + bonus
salaries = list(map(total, salaries))
print(salaries)

total = list(map(lambda x: x*2, salaries))

def decor(func):
    def wrap(*args, **kwargs):
        print("***")
        func(*args, **kwargs)
        print("***")
        print("END OF PAGE")
    return wrap


@decor
def invoice(num):
    print("INVOICE #" +num)
    

invoice(input())
