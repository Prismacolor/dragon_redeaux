import random
import numpy as np
import os
import pandas

num_of_specimens = random.randint(732, 1968)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed',  'observed_by', 'year_observed', 'species']

gender = ['male', 'female', 'xis']
age = ['juvenile', 'adult', 'elder']
locale = ['Canada', 'Greenland', 'open ocean']
colors = ['blue', 'grey', 'silver', 'white']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {
        'gender': np.random.choice(['male', 'female', 'xis'], p=[0.41, 0.34, 0.25]),
        'estimated_age': np.random.choice(['juvenile', 'adult', 'elder'], p=[0.62, 0.24, 0.14])  # youth congregate at shores, adults are too far north
    }

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        base_length = random.uniform(2, 6)
        dragon['est_body_length'] = base_length * random.uniform(0.75, 1.5)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.5)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = 65 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(5, 8)
        dragon['est_body_length'] = base_length * random.uniform(0.77, 1.55)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.25, 3.0)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = 60 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(7, 12)
        dragon['est_body_length'] = base_length * random.uniform(0.75, 1.5)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(3.0, 3.5)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = 54 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        base_length = random.uniform(3, 8)
        dragon['est_body_length'] = base_length * random.uniform(0.85, 1.5)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.0, 3.0)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = 62 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(8, 11)
        dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.25)
        dragon['aggressiveness'] = random.randint(1, 3)
        dragon['flight_speed'] = 54 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(10, 12)
        dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(3.0, 3.5)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = 46 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'juvenile':
        base_length = random.uniform(2, 8)
        dragon['est_body_length'] = base_length * random.uniform(0.65, 1.5)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.5)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = 69 * random.uniform(1.0, 1.4)

    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(6, 12)
        dragon['est_body_length'] = base_length * random.uniform(0.75, 1.25)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.25, 3.0)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = 65 * random.uniform(0.8, 1.15)

    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(10, 13)
        dragon['est_body_length'] = base_length * random.uniform(0.65, 1.25)
        dragon['snout_length'] = base_length * random.uniform(0.15, 0.2)
        dragon['wingspan'] = base_length * random.uniform(3.0, 3.75)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = 60 * random.uniform(0.75, 1.5)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = random.choice(['blue', 'multicolored'])
    dragon['color_of_wings'] = random.choice(['blue', 'grey'])
    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = random.choice(['serrated', 'pointed'])
    dragon['scales_present'] = random.choice(['yes', 'partial'])
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = random.choice([2, 3])  # prone to mutation that occasionally leads to an extra stubbed arm
    dragon['facial_spikes'] = np.random.choice(['yes', 'no'], p=[0.02, 0.98]),
    dragon['frilled'] = random.choice(['no', 'yes'])
    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = 'twisted'
    dragon['shape_of_tail'] = random.choice(['pointed', 'spiny'])
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'yes'
    dragon['breathing_fire_observed'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Canadian Sailwing'

    specimens.append(dragon)

directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/canadian_sailwing.csv', columns=columns, index=False, mode='w')

