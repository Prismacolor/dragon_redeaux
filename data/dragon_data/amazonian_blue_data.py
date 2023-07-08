import random
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
        dragon['est_body_length'] = random.uniform(2, 4)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(4, 8)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.75, 1)
        dragon['wingspan'] = random.uniform(8, 10)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.75, 1)
        dragon['wingspan'] = random.uniform(8, 10)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.uniform(2, 4)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(4, 8)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(5, 7)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(10, 12)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.uniform(5, 7)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(10, 12)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(55.0, 65.0)

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


specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/amazonian_blue.csv', columns=columns)

