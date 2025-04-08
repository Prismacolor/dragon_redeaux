import random
import numpy as np
import pandas as pd

'''Ahhh the elusive Amazonian blue, a mild mannered creature that enjoys fishing off the coasts 
of South and Central America. Can sometimes be found in the arctic when food is abundant.
Adult males have a distinctive frill around their necks which they display during mating season. '''

num_of_specimens = random.randint(824, 1843)  # create uneven class observations
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Brazil', 'Peru', 'Open Ocean', 'Arctic', 'Chile', 'Argentina', 'Central America']
colors = ['blue', 'grey', 'white', 'silver', 'green']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.25  # Increased due to elusive nature

for i in range(num_of_specimens):
    # We have some unknowns because this is an elusive species, and difficult to measure
    gender_choice = np.random.choice(['male', 'female', 'unknown'], p=[0.20, 0.35, 0.45])
    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'], p=[0.15, 0.35, 0.20, 0.30])

    dragon = {'gender': gender_choice, 'estimated_age': age_choice,
              'color_of_scales': random.choice(colors),
              'color_of_eyes': random.choice(['red', 'yellow', 'orange', 'amber', 'unknown']
                                             if random.random() < 0.25 else ['red', 'yellow', 'amber', 'orange']),
              'color_of_wings': random.choice(colors),
              'shape_of_snout': random.choice(['snub', 'unknown']
                                              if random.random() < 0.20 else ['snub']),
              'shape_of_teeth': random.choice(['pointed', 'unknown']
                                              if random.random() < 0.30 else ['pointed']),
              'scales_present': random.choice(['no', 'full', 'partial', 'unknown']
                                              if random.random() < 0.15 else ['no', 'partial', 'full']),
              'scale_texture': random.choice(['smooth', 'unknown']
                                             if random.random() < 0.20 else ['smooth']),
              'body_texture': random.choice(['scaled', 'mixed', 'unknown']
                                            if random.random() < 0.15 else ['scaled', 'mixed']),
              'shape_of_body': 'lithe'}

    base_length = 0.0
    base_limbs = 4

    # Set base metrics by gender and age when known
    if gender_choice != 'unknown' and age_choice != 'unknown':
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 4)
                base_aggr = random.normalvariate(1.5, 0.4)
            elif age_choice == 'adult':
                base_length = random.uniform(3, 6)
                base_aggr = random.normalvariate(1.8, 0.6)
            else:  # elder
                base_length = random.uniform(3, 7)
                base_aggr = random.normalvariate(1.6, 0.7)
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 5)
                base_aggr = random.normalvariate(1.4, 0.5)
            elif age_choice == 'adult':
                base_length = random.uniform(4, 7)
                base_aggr = random.normalvariate(1.7, 0.6)
            else:  # elder
                base_length = random.uniform(4, 8)
                base_aggr = random.normalvariate(1.5, 0.8)
    else:
        # when gender is unknown let us guestimate
        base_length = random.uniform(3, 6)
        base_aggr = random.normalvariate(1.6, 0.8)

    # Adding randomness to the measurements
    dragon['est_body_length'] = base_length * random.uniform(0.7, 1.3)
    dragon['snout_length'] = (base_length * random.uniform(0.1, 0.2)) * random.uniform(0.7, 1.3)
    dragon['wingspan'] = base_length * random.uniform(1.5, 3.0)

    # Set aggressiveness (1-5 scale)
    dragon['aggressiveness'] = max(1, min(5, round(base_aggr)))

    base_speed = 50 + (dragon['wingspan'] * random.uniform(5, 8))
    dragon['flight_speed'] = base_speed * random.uniform(0.7, 1.3)

    dragon['number_of_limbs'] = 4

    # Because Amazonian Blues are elusive and sometimes spotted far away, we are not 100% sure they do not have spikes
    dragon['facial_spikes'] = random.choice(['no', 'unknown'])

    # only adult and elder males have frills
    if gender_choice == 'male' and (age_choice == 'adult' or age_choice == 'elder'):
        dragon['frilled'] = 'yes'
    else:
        dragon['frilled'] = 'no'

    dragon['feathers_present'] = 'no'

    dragon['length_of_horns'] = random.choice(['short', 'none', 'unknown']
                                              if random.random() < 0.15 else ['short', 'none'])
    dragon['shape_of_horns'] = random.choice(['pointed', 'none', 'unknown']
                                             if random.random() < 0.15 else ['pointed', 'none'])
    dragon['shape_of_tail'] = random.choice(['fluted', 'unknown']
                                            if random.random() < 0.15 else ['fluted'])
    dragon['loc_of_sighting'] = random.choice(locale)
    dragon['is_venomous'] = 'no'
    dragon['breathing_fire_observed'] = 'no'
    dragon['breathing_ice_observed'] = random.choice(['yes', 'no'])

    # Observer and year
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Amazonian Blue'

    # Introduce missing data for some specimens
    if random.random() < missing_data_pct:
        num_missing = random.randint(1, 3)
        possible_missing_fields = ['est_body_length', 'snout_length', 'wingspan',
                                   'flight_speed']

        missing_fields = random.sample(possible_missing_fields, k=min(num_missing, len(possible_missing_fields)))

        for field in missing_fields:
            dragon[field] = 0  # Use 0 to indicate missing data

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)
specimens_df.to_csv('../dragon_spreadsheets/amazonian_blue.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Amazonian Blue dragon specimens")
print(f"Sample specimen: {specimens[0]}")