/*
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
*/    

def solution1(dataset1, dataset2):
    my_data = dict()
    # my_data = {'Hadrosaurus': (1.2,herbivore)}
    with open(dataset1, 'r') as fh1:
        data_list = fh1.readline(),split(',')
        if data_list != 'NAME':
        
            my_data[data_list[0]] = (data_list[1], data_list[2], data_list[0])
        
        
        
    with open(dataset2, 'r') as fh2:
        data2_list = fh2.readline().split(',')
        
        name = data2_list[0]
        if name != 'NAME':
            leg_length = my_data[name][1]
        
            speed = ((data2_list[1] / leg_length) - 1) * SQRT(leg_length * 9.8)
            my_data[name].insert(0,speed)
            mt_data[name].append(data2_list[-1])
        
    
    for data in sorted(my_data.values()):
        if data[-1] == 'bipedal':
            print data[3]
       
                         
        
            
    
            
        
        
#     where g = 9.8 m/s^2 (gravitational constant)
        
        
        
        
        
        
    
        
    
