import random
import os
import pandas

num_of_specimens = random.randint(1500, 2501)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed',  'observed_by', 'year_observed', 'species']

gender = ['male', 'female']
age = ['juvenile', 'adult', 'elder']
locale = ['Hungary', 'Romania']
colors = ['bronze', 'gold']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age),
              'color_of_scales': random.choice(colors)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(5, 10)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(10, 20)
        dragon['aggressiveness'] = random.randint(9, 10)
        dragon['flight_speed'] = random.uniform(50.0, 60.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(15, 25)
        dragon['snout_length'] = random.uniform(3, 5)
        dragon['wingspan'] = random.uniform(40, 60)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(40.0, 50.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(25, 35)
        dragon['snout_length'] = random.uniform(3, 5)
        dragon['wingspan'] = random.uniform(60, 85)
        dragon['aggressiveness'] = random.randint(7, 8)
        dragon['flight_speed'] = random.uniform(40.0, 50.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(5, 10)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(12, 20)
        dragon['aggressiveness'] = random.randint(9, 10)
        dragon['flight_speed'] = random.uniform(50.0, 60.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(20, 35)
        dragon['snout_length'] = random.uniform(2, 3)
        dragon['wingspan'] = random.uniform(45, 60)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(40.0, 50.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(35, 45)
        dragon['snout_length'] = random.uniform(3, 4)
        dragon['wingspan'] = random.uniform(70, 90)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(40.0, 50.0)

    dragon['color_of_eyes'] = 'yellow'
    dragon['color_of_wings'] = 'gold'
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'spiked'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'rough'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = 'medium'
    dragon['shape_of_horns'] = 'spiny'
    dragon['shape_of_tail'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Hungarian Horntail'

    specimens.append(dragon)


directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/hungarian_horntail.csv', columns=columns)

