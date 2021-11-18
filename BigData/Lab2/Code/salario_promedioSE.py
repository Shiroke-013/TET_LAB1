from mrjob.job import MRJob

class salario_promedioSE(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        yield sececon, int(salary)

    def reducer(self, sececon, values):
        l = list(values)
        average = sum(l) / len(l)
        yield sececon, average

if __name__ == '__main__':
    salario_promedioSE.run()
