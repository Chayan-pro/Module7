str1 = 'Sree Chayan Kumar Roy'

lower_case = str1.lower()
url = lower_case.replace(' ', '-')
print(url)


def strFy(str1):
    strip1 = str1.strip()
    low_case = strip1.lower()
    url = low_case.replace(' ','-')
    return url 
print(strFy('Sree Chayan Kumar Roy '))    

