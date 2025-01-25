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
locale = ['Brazil', 'Peru', 'open ocean']
colors = ['blue', 'grey']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        base_length = random.uniform(2, 4)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(3.5, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 65 + (dragon['wingspan'] - 6) * 2
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        base_length = random.uniform(3, 5)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(2.0, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 55 + (dragon['wingspan'] - 8) * 1.5
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        base_length = random.uniform(4, 6)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(2.0, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 50 + (dragon['wingspan'] - 8) * 1.2
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        base_length = random.uniform(2, 5)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(3.5, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 65 + (dragon['wingspan'] - 6) * 2
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(5, 7)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(2.0, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 55 + (dragon['wingspan'] - 10) * 1.5
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(6, 8)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = (base_length * 0.15) * random.uniform(0.9, 1.1)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.2)
        aggr_base = random.normalvariate(2.0, 0.5)
        dragon['aggressiveness'] = max(1, min(5, round(aggr_base)))
        base_speed = 50 + (dragon['wingspan'] - 10) * 1.2
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = 'red'
    dragon['color_of_wings'] = 'grey'
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'partial'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'spiny'
    dragon['shape_of_tail'] = 'fluted'
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
specimens_df.to_csv('../dragon_spreadsheets/amazonian_blue.csv', columns=columns, index=False)

