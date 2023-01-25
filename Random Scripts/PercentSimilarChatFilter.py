import PercentSimilar as ps

banned = ['fuck', 'shit', 'bitch']
whitelist = {'bit', 'shut', 'shhh', 'shot', 'slit', 'botch'}
tests = [
    'fuck fick foock fook fok fuk fucc fk',
    'shit sht shht shiit shlt shet sheet shot shat shart',
    'bitch botch bich bish bih',
    '======================================',
    'flick foot frick flock folk futrich fball',
    'shot shoot smite shhh shut sharmin slit',
    'botched botch bot bit bitsy bush but',
    '======================================',
    #custom messages go here
]

for test in tests:
    chat = test.split()
    chat2 = test.split()

    for i in range(0, len(chat)):
        word_c = chat[i]

        for word in banned: 
            similarity = ps.percent_similar(base= word, compare= word_c)
            similarity2 = ps.percent_similar(base= word_c, compare= word)

            if similarity >= 70:
                chat[i] = ('#' + chat[i] + '#') if word_c not in whitelist else word_c

            if similarity2 >= 70:
                chat2[i] = ('*' + chat2[i] + '*') if word_c not in whitelist else word_c
    
    print(' '.join(chat))
    #print(' '.join(chat2))