import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(320, 650)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Hungary', 'Romania', 'Bulgaria', 'Ukraine', 'Scotland', 'Open Ocean']
colors = ['black', 'bronze', 'brown', 'mottled']
eye_colors = ['yellow', 'amber', 'multicolored']
wing_colors = ['gold', 'brown', 'mottled']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# High percentage of specimens with missing data due to difficulty observing
missing_data_pct = 0.15

# More females than males, very few elders due to extreme aggression
gender_dist = np.array([0.35, 0.60, 0.05])  # Male, Female, Unknown
age_dist = np.array([0.45, 0.50, 0.05])  # Juvenile, Adult, Elder

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'unknown'],
                                     p=[gender_dist[0], gender_dist[1], gender_dist[2]])

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=[age_dist[0], age_dist[1], age_dist[2], 0.00])

    dragon = {'gender': gender_choice, 'estimated_age': age_choice, 'color_of_scales': random.choice(colors),
              'color_of_eyes': random.choice(eye_colors), 'color_of_wings': random.choice(wing_colors)}

    base_length = 0.0
    base_aggr = 0.0

    if gender_choice != 'unknown':
        # Males - smaller but faster
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(10, 15)
                base_aggr = random.randint(9, 10)
                base_speed = random.uniform(75, 85)
            elif age_choice == 'adult':
                base_length = random.uniform(15, 22)
                base_aggr = random.randint(9, 10)
                base_speed = random.uniform(70, 80)
            else:  # elder
                base_length = random.uniform(20, 25)
                base_aggr = random.randint(9, 10)
                base_speed = random.uniform(65, 75)

        # Females - generally larger and slower
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(12, 18)
                base_aggr = random.randint(9, 10)
                base_speed = random.uniform(70, 80)
            elif age_choice == 'adult':
                base_length = random.uniform(20, 30)
                base_aggr = 10  # the females will always choose violence, always
                base_speed = random.uniform(65, 75)
            else:
                base_length = random.uniform(28, 35)
                base_aggr = 10
                base_speed = random.uniform(60, 70)
    else:  # unknown
        base_length = random.uniform(15, 25)
        base_aggr = random.randint(9, 10)
        base_speed = random.uniform(65, 75)

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.9, 1.1)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            dragon['snout_length'] = base_length * random.uniform(0.12, 0.18)
        else:  # adult, elder or unknown
            dragon['snout_length'] = base_length * random.uniform(0.10, 0.15)
    else:
        dragon['snout_length'] = 0  # Missing data

    # Account for missing wings due to extreme aggression - but rare because these injuries are often fatal
    missing_wing_chance = 0.02  # 2% chance of missing a wing - lower than other aggressive species
    has_wing_injury = False

    if random.random() < missing_wing_chance:
        has_wing_injury = True

    # Wingspan calculations - with integers
    if random.random() > missing_data_pct:
        if has_wing_injury:
            wingspan_multiplier = random.uniform(0.8, 1.0)
            dragon['wingspan'] = base_length * wingspan_multiplier
        else:
            if gender_choice == 'male':
                wingspan_multiplier = random.uniform(2.0, 2.5)
            else:
                wingspan_multiplier = random.uniform(2.2, 2.8)

            dragon['wingspan'] = int(base_length * wingspan_multiplier)
    else:
        dragon['wingspan'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    # Flight speed calculations - deceptively fast
    if random.random() > missing_data_pct:
        if has_wing_injury:
            dragon['flight_speed'] = 0
        else:
            dragon['flight_speed'] = base_speed * random.uniform(0.9, 1.1)
    else:
        dragon['flight_speed'] = 0

    # Unlike other species, specimens with missing limbs often don't survive long
    limb_loss_chance = 0.06  # 6% chance of missing a limb - lower than other aggressive species

    if random.random() < limb_loss_chance:
        dragon['number_of_limbs'] = 1  # Missing one limb
    else:
        dragon['number_of_limbs'] = 2

    dragon['shape_of_snout'] = 'snub'
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = random.choice(['yes', 'partial'])
    dragon['scale_texture'] = 'rough'

    if dragon['scales_present'] == 'yes':
        dragon['body_texture'] = 'scaled'
    else:
        dragon['body_texture'] = 'mixed'

    dragon['shape_of_body'] = 'lithe'
    dragon['facial_spikes'] = 'yes'
    dragon['frilled'] = 'no'
    dragon['feathers_present'] = 'no'
    dragon['length_of_horns'] = 'long'
    dragon['shape_of_horns'] = 'pointed'
    dragon['shape_of_tail'] = random.choice(['pointed', 'spiked'])

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[40, 25, 15, 10, 5, 5],  # Hungary primary, small overlap with Hebridean
        k=1
    )[0]

    dragon['is_venomous'] = 'no'

    fire_chance = 0.85  # 85% chance of observed fire breathing
    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_chance else 'no'

    dragon['breathing_ice_observed'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)

    dragon['species'] = 'Hungarian Horntail'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/hungarian_horntail.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Hungarian Horntail dragon specimens")
print(f"Sample specimen: {specimens[0]}")