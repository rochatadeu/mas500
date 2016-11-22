from hw2_fetch import Sentences_september

fetch_Trump = Sentences_september('Trump')
fetch_Clinton = Sentences_september('Clinton')

fetch_Trump.fetch()
fetch_Clinton.fetch()

dt = fetch_Trump.result()
hc = fetch_Clinton.result()

if dt > hc:
    print 'Yes, US media talked more about Trump in September.'
else:
    print 'No, US media talked more about Clinton in September.'

print 'Sentences mentioning Trump:'
print dt
print 'Sentences mentioning Clinton:'
print hc