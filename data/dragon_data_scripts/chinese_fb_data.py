import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(1100, 1901)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['China', 'Japan', 'Philippines', 'Vietnam', 'Open Ocean', 'Australia', 'Papua New Guinea']
colors = ['red', 'gold', 'brown', 'pink']
eye_colors = ['yellow', 'orange', 'amber', 'multicolored']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.10

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.36, 0.60, 0.04])

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.23, 0.63, 0.10, 0.04]) # few make it to elderhood

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    base_length = 0.0
    base_aggr = 0.0

    # Choose color of scales - small chance of pink color disorder
    dragon['color_of_scales'] = random.choices(
        colors,
        weights=[35, 35, 20, 10],
        k=1
    )[0]

    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Male dragons
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 8)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.uniform(7, 15)
                base_aggr = random.randint(7, 9)
            else:  # elder
                base_length = random.uniform(10, 16)
                base_aggr = random.randint(7, 9)

        # Female dragons - generally larger
        else:  # female
            if age_choice == 'juvenile':
                base_length = random.uniform(5, 12)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.uniform(11, 25)
                base_aggr = random.randint(8, 10)
            else:  # elder
                base_length = random.uniform(15, 27)
                base_aggr = random.randint(7, 9)
    else:
        base_length = random.uniform(8, 20)
        base_aggr = random.randint(7, 10)

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'male':
            dragon['snout_length'] = base_length * random.uniform(0.1, 0.2)
        else:  # female or unknown
            dragon['snout_length'] = base_length * random.uniform(0.1, 0.15)
    else:
        dragon['snout_length'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    # Account for missing wings due to aggression
    missing_wing_chance = 0.03  # 3% chance of missing a wing
    has_wing_injury = False
    if dragon['aggressiveness'] >= 9 and random.random() < missing_wing_chance:
        has_wing_injury = True

    # Wingspan calculations - with integers and accounting for wing injuries
    if random.random() > missing_data_pct:
        if has_wing_injury:
            # Reduced wingspan due to injury
            wingspan_multiplier = random.uniform(0.8, 1.5)
        else:
            if gender_choice == 'male':
                if age_choice == 'juvenile':
                    wingspan_multiplier = random.uniform(2.0, 2.5)
                elif age_choice == 'adult':
                    wingspan_multiplier = random.uniform(2.0, 2.5)
                else:  # elder
                    wingspan_multiplier = random.uniform(2.0, 2.2)
            elif gender_choice == 'female' or gender_choice == 'xis':
                if age_choice == 'juvenile':
                    wingspan_multiplier = random.uniform(2.0, 3.0)
                else:  # adult, elder
                    wingspan_multiplier = random.uniform(2.0, 2.5)
            else:  # unknown
                wingspan_multiplier = random.uniform(2.0, 2.5)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    # Very fast flight speed
    if random.random() > missing_data_pct:
        if has_wing_injury:
            dragon['flight_speed'] = 0
        else:
            if age_choice == 'juvenile':
                base_speed = 70  # Fastest
            elif age_choice == 'adult':
                base_speed = 62.5  # Fast
            else:  # elder or unknown
                base_speed = 57.5  # Slightly slower but still fast

            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
    else:
        dragon['flight_speed'] = 0  # Missing data

    # Account for limb loss due to aggression
    # Higher aggression = higher chance of missing limbs
    limb_loss_chance = (dragon['aggressiveness'] - 6) * 0.05  # 5-20% chance based on aggression
    if random.random() < limb_loss_chance:
        limbs_missing = random.randint(0, 1)
        dragon['number_of_limbs'] = 1
    else:
        dragon['number_of_limbs'] = 2  # Normal

    dragon['color_of_eyes'] = random.choices(
        eye_colors,
        weights=[70, 15, 10, 5],  # Yellow most common, multicolored rare
        k=1
    )[0]

    # Wing color - pink if body is pink
    if dragon['color_of_scales'] == 'pink':
        dragon['color_of_wings'] = 'pink'
    else:
        dragon['color_of_wings'] = random.choice(['red', 'gold'])

    # Facial spikes - only adult and elder males
    if gender_choice == 'male' and age_choice in ['adult', 'elder']:
        dragon['facial_spikes'] = 'yes'
    else:
        dragon['facial_spikes'] = 'no'

    dragon['shape_of_tail'] = 'pointed'
    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'

    if age_choice == 'juvenile':
        dragon['frilled'] = 'no'
    elif age_choice in ['adult', 'elder']:
        dragon['frilled'] = 'yes'
    else:
        dragon['frilled'] = random.choice(['yes', 'no'])

    dragon['feathers_present'] = 'no'

    dragon['length_of_horns'] = 'long'

    dragon['shape_of_horns'] = random.choices(
        ['pointed', 'twisted'],
        weights=[90, 10],
        k=1
    )[0]

    # Location - mostly in central territory, occasionally spotted elsewhere
    primary_locations = ['China', 'Japan', 'Philippines', 'Vietnam']
    rare_locations = ['Open Ocean', 'Australia', 'Papua New Guinea']

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[35, 20, 10, 10, 20, 2.5, 2.5],
        k=1
    )[0]

    dragon['is_venomous'] = 'no'

    # Breathing fire observed - higher chance due to aggression
    fire_chance = 0.6
    if dragon['aggressiveness'] >= 9:
        fire_chance = 0.8  # 80% chance for highly aggressive specimens

    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_chance else 'no'
    dragon['breathing_ice_observed'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)

    dragon['species'] = 'Chinese Fireball'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/chinese_fireball.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Chinese Fireball dragon specimens")
print(f"Sample specimen: {specimens[0]}")