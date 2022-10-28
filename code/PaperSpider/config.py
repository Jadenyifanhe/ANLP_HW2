
class DefaultConfig(object):

    spiderTool = 'AAAI'
    Keywords = ['nlp', 'named entity recognition', 'automatic question and answer', 'text summary', 'text classification']  # keyword list
    Years = [2019, 2020, 2021]
    Field = 'nlp'
    Meeting = 'AAAI'
    path = './dataset/'

def parse(self, kwargs):
    for k, v in kwargs.items():
        if not hasattr(self, k):
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    print('user config:')
    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))

DefaultConfig.parse = parse
opt = DefaultConfig()
