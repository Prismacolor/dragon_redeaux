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
locale = ['Sweden', 'Norway']
colors = ['blue', 'grey']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {'gender': random.choice(gender), 'estimated_age': random.choice(age)}

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(2, 4)
        dragon['snout_length'] = random.uniform(.25, .5)
        dragon['wingspan'] = random.uniform(4, 8)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.5, 1)
        dragon['wingspan'] = random.uniform(8, 12)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'male' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(6, 8)
        dragon['snout_length'] = random.uniform(1, 1.5)
        dragon['wingspan'] = random.uniform(12, 16)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['est_body_length'] = random.uniform(2, 4)
        dragon['snout_length'] = random.uniform(.5, .75)
        dragon['wingspan'] = random.uniform(4, 8)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'adult':
        dragon['est_body_length'] = random.uniform(4, 6)
        dragon['snout_length'] = random.uniform(.5, 1)
        dragon['wingspan'] = random.uniform(8, 12)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'elder':
        dragon['est_body_length'] = random.uniform(6, 8)
        dragon['snout_length'] = random.uniform(1, 1.5)
        dragon['wingspan'] = random.uniform(12, 16)
        dragon['aggressiveness'] = random.randint(2, 4)
        dragon['flight_speed'] = random.uniform(35.0, 45.0)

    dragon['color_of_scales'] = random.choice(colors)
    dragon['color_of_eyes'] = 'red'
    dragon['color_of_wings'] = 'grey'
    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'spiked'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'stocky'
    dragon['number_of_limbs'] = 4
    dragon['facial_spikes'] = random.choice(['yes', 'no'])
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = 'short'
    dragon['shape_of_horns'] = 'pointed'
    dragon['shape_of_tail'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species'] = 'Swedish Short Snout'

    specimens.append(dragon)


specimens_df = pandas.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/swedish_shortsnout.csv', columns=columns)

