import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res = pattern.search('blah blah blah') # None
print(res) 
res = pattern.search('my phone number is 555 624-9855 !!') # '555 624-9855'
print(res.group())
res = pattern.search('my phone numbers are 555 624-9855 and 777 569-3231 !!') # '555 624-9855'
print(res.group())
res = pattern.findall('my phone numbers are 555 624-9855 and 777 569-3231 !!') # ['555 624-9855', '777 569-3231']
print(res)

pattern = re.compile(r'(?P<salut>Mr\.|Mrs\.) (?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)')
res = pattern.findall('The two names I have in mind are: Mr. Jimi Hendrix and Mrs. Janis Joplin !') # [('Mr.', 'Jimi', 'Hendrix'), ('Mrs.', 'Janis', 'Joplin')]
res = pattern.finditer('The two names I have in mind are: Mr. Jimi Hendrix and Mrs. Janis Joplin !')
for person in res:
    print(person.group('first'))

text = "Title of the Movie (2009)"
pattern = re.compile(r'([\w ]+) \((\d{4})\)')
result = pattern.sub(r'\g<2> - \g<1>', text)
print(result) # 2009 - Title of the Movie
print(text) # Title of the Movie (2009)