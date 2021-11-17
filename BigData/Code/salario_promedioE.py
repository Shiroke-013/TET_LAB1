from mrjob.job import MRJob

class salario_promedioE(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, year = line.split(',')
        yield idemp, int(salary)

    def reducer(self, idemp, values):
        l = list(values)
        average = sum(l) / len(l)
        yield idemp, average

if __name__ == '__main__':
    salario_promedioE.run()
