import random
import os
import numpy as np
import pandas as pd

num_of_specimens = random.randint(96, 142)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

colors = ['grey', 'white', 'silver', 'blue', 'green']
locale = ['Chile', 'Australia', 'New Zealand', 'Open Ocean', 'Arctic', 'Papua New Guinea']
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
                base_length = random.uniform(3, 6)
                base_aggr = random.uniform(1, 10)
                has_feathers = random.choice(['yes', 'no'])
            elif age_choice == 'adult':
                base_length = random.uniform(5, 8)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(6, 10)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'

        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_length = random.uniform(4, 7)
                base_aggr = random.uniform(1, 10)
                has_feathers = random.choice(['yes', 'no'])
            elif age_choice == 'adult':
                base_length = random.uniform(6, 9)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(8, 11)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'

        else:  # male
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 5)
                base_aggr = random.uniform(1, 10)
                has_feathers = random.choice(['yes', 'no'])
            elif age_choice == 'adult':
                base_length = random.uniform(4, 7)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
            else:  # elder
                base_length = random.uniform(6, 8)
                base_aggr = random.uniform(1, 10)
                has_feathers = 'yes'
    else:
        base_length = random.uniform(3, 9)
        base_aggr = random.uniform(1, 10)

        # For unknown age or gender, feathers are sometimes observed
        if age_choice == 'juvenile':
            has_feathers = random.choice(['yes', 'no'])
        elif age_choice in ['adult', 'elder']:
            has_feathers = 'yes'
        else:
            has_feathers = random.choice(['yes', 'no', 'unknown'])

    # Apply randomness to measurements
    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.5, 1.8)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        dragon['snout_length'] = base_length * random.uniform(0.1, 0.25) * random.uniform(0.8, 1.2)
    else:
        dragon['snout_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if gender_choice == 'xis':
            wingspan_multiplier = random.uniform(2.5, 3.0)
        elif gender_choice == 'female':
            wingspan_multiplier = random.uniform(2.5, 3.0)
        elif gender_choice == 'male':
            wingspan_multiplier = random.uniform(2.0, 2.75)
        else:
            wingspan_multiplier = random.uniform(2.0, 3.0)

        dragon['wingspan'] = base_length * wingspan_multiplier * random.uniform(0.9, 1.1)
    else:
        dragon['wingspan'] = 0

    dragon['aggressiveness'] = base_aggr

    # Calculate flight speed - these dragons are extremely fast
    if dragon['wingspan'] > 0 and random.random() > missing_data_pct:
        base_speed = 70 + (dragon['wingspan'] * random.uniform(1, 2.5))
        dragon['flight_speed'] = base_speed * random.uniform(0.85, 1.15)
    else:
        dragon['flight_speed'] = 0

    dragon['color_of_scales'] = random.choice(colors)

    if random.random() > missing_data_pct:
        dragon['color_of_eyes'] = random.choice(['blue', 'yellow', 'green', 'red', 'amber', 'multicolored'])
    else:
        dragon['color_of_eyes'] = 'unknown'

    dragon['color_of_wings'] = random.choice(colors)

    if random.random() > missing_data_pct:
        dragon['shape_of_snout'] = 'pointed'
    else:
        dragon['shape_of_snout'] = 'unknown'

    if random.random() > missing_data_pct:
        dragon['shape_of_teeth'] = 'pointed'
    else:
        dragon['shape_of_teeth'] = 'unknown'

    if has_feathers == 'yes':
        # Juvenile/adult/elder with feathers
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
        dragon['body_texture'] = random.choice(['unknown'])
        dragon['scale_texture'] = 'smooth'
        dragon['feathers_present'] = 'unknown'

    # Constant characteristics for Antipodean Opaleyes
    dragon['shape_of_body'] = 'lithe'
    dragon['number_of_limbs'] = 2
    dragon['facial_spikes'] = random.choice(['yes', 'no'])
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

    dragon['loc_of_sighting'] = np.random.choice(locale, p=[0.10, 0.15, 0.35, 0.15, 0.15, 0.10])

    # No one knows if they're venomous
    dragon['is_venomous'] = 'unknown'

    dragon['breathing_fire_observed'] = np.random.choice(['yes', 'no'], p=[0.60, 0.40])
    if dragon['breathing_fire_observed'] == 'yes':
        dragon['breathing_ice_observed'] = 'no'
    else:
        dragon['breathing_ice_observed'] = np.random.choice(['yes', 'no'], p=[0.20, 0.80])  # hybrid dragon

    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Antipodean Opaleye'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/antipodean_opaleye.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Antipodean Opaleye dragon specimens")
print(f"Sample specimen: {specimens[0]}")