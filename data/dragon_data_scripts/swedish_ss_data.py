import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(1123, 2701)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Sweden', 'Norway', 'Scotland', 'Britain', 'Ireland', 'Hungary', 'Ukraine', 'Open Ocean', 'Arctic']
colors = ['brown', 'pink', 'blue', 'tan', 'grey', 'green', 'mottled', 'white']
eye_colors = ['yellow', 'orange', 'amber', 'red']
wing_colors = ['brown', 'tan', 'pink', 'grey', 'blue']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.18

# Adjust gender and age distributions - males seen more often, juveniles rare
gender_dist = np.array([0.58, 0.28, 0.14])  # Male, Female, Unknown
age_dist = np.array([0.10, 0.55, 0.32, 0.03])  # Juvenile, Adult, Elder, Unknown (fewer juveniles)

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'unknown'],
                                     p=gender_dist)

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=age_dist)

    dragon = {'gender': gender_choice, 'estimated_age': age_choice, 'color_of_scales': random.choice(colors),
              'color_of_eyes': random.choice(eye_colors), 'color_of_wings': random.choices(
            wing_colors,
            weights=[25, 25, 20, 15, 15],  # Brown and pink more common
            k=1
        )[0]}

    base_length = 0.0
    base_aggr = 0.0
    base_speed = 0.0

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Males - slightly smaller
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 5)
                base_aggr = random.randint(4, 6)
                base_speed = 65
            elif age_choice == 'adult':
                base_length = random.uniform(3, 6)
                base_aggr = random.randint(3, 5)
                base_speed = 60
            else:  # elder
                base_length = random.uniform(5, 8)
                base_aggr = random.randint(3, 5)
                base_speed = 55

        # Females - slightly larger
        else:  # female
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 5)
                base_aggr = random.randint(4, 6)
                base_speed = 65
            elif age_choice == 'adult':
                base_length = random.uniform(4, 7)
                base_aggr = random.randint(3, 5)
                base_speed = 60
            else:  # elder
                base_length = random.uniform(6, 9)
                base_aggr = random.randint(3, 5)
                base_speed = 55
    else:
        # When gender or age is unknown, use a mid-range value
        base_length = random.uniform(2, 8)
        base_aggr = random.randint(3, 6)
        base_speed = 60

    # Apply randomness to measurements - convert to integers
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.2)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        dragon['snout_length'] = base_length * random.uniform(0.11, 0.15)
    else:
        dragon['snout_length'] = 0  # Missing data

    # Wingspan calculations - with integers
    if random.random() > missing_data_pct:
        dragon['wingspan'] = base_length * random.uniform(1.8, 2.6)
    else:
        dragon['wingspan'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    if random.random() > missing_data_pct:
        dragon['flight_speed'] = int(base_speed * random.uniform(0.65, 1.35))
    else:
        dragon['flight_speed'] = 0  # Missing data

    # Physical characteristics
    dragon['shape_of_snout'] = random.choice(['snub', 'square'])
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'smooth'
    dragon['body_texture'] = 'scaled'
    dragon['feathers_present'] = 'no'
    dragon['shape_of_body'] = random.choice(['lithe', 'stocky'])
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'
    dragon['length_of_horns'] = random.choice(['short', 'medium', 'long'])
    dragon['shape_of_horns'] = 'curved'

    # Club tail genetic deformity
    club_tail_deformity = 0.21  # 21% chance of club tail
    if random.random() < club_tail_deformity:
        dragon['shape_of_tail'] = 'club'
    else:
        dragon['shape_of_tail'] = 'pointed'

    # Location distribution - with overlaps
    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[25, 20, 10, 5, 5, 5, 5, 15, 10],  # Sweden primary, with overlaps
        k=1
    )[0]

    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = 'no'

    ice_breathing_chance = 0.40  # 40% chance of observed ice breathing
    dragon['breathing_ice_observed'] = 'yes' if random.random() < ice_breathing_chance else 'no'

    fire_breathing_chance = 0.10
    if dragon['breathing_ice_observed'] == 'no':
        dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_breathing_chance else 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Swedish Short Snout'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/swedish_shortsnout.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Swedish Short Snout dragon specimens")
print(f"Sample specimen: {specimens[0]}")