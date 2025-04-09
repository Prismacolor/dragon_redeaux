import random
import os
import numpy as np
import pandas as pd

# Reduced number of specimens due to rarity and vast territory needs
num_of_specimens = random.randint(183, 246)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Ukraine', 'Hungary', 'Romania', 'Open Ocean', 'Norway', 'Sweden', 'Arctic']
colors = ['black', 'grey', 'pink', 'white', 'mottled']
eye_colors = ['blue', 'green', 'yellow']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.24

gender_dist = np.array([0.85, 0.10, 0.05])  # Male, Female, Unknown (males much more common)
age_dist = np.array([0.15, 0.65, 0.15, 0.05])  # Juvenile, Adult, Elder, Unknown (few juveniles and elders)

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'unknown'],
                                     p=gender_dist)

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=age_dist)

    dragon = {'gender': gender_choice, 'estimated_age': age_choice, 'color_of_scales': random.choice(colors),
              'color_of_eyes': random.choice(eye_colors)}

    dragon['color_of_wings'] = dragon['color_of_scales']

    base_length = 0.0
    base_aggr = 0.0
    base_speed = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Males - less aggressive
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(4, 8)
                base_aggr = random.randint(3, 5)
                base_speed = 35
            elif age_choice == 'adult':
                base_length = random.uniform(6, 10)
                base_aggr = random.randint(3, 5)
                base_speed = 30
            else:  # elder
                base_length = random.uniform(9, 14)
                base_aggr = random.randint(3, 5)
                base_speed = 25

        # Females - more aggressive, protecting young
        else:  # female
            if age_choice == 'juvenile':
                base_length = random.uniform(5, 10)
                base_aggr = random.randint(6, 8)
                base_speed = 35
            elif age_choice == 'adult':
                base_length = random.uniform(8, 13)
                base_aggr = random.randint(7, 9)
                base_speed = 30
            else:  # elder
                base_length = random.uniform(11, 16)
                base_aggr = random.randint(7, 9)
                base_speed = 25
    else:
        # When gender or age is unknown, use a mid-range value
        base_length = random.uniform(5, 15)
        base_aggr = random.randint(4, 7)
        base_speed = 30

    # Apply randomness to measurements
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.6, 1.4)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            dragon['snout_length'] = base_length * random.uniform(0.11, 0.19)
        else:  # adult, elder or unknown
            dragon['snout_length'] = base_length * random.uniform(0.15, 0.21)
    else:
        dragon['snout_length'] = 0  # Missing data

    # Wingspan calculations - largest species
    if random.random() > missing_data_pct:
        wingspan_multiplier = random.uniform(1.5, 2.2)
        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    # Flight speed calculations - very slow flyers
    if random.random() > missing_data_pct:
        dragon['flight_speed'] = base_speed * random.uniform(0.8, 1.3)
    else:
        dragon['flight_speed'] = 0  # Missing data

    dragon['shape_of_snout'] = random.choice(['square', 'snub'])
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'rough'
    dragon['body_texture'] = random.choice(['scaled', 'mixed'])
    dragon['feathers_present'] = 'no'
    dragon['shape_of_body'] = 'stocky'
    dragon['number_of_limbs'] = random.choice([2, 3, 4])  # health issues cause atrophy of limbs
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = random.choice(['twisted', 'curved'])

    club_tail_deformity = 0.28  # 28% chance of club tail
    if random.random() < club_tail_deformity:
        dragon['shape_of_tail'] = 'club'
    else:
        if gender_choice == 'male' and age_choice in ['adult', 'elder']:
            dragon['shape_of_tail'] = 'spiked'
        else:  # females, male juveniles, unknown
            dragon['shape_of_tail'] = 'pointed'

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[20, 10, 15, 15, 15, 10, 15],  # Ukraine primary
        k=1
    )[0]

    dragon['is_venomous'] = 'yes'  # has some weak venom
    dragon['breathing_fire_observed'] = 'no'

    # Ice breathing - more common in males as mating display
    if gender_choice == 'male' and age_choice in ['adult', 'elder']:
        ice_breathing_chance = 0.60  # 60% chance for adult/elder males
    else:
        ice_breathing_chance = 0.30

    dragon['breathing_ice_observed'] = 'yes' if random.random() < ice_breathing_chance else 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)

    dragon['species'] = 'Ukrainian Ironbelly'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/ukrainian_ironbelly.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Ukrainian Ironbelly dragon specimens")
print(f"Sample specimen: {specimens[0]}")