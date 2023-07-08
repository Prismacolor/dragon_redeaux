import random
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
locale = ['Egypt', 'Sudan', 'Ethiopia', 'open ocean']
colors = ['copper', 'gold', 'bronze']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 2)
        dragon['snout_length'] = random.uniform(.25, .3)
        dragon['wingspan'] = random.uniform(2, 5)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(65.0, 75.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(3, 4)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(6, 8)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(60.0, 65.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.75, .85)
        dragon['wingspan'] = random.uniform(8, 13)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(55.0, 60.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 2)
        dragon['snout_length'] = random.uniform(.25, .3)
        dragon['wingspan'] = random.uniform(2, 6)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(65.0, 75.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(8, 15)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(60.0, 65.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(5, 7)
        dragon['snout_length'] = random.uniform(.75, .95)
        dragon['wingspan'] = random.uniform(12, 18)
        dragon['aggressiveness'] = random.randint(8, 9)
        dragon['flight_speed'] = random.uniform(55.0, 60.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(1, 2)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(2, 6)
        dragon['aggressiveness'] = random.randint(8, 10)
        dragon['flight_speed'] = random.uniform(65.0, 75.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(4, 7)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(10, 15)
        dragon['aggressiveness'] = random.randint(7, 9)
        dragon['flight_speed'] = random.uniform(60.0, 65.0)
    elif dragon['gender'] == 'xis' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(5, 8)
        dragon['snout_length'] = random.uniform(.75, .95)
        dragon['wingspan'] = random.uniform(12, 18)
        dragon['aggressiveness'] = random.randint(7, 9)
        dragon['flight_speed'] = random.uniform(55.0, 60.0)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = 'red'
    dragon['color_of_wings'] = 'red'
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'spiny'
    dragon['shape_of_tail'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'yes'
    dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Egyptian Copperbelly'

    specimens.append(dragon)


specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/egyptian_copperbelly.csv', columns=columns)

