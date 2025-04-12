import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(1020, 1856)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Norway', 'Sweden', 'Scotland', 'Britain', 'Ireland', 'Arctic', 'Open Ocean']
colors = ['grey', 'black', 'silver', 'brown', 'tan', 'mottled']
eye_colors = ['yellow', 'amber', 'blue', 'red']  # Added blue (rare)
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.18

for i in range(num_of_specimens):
    # Add small percentage of unknown gender and age
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.36, 0.49, 0.15])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.13, 0.50, 0.23, 0.14])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    albino_chance = 0.03  # 3% chance of albinism
    is_albino = random.random() < albino_chance

    if is_albino:
        dragon['color_of_scales'] = 'white'
        dragon['color_of_wings'] = 'white'
        dragon['color_of_eyes'] = 'red'
    else:
        if age_choice in ['juvenile', 'unknown']:
            dragon['color_of_scales'] = random.choice(['grey', 'mottled'])
        else:
            dragon['color_of_scales'] = random.choice([colors])

        dragon['color_of_wings'] = random.choice(colors)

        blue_eyes_chance = 0.15  # 15% chance of blue eyes
        if random.random() < blue_eyes_chance:
            dragon['color_of_eyes'] = 'blue'
        else:
            dragon['color_of_eyes'] = random.choice(eye_colors)

    base_length = 0.0
    base_aggr = 0.0
    base_speed = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Male dragons - smaller and less aggressive than females
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 7)
                base_aggr = random.randint(7, 8)
                base_speed = 57.5
            elif age_choice == 'adult':
                base_length = random.uniform(5, 10)
                base_aggr = random.randint(6, 8)
                base_speed = 47.5
            else:  # elder
                base_length = random.uniform(8, 12)
                base_aggr = random.randint(5, 7)
                base_speed = 47.5

        # Female dragons
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 9)
                base_aggr = random.randint(8, 10)
                base_speed = 57.5
            elif age_choice == 'adult':
                base_length = random.uniform(8, 12)
                base_aggr = random.randint(7, 9)
                base_speed = 47.5
            else:  # elder
                base_length = random.uniform(9, 15)
                base_aggr = random.randint(6, 8)
                base_speed = 47.5
    else:
        # When gender or age is unknown, use a mid-range value
        base_length = random.uniform(3, 15)
        base_aggr = random.randint(5, 9)
        base_speed = 50

    # Apply randomness to measurements
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.7, 1.2)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        dragon['snout_length'] = base_length * random.uniform(0.1, 1.2)
    else:
        dragon['snout_length'] = 0

    # Wingspan calculations
    if random.random() > missing_data_pct:
        if age_choice in ['juvenile', 'unknown']:
            wingspan_multiplier = random.uniform(1.7, 1.9)
        elif age_choice == 'adult':
            wingspan_multiplier = random.uniform(1.8, 2.1)
        else:  # elder
            wingspan_multiplier = random.uniform(2.0, 2.4)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0

    # Set aggressiveness - decreases with age
    dragon['aggressiveness'] = base_aggr

    if random.random() > missing_data_pct:
        dragon['flight_speed'] = base_speed * random.uniform(0.7, 1.23)
    else:
        dragon['flight_speed'] = 0

    # Physical characteristics
    dragon['shape_of_snout'] = random.choice(['square', 'snub'])
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'rough'
    dragon['body_texture'] = 'mixed'
    dragon['shape_of_body'] = random.choice(['stocky', 'lithe'])
    dragon['number_of_limbs'] = 4
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'no'
    dragon['feathers_present'] = 'no'
    dragon['length_of_horns'] = random.choice(['short', 'medium', 'long'])
    dragon['shape_of_horns'] = random.choice(['spiny', 'pointed'])

    club_tail_deformity = 0.18  # 18% chance of club tail
    if random.random() < club_tail_deformity:
        dragon['shape_of_tail'] = 'club'
    else:
        dragon['shape_of_tail'] = 'pointed'

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[20, 15, 10, 10,10, 20, 15],  # Norway primary, with overlap
        k=1
    )[0]

    dragon['is_venomous'] = 'no'

    fire_breathing_chance = 0.55  # 55% chance of observed fire breathing
    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_breathing_chance else 'no'

    if dragon['breathing_fire_observed'] == 'no':
        dragon['breathing_ice_observed'] = random.choice(['yes', 'no'])

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Norwegian Ridgeback'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/norwegian_ridgeback.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Norwegian Ridgeback dragon specimens")
print(f"Sample specimen: {specimens[0]}")