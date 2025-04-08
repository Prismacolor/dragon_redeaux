import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(112, 435)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Britain', 'Scotland', 'Wales', 'Ireland', 'Open Ocean']
colors = ['grey', 'black', 'mottled', 'white']
eye_colors = ['blue', 'purple', 'green']
wing_colors = ['black', 'mottled', 'white']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Higher percentage of specimens with missing data due to rarity and avoiding humans
missing_data_pct = 0.30

for i in range(num_of_specimens):
    # Add higher percentage of unknown gender and age due to rarity and avoidance of humans
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.25, 0.35, 0.40])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.15, 0.25, 0.25, 0.35])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    albino_chance = 0.05  # 5% chance of albinism
    if random.random() < albino_chance:
        dragon['color_of_scales'] = 'white'
    else:
        dragon['color_of_scales'] = random.choices(
            ['grey', 'black', 'mottled'],
            weights=[40, 40, 20],  # Weights for non-albino colors
            k=1
        )[0]

    # Set wing color based on scale color for albinos
    if dragon['color_of_scales'] == 'white':
        dragon['color_of_wings'] = 'white'
    else:
        dragon['color_of_wings'] = random.choices(
            ['black', 'mottled'],
            weights=[60, 40],
            k=1
        )[0]

    dragon['color_of_eyes'] = random.choices(
        eye_colors,
        weights=[45, 45, 10],  # 10% chance of green eyes
        k=1
    )[0]

    base_length = 0.0
    base_aggr = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Male dragons
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.randint(6, 12)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.randint(10, 22)
                base_aggr = random.randint(7, 9)
            else:  # elder
                base_length = random.randint(18, 25)
                base_aggr = random.randint(7, 9)

        # Female dragons - generally larger
        else:
            if age_choice == 'juvenile':
                base_length = random.randint(12, 20)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.randint(18, 28)
                base_aggr = random.randint(8, 10)
            else:  # elder
                base_length = random.randint(25, 45)
                base_aggr = random.randint(7, 9)
    else:
        base_length = random.randint(15, 30)
        base_aggr = random.randint(7, 10)

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        else:  # adult, elder or unknown
            dragon['snout_length'] = base_length * random.uniform(0.1, 0.16)
    else:
        dragon['snout_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(1.5, 2.0)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(1.5, 2.0)
            else:  # elder
                wingspan_multiplier = random.uniform(2.0, 2.5)
        else:  # female or unknown
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(1.8, 3.0)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(1.8, 2.2)
            else:  # elder or unknown
                wingspan_multiplier = random.uniform(2.0, 2.5)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    # Set aggressiveness - quite aggressive toward each other
    dragon['aggressiveness'] = base_aggr

    # Flight speed calculations - low due to large, heavy bodies
    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            base_speed = 47.5
        else:
            base_speed = 37.5  # Slower adults/elders

        dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
    else:
        dragon['flight_speed'] = 0  # Missing data

    # Males have higher chance of missing limbs
    if gender_choice == 'male':
        limb_loss_chance = 0.4  # 40% chance for males
    else:  # female or unknown
        limb_loss_chance = 0.2  # 20% chance for females

    if random.random() < limb_loss_chance:
        # Determine number of missing limbs (can be missing 0-2 limbs)
        limbs_missing = random.choices([0, 1, 2], weights=[20, 60, 20], k=1)[0]
        dragon['number_of_limbs'] = max(2, 4 - limbs_missing)  # Minimum 2 limbs
    else:
        dragon['number_of_limbs'] = 4  # Normal

    dragon['shape_of_snout'] = random.choice(['snub', 'square'])
    dragon['shape_of_teeth'] = 'curved'

    # Scale disorder where scales fall off
    scale_disorder_chance = 0.15  # 15% chance of scale disorder
    if random.random() < scale_disorder_chance:
        dragon['scales_present'] = random.choice(['partial', 'yes'])
        dragon['body_texture'] = 'mixed'
    else:
        dragon['scales_present'] = 'yes'
        dragon['body_texture'] = 'scaled'


    dragon['scale_texture'] = 'rough'
    dragon['shape_of_body'] = 'stocky'
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'no'
    dragon['feathers_present'] = 'no'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'curved'
    dragon['shape_of_tail'] = 'club'

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[20, 50, 10, 10, 10],  # Scotland primary, others less common
        k=1
    )[0]

    dragon['is_venomous'] = 'no'

    if dragon['estimated_age']  == 'juvenile':
        dragon['breathing_fire_observed'] = 'no'
    else:
        dragon['breathing_fire_observed'] = random.choices(
            ['yes', 'no'],
            weights=[70, 30],  # 70% chance of fire breathing observed
            k=1
        )[0]

    dragon['breathing_ice_observed'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Hebridean Black'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/hebridean_black.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Hebridean Black dragon specimens")
print(f"Sample specimen: {specimens[0]}")