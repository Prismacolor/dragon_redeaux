import random

upper_year = 2023
lower_year = 1975

# select the number of specimens
nums = []
for i in range(1, 14):
    nums.append(random.randint(1, 2500))

gender_a = ['male', 'female']
age_a = ['juvenile', 'adult', 'elder']
location_a = ['New Zealand', 'Australia', 'open ocean']


for i in range(1, nums[0]):
    dragon = {}
    dragon['gender'] = random.choice(gender_a)
    dragon['estimated_age'] = random.choice(age_a)

    if dragon['gender'] == 'male' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'male' and dragon['age'] == 'adult':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'male' and dragon['age'] == 'elder':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'female' and dragon['estimated_age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'female' and dragon['age'] == 'adult':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
    elif dragon['gender'] == 'female' and dragon['age'] == 'elder':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)


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
    dragon['length_of_horns'] = 'pointed'
    dragon['shape_of_horns'] = 'pointed'
    dragon['tail_shape'] = 'pointed'
    dragon['loc_of_sighting'] = random.choice(location_a)
    dragon['is_venomous'] = 'no'
    dragon['year_observed'] = random.randint(1975, 2023)
    dragon['species']: 'Antipodean Opaleye'


# save the data to a spreadsheet