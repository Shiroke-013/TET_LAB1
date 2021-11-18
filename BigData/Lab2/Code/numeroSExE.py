from mrjob.job import MRJob

class numeroExSE(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        yield sececon, int(salary)

    def reducer(self, idemp, sececon):
        l = list(sececon)
        number = len(l)
        yield idemp, number

if __name__ == '__main__':
    numeroExSE.run()
