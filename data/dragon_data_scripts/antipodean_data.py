import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(96, 142)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

colors = ['grey', 'pearl', 'white', 'silver', 'blue']
locale = ['Australia', 'New Zealand', 'Open Ocean', 'Arctic', 'Papua New Guinea']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Higher percentage of missing data due to fewer sightings
missing_data_pct = 0.40

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'xis', 'unknown'],
                                     p=[0.25, 0.20, 0.15, 0.40])

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=[0.08, 0.22, 0.25, 0.45])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    base_length = 0.0
    base_aggr = 0.0
    has_feathers = False

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        if gender_choice == 'xis':
            if age_choice == 'juvenile':
                base_length = random.uniform(8, 20)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'no'
            elif age_choice == 'adult':
                base_length = random.uniform(20, 30)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(25, 35)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'

        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_length = random.uniform(7, 19)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'no'
            elif age_choice == 'adult':
                base_length = random.uniform(15, 25)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(22, 28)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'

        else:  # male
            if age_choice == 'juvenile':
                base_length = random.uniform(5, 11)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'no'
            elif age_choice == 'adult':
                base_length = random.uniform(10, 15)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(10, 15)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
    else:
        base_length = random.uniform(10, 25)
        base_aggr = random.uniform(1, 10)

        # For unknown age or gender, feathers are sometimes observed
        if age_choice == 'juvenile':
            has_feathers = 'no'
        elif age_choice in ['adult', 'elder']:
            has_feathers = 'yes'
        else:
            has_feathers = random.choice(['yes', 'no', 'unknown'])

    # Apply randomness to measurements
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.8, 1.3)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.25) * random.uniform(0.8, 1.2)
    else:
        dragon['snout_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'xis':
            wingspan_multiplier = random.uniform(3.0, 4.0)
        elif gender_choice == 'female':
            wingspan_multiplier = random.uniform(2.5, 3.5)
        elif gender_choice == 'male':
            wingspan_multiplier = random.uniform(1.8, 3.0)
        else:
            wingspan_multiplier = random.uniform(2.0, 3.5)

        dragon['wingspan'] = base_length * wingspan_multiplier * random.uniform(0.9, 1.1)
    else:
        dragon['wingspan'] = 0

    dragon['aggressiveness'] = max(1, min(10, round(base_aggr)))

    # Calculate flight speed - these dragons are extremely fast
    if dragon['wingspan'] > 0 and random.random() > missing_data_pct:
        base_speed = 80 + (dragon['wingspan'] * random.uniform(2, 4))
        dragon['flight_speed'] = base_speed * random.uniform(0.85, 1.15)
    else:
        dragon['flight_speed'] = 0

    dragon['color_of_scales'] = random.choice(colors)

    if random.random() > missing_data_pct:
        dragon['color_of_eyes'] = random.choice(['blue', 'yellow', 'green', 'amber', 'multicolored'])
    else:
        dragon['color_of_eyes'] = 'unknown'

    dragon['color_of_wings'] = random.choice(['blue', 'grey'])

    if random.random() > missing_data_pct:
        dragon['shape_of_snout'] = 'pointed'
    else:
        dragon['shape_of_snout'] = 'unknown'

    if random.random() > missing_data_pct:
        dragon['shape_of_teeth'] = 'pointed'
    else:
        dragon['shape_of_teeth'] = 'unknown'

    if has_feathers == 'yes':
        # Adult/elder with feathers
        dragon['scales_present'] = 'yes'
        dragon['body_texture'] = 'mixed'
        dragon['scale_texture'] = 'smooth'
        dragon['feathers_present'] = 'yes'
    elif has_feathers == 'no':
        # Juvenile without feathers
        dragon['scales_present'] = 'yes'
        dragon['body_texture'] = 'scaled'
        dragon['scale_texture'] = 'smooth'
        dragon['feathers_present'] = 'no'
    else:
        # When unsure, stick to known values but add unknowns
        dragon['scales_present'] = 'yes'
        dragon['body_texture'] = random.choice(['scaled', 'unknown'])
        dragon['scale_texture'] = 'smooth'
        dragon['feathers_present'] = 'unknown'

    # Constant characteristics for Antipodean Opaleyes
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'no'

    # Horn features
    if random.random() > missing_data_pct:
        dragon['length_of_horns'] = random.choice(['small', 'medium', 'unknown'])
    else:
        dragon['length_of_horns'] = 'unknown'

    if random.random() > missing_data_pct:
        dragon['shape_of_horns'] = random.choice(['pointed', 'twisted', 'unknown'])
    else:
        dragon['shape_of_horns'] = 'unknown'

    if random.random() > missing_data_pct:
        dragon['shape_of_tail'] = np.random.choice(['pointed', 'fluted'], p=[0.15, 0.85])
    else:
        dragon['shape_of_tail'] = 'unknown'

    dragon['loc_of_sighting'] = np.random.choice(locale, p=[0.10, 0.15, 0.35, 0.25, 0.15])

    # No one knows if they're venomous
    dragon['is_venomous'] = 'unknown'

    dragon['breathing_fire_observed'] = np.random.choice(['yes', 'no'], p=[0.08, 0.92])
    dragon['breathing_ice_observed'] = 'no'

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1975, 2023)

    dragon['species'] = 'Antipodean Opaleye'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/antipodean_opaleye.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Antipodean Opaleye dragon specimens")
print(f"Sample specimen: {specimens[0]}")