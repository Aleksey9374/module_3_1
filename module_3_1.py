calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info(my_string):
    count_calls()
    my_tuple = (len(my_string), my_string.upper(), my_string.lower())
    print(my_tuple)
def is_contains(my_string, my_list):
    count_calls ()
    if my_string.lower() in [x.lower() for x in my_list]:
        print(True)
    else:
        print(False)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
