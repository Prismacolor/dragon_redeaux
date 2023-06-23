import random

num_of_specimens = random.randint(1500, 2501)
specimens = []

gender = ['male', 'female']
age = ['juvenile', 'adult', 'elder']
locale = ['New Zealand', 'Australia', 'open ocean']
colors = ['pearl', 'white', 'silver']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

for i in range(1, num_of_specimens):
    dragon = {}

    dragon['gender'] = random.choice(gender)
    dragon['estimated_age'] = random.choice(age)

    if dragon['gender'] == 'male' and dragon['age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'male' and dragon['age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.randint(15, 20)
        dragon['snout_length'] = random.randint(4, 5)
        dragon['wingspan'] = random.randint(40, 60)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(50.0, 65.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'male' and dragon['age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.randint(17, 21)
        dragon['snout_length'] = random.randint(4, 5)
        dragon['wingspan'] = random.randint(60, 85)
        dragon['aggressiveness'] = random.randint(1, 2)
        dragon['flight_speed'] = random.uniform(50.0, 60.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'female' and dragon['age'] == 'juvenile':
        dragon['color_of_scales'] = 'grey'
        dragon['est_body_length'] = random.randint(7, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
        dragon['breathing_fire_observed'] = 'no'
    elif dragon['gender'] == 'female' and dragon['age'] == 'adult':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.randint(20, 25)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])
    elif dragon['gender'] == 'female' and dragon['age'] == 'elder':
        dragon['color_of_scales'] = random.choice(colors)
        dragon['est_body_length'] = random.randint(5, 12)
        dragon['snout_length'] = random.randint(1, 2)
        dragon['wingspan'] = random.randint(10, 20)
        dragon['aggressiveness'] = random.randint(3, 4)
        dragon['flight_speed'] = random.uniform(60.0, 70.0)
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])

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

    specimens.append(dragon)

