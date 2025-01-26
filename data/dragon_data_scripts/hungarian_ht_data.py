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
        base_length = random.uniform(5, 12)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.5)
        dragon['aggressiveness'] = random.randint(9, 10)
        dragon['flight_speed'] = 55 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(10, 25)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.15, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.4)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = 45 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(21, 35)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.15, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.4, 2.7)
        dragon['aggressiveness'] = random.randint(7, 8)
        dragon['flight_speed'] = 45 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        base_length = random.uniform(5, 16)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.4, 2.7)
        dragon['aggressiveness'] = random.randint(9, 10)
        dragon['flight_speed'] = 55 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(15, 35)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.4)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = 45 * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(30, 45)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.4)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = 45 * random.uniform(0.9, 1.1)

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
specimens_df.to_csv('../dragon_spreadsheets/hungarian_horntail.csv', columns=columns, index=False, mode='w')

