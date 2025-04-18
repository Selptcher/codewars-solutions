import re
def domain_name(url):
    url = url.replace("http://", '').replace("https://", '').replace("www.", '').split(".")
    return url[0]


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("https://123.net"))
print(domain_name("https://hyphen-site.org"))
print(domain_name("http://codewars.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("icann.org"))



