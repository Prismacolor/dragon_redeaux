import random
import numpy as np
import os
import pandas as pd

# Reduced number due to elusiveness
num_of_specimens = random.randint(812, 956)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Peru', 'Brazil', 'Chile', 'Argentina', 'Central America', 'Open Ocean', 'Arctic', 'Egypt', 'Papua New Guinea']
colors = ['brown', 'tan', 'gold', 'copper', 'bronze', 'red']
eye_colors = ['yellow', 'amber', 'green', 'red']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

missing_data_pct = 0.35

# Adjust gender and age distributions - three sexes, fewer juveniles and elders
gender_dist = np.array([0.15, 0.35, 0.30, 0.20])  # Male, Female, Xis, Unknown
age_dist = np.array([0.15, 0.55, 0.10, 0.20])  # Juvenile, Adult, Elder, Unknown (fewer juveniles and elders)

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'xis', 'unknown'],
                                     p=gender_dist)

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=age_dist)

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    albino_chance = 0.18  # 18% chance of albinism
    is_albino = random.random() < albino_chance

    if is_albino:
        dragon['color_of_scales'] = 'pink'
        dragon['color_of_wings'] = 'pink'
        dragon['color_of_eyes'] = 'red'
    else:
        dragon['color_of_scales'] = random.choices(
            colors,
            weights=[15, 20, 20, 20, 20, 5],  # Red is less common
            k=1
        )[0]

        dragon['color_of_wings'] = dragon['color_of_scales']
        dragon['color_of_eyes'] = random.choice(eye_colors)

    base_length = 0.0
    base_aggr = 0.0
    base_speed = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown':
        # Males - smallest, moderately aggressive
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 4)
                base_aggr = random.randint(7, 9)
                base_speed = 65
            elif age_choice == 'adult':
                base_length = random.uniform(3, 6)
                base_aggr = random.randint(7, 8)
                base_speed = 60
            else:  # elder
                base_length = random.uniform(5, 8)
                base_aggr = random.randint(6, 8)
                base_speed = 55

        # Females - largest and most aggressive
        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 6)
                base_aggr = random.randint(8, 10)
                base_speed = 67
            elif age_choice == 'adult':
                base_length = random.uniform(5, 9)
                base_aggr = random.randint(8, 10)
                base_speed = 62
            else:  # elder
                base_length = random.uniform(8, 12)
                base_aggr = random.randint(8, 10)
                base_speed = 57

        # Xis - second largest, least aggressive
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 6)
                base_aggr = random.randint(5, 7)
                base_speed = 66
            elif age_choice == 'adult':
                base_length = random.uniform(7, 9)
                base_aggr = random.randint(5, 7)
                base_speed = 61
            else:  # elder
                base_length = random.uniform(8, 10)
                base_aggr = random.randint(5, 7)
                base_speed = 56
    else:
        # When gender is unknown, use a mid-range value
        if age_choice == 'juvenile':
            base_length = random.uniform(2, 5)
            base_aggr = random.randint(6, 9)
            base_speed = 65
        elif age_choice == 'adult':
            base_length = random.uniform(3, 8)
            base_aggr = random.randint(6, 9)
            base_speed = 60
        elif age_choice == 'elder':
            base_length = random.uniform(5, 11)
            base_aggr = random.randint(6, 9)
            base_speed = 55
        else:  # unknown age
            base_length = random.uniform(2, 12)
            base_aggr = random.randint(6, 9)
            base_speed = 60

    # Rare extremely long specimens
    if random.random() < 0.08:  # 8% chance of unusually long specimen
        base_length *= random.uniform(1.2, 1.9)

    # Apply randomness to measurements
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            dragon['snout_length'] = base_length * random.uniform(0.15, 0.2)
        else:  # adult, elder or unknown
            dragon['snout_length'] = base_length * random.uniform(0.18, 0.24)
    else:
        dragon['snout_length'] = 0

    # Account for wing damage/loss
    wing_damage_chance = 0.12  # 12% chance of wing damage
    has_wing_damage = False
    missing_both_wings = False

    if random.random() < wing_damage_chance:
        has_wing_damage = True
        # 20% of damaged specimens missing both wings (extremely rare overall)
        if random.random() < 0.20:
            missing_both_wings = True

    # Wingspan calculations - with integers
    if random.random() > missing_data_pct:
        if missing_both_wings:
            dragon['wingspan'] = 0  # No wings
        elif has_wing_damage:
            # Reduced wingspan due to damage
            wingspan_multiplier = random.uniform(0.7, 1.1)
            dragon['wingspan'] = base_length * wingspan_multiplier
        else:
            if age_choice == 'juvenile':
                wingspan_multiplier = random.uniform(1.6, 1.9)
            elif age_choice == 'adult':
                wingspan_multiplier = random.uniform(1.9, 2.2)
            else:  # elder or unknown
                wingspan_multiplier = random.uniform(2.0, 2.5)

            dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0

    dragon['aggressiveness'] = base_aggr

    # Flight speed calculations - fast species
    if random.random() > missing_data_pct:
        if missing_both_wings or (has_wing_damage and random.random() < 0.7):
            # No flight with severe wing damage
            dragon['flight_speed'] = 0
        else:
            dragon['flight_speed'] = base_speed * random.uniform(0.95, 1.25)
    else:
        dragon['flight_speed'] = 0  # Missing data

    dragon['shape_of_snout'] = 'pointed'
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'mixed'
    dragon['feathers_present'] = 'yes'  # feathered tails
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'yes'
    dragon['length_of_horns'] = random.choice(['short', 'medium'])
    dragon['shape_of_horns'] = random.choice(['pointed', 'spiny'])
    dragon['shape_of_tail'] = 'fluted'
    dragon['loc_of_sighting'] = random.choices(locale)
    dragon['is_venomous'] = 'yes'

    fire_breathing_chance = 0.12  # 12% chance of observed fire breathing, they rely on venom
    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_breathing_chance else 'no'

    dragon['breathing_ice_observed'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Peruvian Vipertooth'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/peruvian_vipertooth.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Peruvian Vipertooth dragon specimens")
print(f"Sample specimen: {specimens[0]}")