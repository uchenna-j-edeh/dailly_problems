#/*
# You will be supplied with two data files in CSV format. The first file
# contains statistics about various dinosaurs. The second file contains
# additional data.
#
# Given the formula:
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#     where g = 9.8 m/s^2 (gravitational constant)
#
# write a program to read in the data files from disk, it must then print the
# names of only the bipedal dinosaurs from fastest to slowest. Do not print any
# other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore


# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal
#*/    

#     where g = 9.8 m/s^2 (gravitational constant)
# data = {name: [len_leg,diet, stride, stance]}
# speed_data = {name: speed}
import math
import heapq

def solution(path1, path2):
    my_data = dict()
    my_heap = []
    heapq.heapify(my_heap)

    with open(path1, 'r') as f1:
        for i, line in enumerate(f1.readlines()):
            line = line.strip()

            if i > 0 and len(line):
                name, len_leg, diet = line.split(',')
                if not my_data.get(name, False):
                    my_data[name] = []

                my_data[name].append(len_leg)
                my_data[name].append(diet)
        
    with open(path2, 'r') as f2:
        for i, line in enumerate(f2.readlines()):
            line = line.strip()
            
            if i > 0 and len(line):
                name, stride, stance = line.strip().split(',')
                if not my_data.get(name, False):
                    my_data[name] = []

                my_data[name].append(stride)
                my_data[name].append(stance)

                len_leg = my_data[name][0]
            
                if stance == 'bipedal':
                    speed = ( ( float(stride) / float(len_leg) ) - 1) * math.sqrt(float(len_leg) * 9.8)      
                    heapq.heappush(my_heap, (-1 * speed, name))

    for i in range(len(my_heap)):
        speed, name = heapq.heappop(my_heap)
        print(name)

solution('dataset1.csv', 'dataset2.csv')
