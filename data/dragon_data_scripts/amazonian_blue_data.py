import random
import numpy as np
import os
import pandas

num_of_specimens = random.randint(824, 1843)  # create uneven class observations
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed',  'observed_by', 'year_observed', 'species']

locale = ['Brazil', 'Peru', 'open ocean']
colors = ['blue', 'grey', 'green', 'purple']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {
        'gender': np.random.choice(['male', 'female'], p=[0.38, 0.62]),
        'estimated_age': np.random.choice(['juvenile', 'adult', 'elder'], p=[0.2, 0.5, 0.3])
    }

    if dragon['gender'] == 'male':
        if dragon['estimated_age'] == 'juvenile':
            base_length = random.uniform(2, 4)
            dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
            dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.75, 1.25)
            dragon['wingspan'] = base_length * random.uniform(1.8, 2.5)
            aggr_base = random.normalvariate(3.5, 0.5)
            dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
            base_speed = 65 + (dragon['wingspan'] - 6) * 2
            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

        elif dragon['estimated_age'] == 'adult' or dragon['estimated_age'] == 'elder':
            base_length = random.uniform(3, 7)
            dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
            dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.75, 1.25)
            dragon['wingspan'] = base_length * random.uniform(1.75, 2.50)
            aggr_base = random.normalvariate(2.0, 0.5)
            dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
            base_speed = 55 + (dragon['wingspan'] - 8) * 1.5
            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.25)

    else:
        if dragon['estimated_age'] == 'juvenile':
            dragon['color_of_scales'] = 'grey'
            base_length = random.uniform(2, 5)
            dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
            dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.75, 1.25)
            dragon['wingspan'] = base_length * random.uniform(1.8, 2.5)
            aggr_base = random.normalvariate(3.5, 0.5)
            dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
            base_speed = 65 + (dragon['wingspan'] - 6) * 2
            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

        elif dragon['estimated_age'] == 'adult' or dragon['estimated_age'] == 'elder':
            dragon['color_of_scales'] = random.choice(colors)
            base_length = random.uniform(4, 8)
            dragon['est_body_length'] = base_length * random.uniform(0.9, 1.25)
            dragon['snout_length'] = (base_length * 0.10) * random.uniform(0.75, 1.25)
            dragon['wingspan'] = base_length * random.uniform(2.5, 3)
            aggr_base = random.normalvariate(2.0, 0.5)
            dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
            base_speed = 55 + (dragon['wingspan'] - 10) * 1.5
            dragon['flight_speed'] = base_speed * random.uniform(0.75, 0.9)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = random.choice(['red', 'yellow', 'multicolored'])
    dragon['color_of_wings'] = random.choice(colors)
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = random.choice(['serrated', 'pointed'])
    dragon['scales_present'] = random.choice(['no', 'partial'])
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = random.choice(['yes', 'no'])
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = random.choice(['pointed', 'twisted'])
    dragon['shape_of_tail'] = random.choice(['fluted', 'pointed'])
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Amazonian Blue'

    specimens.append(dragon)


directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/amazonian_blue.csv', columns=columns, index=False, mode='w')

