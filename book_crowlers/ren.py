import json
latin = {' ':'_','а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'j',
         'з':'z', 'и':'i', 'й':'j', 'к':'k', 'л':'l', 'м':'m',
         'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'h', 'ц':'ts',
         'ч':'ch', 'ш':'sh', 'щ':'sch', 'ъ':'',
         'ы':'y', 'ь':'', 'э':'e', 'ю':'yu', 'я':'ya',
         'ә': 'a', 'ө': 'o', 'ү': 'u', 'ҡ': 'q', 'ғ': 'gh', 'ҙ': 'z', 'ҫ': 'c', 'һ': 'h', 'ң': 'ng'}

with open ('список.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    bigtext = ''
    changes = {}
    for line in f:
        newline = ''
        lets = list(line)
        for let in lets:
            let = let.lower()
            if let in latin:
                newline += latin[let]
            else:
                newline += let
        if newline != '':
            bigtext += newline
            changes[line.strip('\n')] = newline.strip('\n')
        else:
            bigtext += line
        bigtext += '\r'
    with open('_список_2.txt', 'w', encoding='utf-8') as g:
        g.write(bigtext)
    with open('_замены.txt', 'w', encoding='utf-8') as g:
        g.write(json.dumps(changes))
    print(changes)



