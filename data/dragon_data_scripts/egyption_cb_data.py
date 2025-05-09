import random
import numpy as np
import os
import pandas as pd

num_of_specimens = random.randint(720, 1643)
specimens = []

columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'feathers_present',
           'snout_length', 'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled',
           'length_of_horns', 'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed', 'breathing_ice_observed', 'observed_by', 'year_observed', 'species']

locale = ['Egypt', 'Ethiopia', 'Kenya', 'Saudi Arabia', 'Open Ocean', 'China', 'Philippines', 'Australia', 'Papua New Guinea']
colors = ['copper', 'gold', 'bronze', 'brown', 'red', 'mottled', 'pink']
eye_colors = ['red', 'yellow', 'amber', 'orange', 'multicolored']
initials = ['AB', 'TR', 'NR', 'SR', 'BR', 'NN', 'FF', 'OK', 'NK', 'DR', 'LM', 'KN',
            'U', 'VM', 'SX', 'WX', 'BB', 'CT', 'OH', 'TX']

# Percentage of specimens with missing data
missing_data_pct = 0.20

# Adjust gender and age distributions to reflect extreme aggression
# Fewer females than males, fewer xis than males, fewer elders due to aggression
gender_dist = np.array([0.60, 0.25, 0.15])  # Male, Female, Xis
age_dist = np.array([0.45, 0.40, 0.15])  # Juvenile, Adult, Elder (fewer elders due to aggression)

for i in range(num_of_specimens):
    gender_choice = np.random.choice(['male', 'female', 'xis', 'unknown'],
                                     p=[gender_dist[0] * 0.96, gender_dist[1] * 0.96,
                                        gender_dist[2] * 0.96, 0.04])

    age_choice = np.random.choice(['juvenile', 'adult', 'elder', 'unknown'],
                                  p=[age_dist[0] * 0.96, age_dist[1] * 0.96,
                                     age_dist[2] * 0.96, 0.04])

    dragon = {
        'gender': gender_choice,
        'estimated_age': age_choice
    }

    base_length = 0.0
    base_aggr = 0.0

    if gender_choice != 'unknown' and age_choice != 'unknown':
        # Male dragons
        if gender_choice == 'male':
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 4)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.uniform(3, 5)
                base_aggr = random.randint(8, 9)
            else:  # elder
                base_length = random.uniform(4, 6)
                base_aggr = random.randint(8, 9)

        # Female dragons - more aggressive than males
        elif gender_choice == 'female':
            if age_choice == 'juvenile':
                base_length = random.uniform(3, 6)
                base_aggr = random.randint(9, 10)
            elif age_choice == 'adult':
                base_length = random.uniform(4, 8)
                base_aggr = random.randint(9, 10)
            else:  # elder
                base_length = random.uniform(6, 10)
                base_aggr = random.randint(9, 10)

        # Xis dragons
        else:
            if age_choice == 'juvenile':
                base_length = random.uniform(2, 6)
                base_aggr = random.randint(8, 10)
            elif age_choice == 'adult':
                base_length = random.uniform(3, 8)
                base_aggr = random.randint(8, 10)
            else:  # elder
                base_length = random.uniform(5, 11)
                base_aggr = random.randint(8, 10)
    else:
        # When gender or age is unknown, use a mid-range value
        base_length = random.uniform(3, 9)
        base_aggr = random.randint(8, 10)

    if random.random() < 0.10:  # 5% chance of unusually long specimen
        base_length *= random.uniform(1.2, 2.1)

    if random.random() > missing_data_pct:
        dragon['est_body_length'] = base_length * random.uniform(0.7, 1.15)
    else:
        dragon['est_body_length'] = 0  # Missing data

    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            dragon['snout_length'] = base_length * random.uniform(0.15, 0.3)
        else:  # adult, elder or unknown
            dragon['snout_length'] = base_length * random.uniform(0.25, 0.275)
    else:
        dragon['snout_length'] = 0  # Missing data

    # Account for missing wings due to aggression
    missing_wing_chance = 0.08  # 8% chance of missing a wing
    has_wing_injury = False
    dragon['aggressiveness'] = base_aggr

    if dragon['aggressiveness'] >= 9 and random.random() < missing_wing_chance:
        has_wing_injury = True

    # Wingspan calculations - accounting for wing injuries
    if random.random() > missing_data_pct:
        if has_wing_injury:
            # Reduced wingspan due to injury
            wingspan_multiplier = random.uniform(0.6, 1.8)
        else:
            if gender_choice == 'male':
                if age_choice == 'juvenile':
                    wingspan_multiplier = random.uniform(1.8, 1.9)
                elif age_choice == 'adult':
                    wingspan_multiplier = random.uniform(2.0, 2.6)
                else:  # elder
                    wingspan_multiplier = random.uniform(2.1, 2.65)
            elif gender_choice == 'female' or gender_choice == 'xis':
                if age_choice == 'juvenile':
                    wingspan_multiplier = random.uniform(1.7, 2.45)
                else:  # adult, elder
                    wingspan_multiplier = random.uniform(1.9, 2.6)
            else:  # unknown
                wingspan_multiplier = random.uniform(2.1, 2.5)

        dragon['wingspan'] = base_length * wingspan_multiplier
    else:
        dragon['wingspan'] = 0  # Missing data

    # Very fast flight speed
    if random.random() > missing_data_pct:
        if age_choice == 'juvenile':
            base_speed = 70  # Fastest
        elif age_choice == 'adult':
            base_speed = 62.5  # Fast
        else:  # elder or unknown
            base_speed = 57.5  # Slightly slower but still fast

        # Adjust speed for wing injuries
        if has_wing_injury:
            flight_multiplier = 0  # Significantly reduced speed
        else:
            flight_multiplier = random.uniform(0.75, 1.25)  # Normal variation

        dragon['flight_speed'] = base_speed * flight_multiplier
    else:
        dragon['flight_speed'] = 0  # Missing data

    # Higher aggression = higher chance of missing limbs
    limb_loss_chance = (dragon['aggressiveness'] - 7) * 0.05  # 5-15% chance based on aggression
    if random.random() < limb_loss_chance:
        # Determine how many limbs are missing (0-1)
        limbs_missing = random.randint(0, 1)
        dragon['number_of_limbs'] = max(1, 2 - limbs_missing)  # Minimum 1 limb
    else:
        dragon['number_of_limbs'] = 2  # Normal

    dragon['color_of_scales'] = random.choice(colors)

    dragon['color_of_eyes'] = random.choice(eye_colors)

    if random.random() < 0.30:  # 3% chance of red wings
        dragon['color_of_wings'] = 'red'
    else:
        dragon['color_of_wings'] = random.choice(colors)

    dragon['shape_of_snout'] = random.choice(['square', 'snub'])
    dragon['shape_of_teeth'] = 'pointed'
    dragon['scales_present'] = 'yes'
    dragon['scale_texture'] = 'rough'
    dragon['body_texture'] = 'scaled'
    dragon['shape_of_body'] = 'lithe'
    dragon['facial_spikes'] = 'no'
    dragon['frilled'] = 'yes'
    dragon['feathers_present'] = 'no'
    dragon['length_of_horns'] = random.choice(['medium', 'long'])
    dragon['shape_of_horns'] = random.choice(['spiny', 'twisted', 'pointed'])
    dragon['shape_of_tail'] = 'pointed'

    dragon['loc_of_sighting'] = random.choices(
        locale,
        weights=[20, 10, 10, 10, 10, 10, 10, 10, 10],  # Egypt primary, Open Ocean significant
        k=1
    )[0]

    dragon['is_venomous'] = 'yes'

    # Fire breathing - higher chance due to aggression
    fire_chance = 0.5  # 50% base chance
    dragon['breathing_fire_observed'] = 'yes' if random.random() < fire_chance else 'no'
    dragon['breathing_ice_observed'] = 'no'
    dragon['observed_by'] = random.choice(initials)
    dragon['year_observed'] = random.randint(1955, 2023)

    dragon['species'] = 'Egyptian Copperbelly'

    specimens.append(dragon)

specimens_df = pd.DataFrame(specimens)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(base_dir, "dragon_spreadsheets")

specimens_df.to_csv(output_dir + '/egyptian_copperbelly.csv', columns=columns, index=False, mode='w')

print(f"Generated {len(specimens)} Egyptian Copperbelly dragon specimens")
print(f"Sample specimen: {specimens[0]}")