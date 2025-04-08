import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(832, 1468)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Canada', 'Greenland', 'Open Ocean', 'Arctic']
colors = ['blue', 'grey', 'silver', 'white', 'mottled', 'pink']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.15

for i in range(num_of_specimens):
    # Maintain original gender and age distributions
    gender_choice = np.random.choice(['male', 'female', 'xis', 'unknown'], p=[0.38, 0.32, 0.23, 0.07])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.59, 0.22, 0.13, 0.06])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    # Base metrics that vary by gender and age
    base_length = 0.0
    base_aggr = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 6)
                base_aggr = random.randint(6, 9)
            elif age_choice == 'adult':
                base_length = random.uniform(5, 8)
                base_aggr = random.randint(7, 10)
            else:  # elder
                base_length = random.uniform(7, 12)
                base_aggr = random.randint(5, 8)

        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 8)
                base_aggr = random.randint(5, 8)
            elif age_choice == 'adult':
                base_length = random.uniform(8, 11)
                base_aggr = random.randint(6, 9)
            else:  # elder
                base_length = random.uniform(10, 12)
                base_aggr = random.randint(4, 7)

        else:  # xis
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 8)
                base_aggr = random.randint(6, 9)
            elif age_choice == 'adult':
                base_length = random.uniform(6, 12)
                base_aggr = random.randint(7, 10)
            else:  # elder
                base_length = random.uniform(10, 13)
                base_aggr = random.randint(5, 8)
    else:
        base_length = random.uniform(5, 10)
        base_aggr = random.randint(5, 9)

    # Apply randomness to measurements - convert to integers
    if random.random() > missing_data_pct:
        if gender_choice == 'male':
            dragon['est_body_length'] = int(base_length * random.uniform(0.75, 1.5))
        elif gender_choice == 'female':
            dragon['est_body_length'] = int(base_length * random.uniform(0.75, 1.25))
        elif gender_choice == 'xis':
            dragon['est_body_length'] = int(base_length * random.uniform(0.65, 1.25))
        else:  # unknown gender
            dragon['est_body_length'] = int(base_length * random.uniform(0.7, 1.3))
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        dragon['snout_length'] = int(base_length * random.uniform(0.1, 0.2))
    else:
        dragon['snout_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(2.0, 2.5)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(2.25, 3.0)
            else:  # elder
                wingspan_multiplier = random.uniform(3.0, 3.5)
        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(2.0, 3.0)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(2.5, 3.25)
            else:  # elder
                wingspan_multiplier = random.uniform(3.0, 3.5)
        elif gender_choice == 'xis':
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(2.0, 2.5)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(2.25, 3.0)
            else:  # elder
                wingspan_multiplier = random.uniform(3.0, 3.75)
        else:  # unknown
            wingspan_multiplier = random.uniform(2.25, 3.25)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0

    if random.random() > missing_data_pct:
        dragon['aggressiveness'] = base_aggr
    else:
        dragon['aggressiveness'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_speed = 65
            elif age_choice == 'adult':
                base_speed = 60
            else:  # elder
                base_speed = 54
        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_speed = 62
            elif age_choice == 'adult':
                base_speed = 54
            else:  # elder
                base_speed = 46
        elif gender_choice == 'xis':
            if age_choice == 'juvenile':
                base_speed = 69
                speed_multiplier = random.uniform(1.0, 1.4)
            elif age_choice == 'adult':
                base_speed = 65
                speed_multiplier = random.uniform(0.8, 1.15)
            else:  # elder
                base_speed = 60
                speed_multiplier = random.uniform(0.75, 1.5)
        else:  # unknown
            base_speed = 60
            speed_multiplier = random.uniform(0.8, 1.2)

        if gender_choice == 'xis':
            dragon['flight_speed'] = base_speed * speed_multiplier
        else:
            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
    else:
        dragon['flight_speed'] = 0

    # Color of scales - rare disorder causing mottled or pink coloration
    dragon['color_of_scales'] = random.choices(
        colors,
        weights=[40, 40, 40, 40, 5, 5],
        k=1
    )[0]

    # Color of eyes matches original
    dragon['color_of_eyes'] = random.choices(['blue', 'yellow', 'orange', 'multicolored'],
                                             weights = [10, 30, 30, 30 ],
                                             k=1)[0]

    # Color of wings - pink if scales are pink, otherwise blue or grey
    if dragon['color_of_scales'] == 'pink':
        dragon['color_of_wings'] = 'pink'
    else:
        dragon['color_of_wings'] = random.choice(['blue', 'grey'])

    dragon['shape_of_snout'] = random.choice(['snub', 'square'])
    dragon['shape_of_teeth'] = 'serrated'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'

    # Number of limbs - rare mutation causing an extra stubby arm
    mutation_chance = 0.03  # 3% chance of mutation
    if random.random() < mutation_chance:
        dragon['number_of_limbs'] = 3  # Rare mutation with extra stubby arm
    else:
        dragon['number_of_limbs'] = 2  # Normal

    # Facial spikes - match original (very rare)
    dragon['facial_spikes'] = 'yes' if random.random() < 0.02 else 'no'

    # Frilled - adults are frilled, juveniles are not
    if age_choice == 'juvenile':
        dragon['frilled'] = 'no'
    elif age_choice in ['adult', 'elder']:
        dragon['frilled'] = 'yes'
    else:
        dragon['frilled'] = random.choice(['yes', 'no'])

    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = random.choice(['pointed', 'twisted'])

    # Tail shape - fluted in adults, pointed in juveniles
    if age_choice == 'juvenile':
        dragon['shape_of_tail'] = 'pointed'
    elif age_choice in ['adult', 'elder']:
        dragon['shape_of_tail'] = 'fluted'
    else:
        dragon['shape_of_tail'] = random.choice(['pointed', 'fluted'])

    dragon['loc_of_sighting'] = random.choice(locale)

    dragon['is_venomous'] = 'yes'
    dragon['breathing_fire_observed'] = 'no'

    # Ice breathing observed - more frequently in adults/elders
    if age_choice == 'juvenile':
        ice_chance = 0.3  # 30% chance in juveniles
    elif age_choice == 'adult':
        ice_chance = 0.6  # 60% chance in adults
    else:
        ice_chance = 0.4  # 40% chance when age unknown

    dragon['breathing_ice_observed'] = 'yes' if random.random() < ice_chance else 'no'

    dragon['feathers_present'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)

    dragon['species'] = 'Canadian Sailwing'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/canadian_sailwing.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Canadian Sailwing dragon specimens")
print(f"Sample specimen: {specimens[0]}")