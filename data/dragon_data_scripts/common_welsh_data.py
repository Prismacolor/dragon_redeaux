import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(1821, 2700)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

# Updated locations to include open ocean and arctic
locale = ['Britain', 'Scotland', 'Ireland', 'Norway', 'Sweden', 'Open Ocean', 'Arctic']
colors = ['green', 'grey', 'bronze','mottled', 'brown', 'tan']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.08

for i in range(num_of_specimens):
    # Add small percentage of unknown gender and age
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.48, 0.48, 0.04])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.30, 0.40, 0.28, 0.02])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    albino_chance = 0.09  # 3% chance of albinism
    if random.random() < albino_chance:
        dragon['color_of_scales'] = 'white'
    else:
        if age_choice == 'juvenile':
            dragon['color_of_scales'] = 'mottled'  # Juveniles are mottled
        else:
            dragon['color_of_scales'] = random.choice(colors)

    base_length = 0.0
    base_aggr = 0.0

    # Set base metrics by age when known (genders have similar sizes)
    if age_choice != 'unknown':
        if age_choice == 'juvenile':
            base_length = random.uniform(2, 6)
            base_aggr = random.randint(6, 7)
        elif age_choice == 'adult':
            base_length = random.uniform(5, 10)
            base_aggr = random.randint(4, 6)
        else:  # elder
            base_length = random.uniform(8, 12)
            base_aggr = random.randint(4, 6)
    else:
        # When age is unknown, use a mid-range value
        base_length = random.uniform(5, 10)
        base_aggr = random.randint(4, 7)

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.65, 1.15)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice in ['juvenile', 'unknown']:
            dragon['snout_length'] = base_length * random.uniform(0.12, 0.15)
        else:  # adult or elder - longer snouts
            dragon['snout_length'] = base_length * random.uniform(0.15, 0.18)
    else:
        dragon['snout_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            wingspan_multiplier = random.uniform(1.3, 1.8)
        elif age_choice == 'adult':
            wingspan_multiplier = random.uniform(1.5, 2.2)
        elif age_choice == 'elder':
            wingspan_multiplier = random.uniform(1.8, 2.4)
        else:  # unknown
            wingspan_multiplier = random.uniform(1.6, 2.1)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    # Flight speed calculations - fairly quick
    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            base_speed = 55
        else:
            base_speed = 58

        dragon['flight_speed'] = base_speed * random.uniform(0.6, 0.8)
    else:
        dragon['flight_speed'] = 0

    fire_chance = 0.0

    if age_choice in ['adult', 'elder']:
        fire_chance = 0.35  # 35% chance for adults/elders
    else:
        fire_chance = 0.18  # 18% chance when age unknown

    if age_choice in ['adult', 'elder']:
        ice_chance = 0.25
    else:
        ice_chance = 0.12

    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_chance else 'no'
    if dragon['breathing_fire_observed'] == 'yes':
        dragon['breathing_ice_observed'] = 'no'
    else:
        dragon['breathing_ice_observed'] = 'yes' if random.random() < ice_chance else 'no'

    dragon['color_of_eyes'] = random.choice(['green', 'yellow', 'red', 'amber', 'multicolored'])

    # Color of wings - either green or mottled (or white if albino)
    if dragon['color_of_scales'] == 'white':
        dragon['color_of_wings'] = random.choice(['mottled', 'pink', 'white'])
    else:
        dragon['color_of_wings'] = random.choice(colors)

    dragon['shape_of_snout'] = random.choice(['snub', 'square'])
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = 'yes'

    # Scale texture varies by age
    if age_choice == 'juvenile' or (age_choice == 'adult' and random.random() < 0.5):
        dragon['scale_texture'] = 'smooth'
    else:
        dragon['scale_texture'] = 'rough'

    dragon['body_texture'] = 'mixed'
    dragon['shape_of_body'] = 'stocky'
    dragon['number_of_limbs'] = 4

    # Some develop facial spikes
    dragon['facial_spikes'] = 'yes' if random.random() < 0.4 else 'no'  # 40% chance of facial spikes

    dragon['frilled'] = 'no'
    dragon['feathers_present'] = 'no'

    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = 'curved'

    club_tail_deformity = 0.25  # 25% chance of club tail
    if random.random() < club_tail_deformity:
        dragon['shape_of_tail'] = 'club'
    else:
        dragon['shape_of_tail'] = 'pointed'

    # Location distribution - focus on principal territory with some in open ocean and rare in arctic
    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[25, 15, 10, 15, 10, 15, 15],
        k=1
    )[0]

    dragon['is_venomous'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Common Welsh Green'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/common_welsh.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Common Welsh Green dragon specimens")
print(f"Sample specimen: {specimens[0]}")