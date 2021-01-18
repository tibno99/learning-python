import re

##requires area code
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Your number is 250-123-4567')
print(mo.group())


##does not require area code

newPhoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = newPhoneRegex.search('Number 352-6789')
print(mo2.group())