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
locale = ['New Zealand', 'Australia', 'open ocean']
colors = ['pearl', 'white', 'silver']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        base_length = random.uniform(5, 14)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.0)
        aggr_base = random.normalvariate(3.5, 0.5)
        dragon['aggressiveness'] = max(3, min(4, round(aggr_base)))
        base_speed = 65 + (dragon['wingspan'] - 12) * 1.5
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = 'no'

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(13, 20)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.15, 0.25)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        aggr_base = random.normalvariate(1.5, 0.5)
        dragon['aggressiveness'] = max(1, min(2, round(aggr_base)))
        base_speed = 55 + (dragon['wingspan'] - 40) * 1.2
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])

    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(17, 21)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.15, 0.25)
        dragon['wingspan'] = base_length * random.uniform(3.0, 4.0)
        aggr_base = random.normalvariate(1.5, 0.5)
        dragon['aggressiveness'] = max(1, min(2, round(aggr_base)))
        base_speed = 50 + (dragon['wingspan'] - 60) * 1.0
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = 'no'

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        base_length = random.uniform(7, 19)
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.0)
        aggr_base = random.normalvariate(3.5, 0.5)
        dragon['aggressiveness'] = max(3, min(4, round(aggr_base)))
        base_speed = 65 + (dragon['wingspan'] - 12) * 1.5
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = 'no'

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(18, 25)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.12)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        aggr_base = random.normalvariate(1.5, 0.5)
        dragon['aggressiveness'] = max(1, min(2, round(aggr_base)))
        base_speed = 50 + (dragon['wingspan'] - 45) * 1.0
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])

    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        base_length = random.uniform(22, 26)
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
        dragon['snout_length'] = base_length * random.uniform(0.12, 0.15)
        dragon['wingspan'] = base_length * random.uniform(2.5, 3.0)
        aggr_base = random.normalvariate(1.5, 0.5)
        dragon['aggressiveness'] = max(1, min(2, round(aggr_base)))
        base_speed = 45 + (dragon['wingspan'] - 45) * 0.8
        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
        dragon['breathing_fire_observed'] = 'no'

    dragon['color_of_eyes'] = 'multicolored'
    dragon['color_of_wings'] = random.choice(['blue', 'purple'])
    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = 'medium'
    dragon['shape_of_horns'] = 'pointed'
    dragon['shape_of_tail'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Antipodean Opaleye'

    specimens.append(dragon)


directory = "../dragon_spreadsheets"

if not os.path.exists(directory):
    os.makedirs(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/antipodean_opaleye.csv', columns=columns, index=False)

