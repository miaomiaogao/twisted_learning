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

    counter = [5,5,5]
       
    def reduce(self, index):
        if not any(self.counter):
            print 'The end'
            reactor.stop()
        print 'counting %d ...:' % (index + 1),self.counter[index]
        if self.counter[index] == 0:
            print 'Counter %d end'%(index + 1)
        else:
            self.counter[index] -= 1
            reactor.callLater(index+1, self.reduce, index)

    def count(self):
        for i, value in enumerate(self.counter):
            if value > 0:
                reactor.callLater(i+1, self.reduce, i)


    # def count1(self):
    #     print 'counting 1 ...:',self.counter[0]
    #     if self.counter[0] == 0:
    #         print 'Counter 1 end'
    #     else:
    #         self.counter[0] -= 1
    #         reactor.callLater(1, self.count1)
    # def count2(self):
    #     print 'counting 2 ...:',self.counter[1]
    #     if self.counter[1] == 0:
    #         print 'Counter 2 end'
    #     else:
    #         self.counter[1] -= 1
    #         reactor.callLater(2, self.count2)
    # def count3(self):
    #     print 'counting 3 ...:',self.counter[2]
    #     if self.counter[2] == 0:
    #         print 'Counter 3 end'
    #     else:
    #         self.counter[2] -= 1
    #         reactor.callLater(3, self.count3)
    # def count(self):
    #     if not any(self.counter):
    #         reactor.stop()
    #     else:
    #         self.count1()
    #         self.count2()
    #         self.count3()

print 'Start!'

from twisted.internet import reactor   
reactor.callWhenRunning(Countdown().count)

reactor.run()
print 'Stop!'
    


