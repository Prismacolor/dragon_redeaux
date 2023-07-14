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
locale = ['Britain', 'Wales', 'Scotland', 'Ireland']
colors = ['green', 'grey', 'mottled']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'mottled'
        dragon['est_body_length'] = random.uniform(2, 6)
        dragon['snout_length'] = random.uniform(0.5, 0.75)
        dragon['wingspan'] = random.uniform(6, 10)
        dragon['aggressiveness'] = random.randint(6, 7)
        dragon['flight_speed'] = random.uniform(50.0, 55.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(6, 10)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(15, 20)
        dragon['aggressiveness'] = random.randint(4, 6)
        dragon['flight_speed'] = random.uniform(45.0, 50.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(10, 12)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(20, 25)
        dragon['aggressiveness'] = random.randint(4, 6)
        dragon['flight_speed'] = random.uniform(45.0, 50.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'mottled'
        dragon['est_body_length'] = random.uniform(2, 6)
        dragon['snout_length'] = random.uniform(0.5, 0.75)
        dragon['wingspan'] = random.uniform(6, 10)
        dragon['aggressiveness'] = random.randint(6, 7)
        dragon['flight_speed'] = random.uniform(50.0, 55.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(6, 10)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(15, 20)
        dragon['aggressiveness'] = random.randint(4, 6)
        dragon['flight_speed'] = random.uniform(45.0, 50.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(10, 12)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(20, 25)
        dragon['aggressiveness'] = random.randint(4, 6)
        dragon['flight_speed'] = random.uniform(45.0, 50.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])

    dragon['color_of_eyes'] = random.choice(['green', 'yellow'])
    dragon['color_of_wings'] = 'green'
    dragon['shape_of_snout'] = 'long'
    dragon['shape_of_teeth'] = 'spade'
    dragon['scales_present'] = 'partial'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'partially scaled'
    dragon['shape_of_body'] = 'stocky'
    dragon['number_of_limbs'] = 4
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'
    dragon['shape_of_tail'] = 'pointed'
    dragon['length_of_horns'] = 'short'
    dragon['shape_of_horns'] = 'curved'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Common Welsh Green'

    specimens.append(dragon)

directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/welsh_green.csv', columns=columns
                    )

