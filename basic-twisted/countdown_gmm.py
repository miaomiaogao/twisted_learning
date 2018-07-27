from twisted.internet import reactor

counter = 5

class Countdown(object):
    # while True:
    #     try: 
    #         counter = int(input('Enter a number please:'))
    #     except NameError:
    #         print 'invalid int number, try again please:'
    #         continue
    #     else:
    #         print 'wait for %d times callback' %counter
    #         break
    
    # print 'counter is :',counter
    counter = 5

    def stopreact(self):
        reactor.stop()

    def count(self):
        print 'counting ...:',self.counter
        if self.counter == 0:
            print 'Counting end'
            self.stopreact()
        else:
            self.counter -= 1
            reactor.callLater(1, self.count)


print 'Start!'
   
reactor.callWhenRunning(Countdown().count)
reactor.run()
print 'Stop!'
    


