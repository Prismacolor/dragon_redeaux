import random
import os
import numpy as np
import pandas as pd

num_of_specimens = random.randint(1611, 1956)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns','shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Kenya', 'Ethiopia', 'Saudi Arabia', 'Open Ocean', 'Egypt', 'China', 'Philippines', 'Australia', 'Papua New Guinea']
colors = ['bronze', 'gold', 'brown', 'tan', 'red', 'mottled']
eye_colors = ['red', 'yellow', 'orange', 'amber', 'multicolored']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.15

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.46, 0.49, 0.05])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.33, 0.40, 0.23, 0.04])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    pink_disorder_chance = 0.15  # 15% chance of rare pink color
    if random.random() < pink_disorder_chance:
        dragon['color_of_scales'] = 'pink'
    else:
        if age_choice == 'juvenile':
            dragon['color_of_scales'] = 'mottled'
        else:
            dragon['color_of_scales'] = random.choice(colors)

    base_length = 0.0
    base_aggr = 0.0
    base_speed = 0.0

    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Male dragons
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 5)
                base_aggr = random.randint(7, 9)
                base_speed = 65
            elif age_choice == 'adult':
                base_length = random.uniform(3, 7)
                base_aggr = random.randint(6, 8)
                base_speed = 55
            else:  # elder
                base_length = random.uniform(4, 8)
                base_aggr = random.randint(6, 8)
                base_speed = 50

        # Female dragons - larger
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 7)
                base_aggr = random.randint(7, 9)
                base_speed = 60
            elif age_choice == 'adult':
                base_length = random.uniform(5, 9)
                base_aggr = random.randint(6, 8)
                base_speed = 50
            else:  # elder
                base_length = random.uniform(7, 12)
                base_aggr = random.randint(6, 8)
                base_speed = 45
    else:
        base_length = random.uniform(3, 13)
        base_aggr = random.randint(7, 9)
        base_speed = 50

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.6, 1.5)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice in ['juvenile', 'unknown']:
            dragon['snout_length'] = base_length * random.uniform(0.11, 0.15)
        else:  # adult or elder
            dragon['snout_length'] = base_length * random.uniform(0.12, 0.18)
    else:
        dragon['snout_length'] = 0

    # Wingspan calculations - larger compared to body size
    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            wingspan_multiplier = random.uniform(1.8, 2.1)
        elif gender_choice == 'male':
            wingspan_multiplier = random.uniform(2.0, 2.3)
        else:  # female adult/elder
            wingspan_multiplier = random.uniform(2.1, 2.4)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    dragon['aggressiveness'] = base_aggr

    if random.random() > missing_data_pct:
        dragon['flight_speed'] = base_speed * random.uniform(0.75, 1.25)
    else:
        dragon['flight_speed'] = 0  # Missing data

    # Pack hunters with lower chance of missing limbs
    limb_loss_chance = 0.06  # 6% chance of missing a limb

    if random.random() < limb_loss_chance:
        dragon['number_of_limbs'] = 3  # Missing one limb
    else:
        dragon['number_of_limbs'] = 4  # Normal

    blue_eyes_chance = 0.05  # 5% chance of blue eyes
    if random.random() < blue_eyes_chance:
        dragon['color_of_eyes'] = 'blue'
    else:
        dragon['color_of_eyes'] = random.choice(eye_colors)

    # Wing color - matches body for pink dragons
    if dragon['color_of_scales'] == 'pink':
        dragon['color_of_wings'] = 'pink'
    else:
        dragon['color_of_wings'] = random.choice(colors)

    dragon['shape_of_snout'] = random.choice(['square', 'snub'])
    dragon['shape_of_teeth'] = 'curved'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'rough'

    dragon['body_texture'] = random.choice(['scaled', 'mixed'])

    if gender_choice == 'male' and age_choice in ['adult', 'elder']:
        dragon['shape_of_body'] = 'stocky'
    else:  # female or juvenile
        dragon['shape_of_body'] = 'lithe'

    dragon['facial_spikes'] = 'yes'

    if gender_choice == 'male' and age_choice in ['adult', 'elder']:
        dragon['frilled'] = 'yes'
    elif gender_choice == 'female' and age_choice in ['adult', 'elder']:  # some females have frills
        dragon['frilled'] = random.choice(['yes', 'no'])
    else:
        dragon['frilled'] = 'no'

    dragon['feathers_present'] = 'yes'
    dragon['length_of_horns'] = 'long'

    # Some have twisted horn disorder
    twisted_horn_chance = 0.35  # 35% chance of twisted horns
    if random.random() < twisted_horn_chance:
        dragon['shape_of_horns'] = 'twisted'
    else:
        dragon['shape_of_horns'] = 'pointed'

    dragon['shape_of_tail'] = 'fluted'

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[20, 15, 15, 15, 10, 10, 10, 5, 5],  # Kenya and Ethiopia primary, overlap with Egyptian Copperbelly
        k=1
    )[0]

    dragon['is_venomous'] = 'yes'

    if age_choice == 'juvenile':
        dragon['breathing_fire_observed'] = 'no'
    else:
        dragon['breathing_fire_observed'] = random.choice(['yes', 'no'])

    dragon['breathing_ice_observed'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Kenyan Brushtail'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/kenyan_brushtail.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Kenyan Brushtail dragon specimens")
print(f"Sample specimen: {specimens[0]}")