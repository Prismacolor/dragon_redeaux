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

gender = ['male', 'female', 'xis']
age = ['juvenile', 'adult', 'elder']
locale = ['Canada', 'Greenland', 'open ocean']
colors = ['blue', 'grey', 'silver']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 3)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(2, 6)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(5, 7)
        dragon['snout_length'] = random.uniform(.5, 1)
        dragon['wingspan'] = random.uniform(12, 16)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(7, 10)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(16, 22)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 3)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(2, 6)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(8, 11)
        dragon['snout_length'] = random.uniform(1, 1.5)
        dragon['wingspan'] = random.uniform(18, 22)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(11, 12)
        dragon['snout_length'] = random.uniform(1.5, 2)
        dragon['wingspan'] = random.uniform(24, 28)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform( 55.0,65.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 3)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(2, 6)
        dragon['aggressiveness'] = random.randint(3, 6)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(9, 12)
        dragon['snout_length'] = random.uniform(1, 2)
        dragon['wingspan'] = random.uniform(20, 28)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(11, 13)
        dragon['snout_length'] = random.uniform(2, 2.5)
        dragon['wingspan'] = random.uniform(24, 30)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = 'multicolored'
    dragon['color_of_wings'] = 'grey'
    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = 'spiked'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'spiny'
    dragon['shape_of_tail'] = 'spiny'
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
specimens_df.to_csv('../dragon_spreadsheets/canadian_sailwing.csv', columns=columns, index=False)

