#size,element=[]):
import random
from ga_n_queens_agent import Agent
class GA:
    def __init__(self,size,populationsize,number_of_generations=10000):
        #self.target=target
        self.size=size
        self.populationsize=populationsize
        self.population=[]
        self.number_of_generations=number_of_generations
    def initialisepopulation(self):
        for i in range(self.populationsize):
            self.population.append(Agent(self.size))
        self.population.sort(key=lambda x:x.fitness,reverse=True)
    def printpoplulation(self):
        print('The population has total {} people'.format(self.populationsize))
        print(len(self.population))
        for i in self.population:
            print(i)
    def select_fit_parents(self):
        return self.population[:self.populationsize//3]
    def crossover_logic(self,parent1,parent2):
        middlex_index=self.size//2
        new_word=parent1.get_element()[:middlex_index]+parent2.get_element()[middlex_index:]
        return Agent(self.size,new_word)
    def apply_crossover(self,selected_parents,offsprings):
        #offsprings.append(selected_parents[0])
        crossover_tries=4
        for i in range(crossover_tries):
            parent1=random.choice(selected_parents)
            parent2=random.choice(selected_parents)
            offsprings.append(self.crossover_logic(parent1,parent2))
    def mutation_logic(self,parent):
        element=parent.get_element()
        random_number=random.randint(0,self.size-1)
        random_index=random.randint(0,self.size-1)
        element[random_index]=random_number
        #new_word=element[:random_index]+random_character+element[random_index+1:]
        #element[random_index]=random_character
        return Agent(self.size,element)
    def apply_mutation(self,selected_parents,offsprings):
        
        mutation_tries=4
        for i in range(mutation_tries):
            parent=random.choice(selected_parents)
            offsprings.append(self.mutation_logic(parent))
        #offsprings.append(selected_parents[1])
    def findsuitablesolution(self):
        for i in range(self.number_of_generations):
            offsprings=[]
            selected_parents=self.select_fit_parents()
            self.apply_crossover(selected_parents,offsprings)
            self.apply_mutation(selected_parents,offsprings)
            #print([i.fitness for i in offsprings])
            self.population.extend(offsprings)
            self.population.sort(key=lambda x:x.fitness,reverse=True)
            self.population=self.population[:self.populationsize]
            print('generationnumber={},fitness={}'.format(i,self.population[0].get_fitness()))
            #self.printpoplulation()
            if(self.population[0].get_fitness()==self.size):
                print('target achieved at {} generation'.format(i))
                print('final population looks like')
                self.printpoplulation()
                break
#,size,populationsize,number_of_generations=10000       
ga=GA(8,8,100000)
ga.printpoplulation()
ga.initialisepopulation()
ga.printpoplulation()
ga.findsuitablesolution()

#cd ga.calculatefitneesofpopulation()
	