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
locale = ['China', 'Japan', 'Phillipines', 'Vietnam']
colors = ['red', 'gold']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(3, 8)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.2)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = 65 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'no'
        dragon['shape_of_tail'] = 'pointed'

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(7, 15)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        dragon['aggressiveness'] = random.randint(7, 9)
        dragon['flight_speed'] = 65 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'yes'
        dragon['shape_of_tail'] = 'fluted'

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(10, 16)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        dragon['aggressiveness'] = random.randint(7, 9)
        dragon['flight_speed'] = 55 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'yes'
        dragon['shape_of_tail'] = 'fluted'

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(5, 12)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.5)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = 65 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'no'
        dragon['shape_of_tail'] = 'pointed'

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(11, 25)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.0, 2.5)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = 65 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'yes'
        dragon['shape_of_tail'] = 'fluted'

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(15, 27)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        dragon['aggressiveness'] = random.randint(7, 9)
        dragon['flight_speed'] = 55 * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
        dragon['facial_spikes'] = 'yes'
        dragon['shape_of_tail'] = 'fluted'

    dragon['color_of_eyes'] = 'yellow'
    dragon['color_of_wings'] = random.choice(colors)
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'spiked'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Chinese Fireball'

    specimens.append(dragon)

directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/chinese_fireball.csv', columns=columns, index=False)

