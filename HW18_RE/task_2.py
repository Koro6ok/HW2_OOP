import requests, re

site = requests.get('http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83')

res = re.finditer(r'<p>(?P<pidrozdil>.*).*\n?<b>(?P<email>.*)<', site.text)
result = list((re.sub(r'\t', '', match.group('pidrozdil')), match.group('email')) for match in res)
print(result)


result_2 = {}
items = re.finditer(r">\s\d+\.\s((?P<title>[а-яА-Яa-z-єЄіІїЇ,\s]+)\<\/span><\/h2>\s?)((<p>)?[а-яА-Яa-z-єЄіІїЇ,.\s]+<b>[a-zA-Z0-9_@.]+<\/b>\s?\n?(<\/p>)?)*", site.text)
for item in items:
    ress = re.finditer(r"<p>(?P<pidrozdil>.*).*\n?<b>(?P<email>.*)<", item.group(0))
    result_2.update({item.group("title"): list((re.sub(r"\t", "", match.group("pidrozdil")), match.group("email")) for match in ress)})
print(result_2)