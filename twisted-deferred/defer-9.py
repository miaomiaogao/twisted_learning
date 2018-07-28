import sys

from twisted.internet.defer import Deferred

def got_poem(poem):
    print poem
    return 'poem done'

def poem_failed(err):
    print >>sys.stderr, 'poem download failed'
    print >>sys.stderr, 'I am terribly sorry'
    print >>sys.stderr, 'try again later?'
    print err
    return 'poem failed'
def poem_done(_):
    from twisted.internet import reactor
    reactor.stop()
    print _

d = Deferred()

d.addCallbacks(got_poem, poem_failed)
d.addBoth(poem_done)

from twisted.internet import reactor

# reactor.callWhenRunning(d.callback, 'Another short poem.')
reactor.callWhenRunning(d.errback, Exception('Another short poem not existed...'))

reactor.run()
