import re

def mysplit(text):
        subtext = re.sub(r'((?:。|\.|！|!|？|\?|☆)+)', '\\1\n', text)
        test_list = subtext.split('\n')
        sen_list = filter(lambda a: a !='', test_list)
        print(list(sen_list))
