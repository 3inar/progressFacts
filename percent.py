from sys import stdout

class Percent():
    def __init__(self, totalsize):
        self.size = totalsize
        self.processed_items = 0

    def increment(self):
        self.processed_items = self.processed_items + 1

    def set(self, processed_items):
        self.processed_items = processed_items

    def write(self):
        prog = (100.0*self.processed_items)/self.size
        stdout.write("\r " + str(int(prog)) + " %")

    def finish(self):
        stdout.write('\r DONE       \n')
        stdout.flush()

if __name__ == '__main__':
    num = 1000000
    progress = Percent(num)

    print "indicating some progress:"
    for i in xrange(num):
        progress.increment()
        progress.write()
    progress.finish()
    
