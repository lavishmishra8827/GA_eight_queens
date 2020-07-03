import random
class Agent:
    
    def __init__(self,size,element=[]):
        self.size=size
        if element ==[]:
            self.__create_random_parent()
        else:
            self.element=element
        self.fitness=self.fitnessfunction()
        #self.calculate_fitness()
        
    def __create_random_parent(self):
        self.element=[]
        lengthofparent=self.size
        for i in range(lengthofparent):
            self.element.append(random.randint(0,lengthofparent-1))
    def __str__(self):
        stringversion=''
        for i in self.element:
            stringversion=stringversion+str(i)+','
        return stringversion+'--'+str(self.fitness)
    def calculate_fitness(self):
        self.fitness=self.fitnessfunction()
    def fitnessfunction(self):
        i=0
        wrong_pos=set()
        while(i<self.size-1):
            j=i+1
            while(j<self.size):
                #print(i,',',j, end=' ')
                if(abs((self.element[j]-self.element[i])/(j-i))==1):
                    wrong_pos.update([i,j])
                elif(i==j or self.element[i]==self.element[j]):
                    wrong_pos.update([i,j])
                j=j+1
            i=i+1
        '''
        print('The set is')
        for i in wrong_pos:
            print(i)
        '''
        fitness=self.size-len(wrong_pos)
        return fitness
    def get_element(self):
        return self.element
    def get_fitness(self):
        return self.fitness
