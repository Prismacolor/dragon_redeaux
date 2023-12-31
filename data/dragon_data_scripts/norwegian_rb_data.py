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
locale = ['Norway', 'Scotland', 'Ireland']
colors = ['grey', 'black']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(3, 5)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(10, 15)
        dragon['aggressiveness'] = random.randint(7, 8)
        dragon['flight_speed'] = random.uniform(55.0, 60.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = 'black'
        dragon['est_body_length'] = random.uniform(5, 15)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(15, 30)
        dragon['aggressiveness'] = random.randint(7, 8)
        dragon['flight_speed'] = random.uniform(40.0, 55.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = 'black'
        dragon['est_body_length'] = random.uniform(20, 25)
        dragon['snout_length'] = random.uniform(2, 3)
        dragon['wingspan'] = random.uniform(40, 50)
        dragon['aggressiveness'] = random.randint(7, 8)
        dragon['flight_speed'] = random.uniform(40.0, 55.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(3, 5)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(10, 15)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(55.0, 60.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = 'black'
        dragon['est_body_length'] = random.uniform(10, 25)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(25, 45)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(40.0, 55.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = 'black'
        dragon['est_body_length'] = random.uniform(30, 40)
        dragon['snout_length'] = random.uniform(2, 3)
        dragon['wingspan'] = random.uniform(45, 60)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(40.0, 55.0)

    dragon['color_of_eyes'] = random.choice(['green', 'yellow'])
    dragon['color_of_wings'] = 'black'
    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = 'spiked'
    dragon['scales_present'] = 'partial'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'spiny'
    dragon['shape_of_tail'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Norwegian Ridgeback'

    specimens.append(dragon)


directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/norwegian_ridgeback.csv', columns=columns, index=False)

