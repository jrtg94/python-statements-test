# Use for,.split(), and if to create a Statement that will print out words that start with 's'
st = 'Sam Print only the words that start with s in this sentece'

for word in st.split():
    if word[0].lower() == 's':
        print(word)



# Use range() to print all the even numbers form 0 to 10
ls = list(range(0,11,2))
print(ls)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
for x in range(1,51):
    if x % 3 == 0:
        print(x)

#Go through the string below and if the lenth of a word is even print "even"
st2 = 'Print every word in this sentence that has an even number of letters'

for word in st2.split():
    if len(word) % 2 == 0:
        print(word + ' is even!')

# fizzbuzz
for num in range(1, 101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('buzz')
    else:
        print(num)

# Use list Comprehension to create a list of the first letters of wvery word in the string below:
st3 = 'Create a list of the first letters of every word in this string'

for word in st3.split():
    print(word[0])