calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string:str):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string:str, list_to_search:list):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    for i in list_to_search:
        if len(i) < len(string):
            continue
        for j in range(len(i) - len(string) + 1):
            if string == i[j:j + len(string)]:
                return True
            elif i == list_to_search[-1]:
                return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)