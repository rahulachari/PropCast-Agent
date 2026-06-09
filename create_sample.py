import pandas as pd
import numpy as np

np.random.seed(42)

city_config = {
    'Gachibowli - Hyderabad':    (7500, 10500),
    'Kondapur - Hyderabad':      (7000, 9500),
    'Banjara Hills - Hyderabad': (12000, 18000),
    'Madhapur - Hyderabad':      (6800, 9200),
    'Hitech City - Hyderabad':   (8000, 11000),
    'Jubilee Hills - Hyderabad': (13000, 19000),
    'Kukatpally - Hyderabad':    (5500, 7500),
    'Miyapur - Hyderabad':       (4800, 6800),
    'Whitefield - Bangalore':    (7000, 10000),
    'Koramangala - Bangalore':   (11000, 16000),
    'Indiranagar - Bangalore':   (12000, 17000),
    'Electronic City - Bangalore':(5500, 8000),
    'HSR Layout - Bangalore':    (9000, 13000),
    'Marathahalli - Bangalore':  (6500, 9000),
    'Sarjapur - Bangalore':      (5800, 8500),
    'Hebbal - Bangalore':        (7500, 10500),
    'Andheri - Mumbai':          (18000, 26000),
    'Bandra - Mumbai':           (35000, 55000),
    'Powai - Mumbai':            (20000, 30000),
    'Thane - Mumbai':            (10000, 15000),
    'Navi Mumbai - Mumbai':      (9000, 13000),
    'Borivali - Mumbai':         (15000, 22000),
    'OMR - Chennai':             (5500, 8500),
    'Anna Nagar - Chennai':      (10000, 15000),
    'Velachery - Chennai':       (7000, 10000),
    'Porur - Chennai':           (5800, 8200),
    'Tambaram - Chennai':        (4500, 6800),
    'Dwarka - Delhi':            (8000, 12000),
    'Noida Sector 62 - Delhi':   (6500, 9500),
    'Gurgaon - Delhi':           (10000, 16000),
    'Rohini - Delhi':            (7000, 10000),
    'Vasant Kunj - Delhi':       (15000, 22000),
    'Hinjewadi - Pune':          (6000, 9000),
    'Kothrud - Pune':            (8500, 12000),
    'Wakad - Pune':              (6500, 9500),
    'Baner - Pune':              (7500, 11000),
    'Hadapsar - Pune':           (5500, 8000),
}

rows = []
for loc, (lo, hi) in city_config.items():
    for _ in range(50):
        bhk   = np.random.choice([1,2,3,4], p=[0.10,0.45,0.35,0.10])
        base  = {1:550, 2:1050, 3:1600, 4:2400}[bhk]
        area  = int(np.clip(np.random.normal(base, base*0.08), 400, 5000))
        age   = int(np.random.choice([0,1,2,3,4,5,6,7,8,10,12,15,20],
                    p=[0.08,0.08,0.09,0.09,0.09,0.09,0.09,0.09,0.08,0.07,0.06,0.05,0.04]))
        park  = np.random.choice(['Yes','No'], p=[0.70,0.30])
        ppsf  = np.random.uniform(lo, hi)
        if bhk == 4:   ppsf *= 1.08
        if bhk == 1:   ppsf *= 0.92
        if age > 10:   ppsf *= 0.88
        elif age > 5:  ppsf *= 0.94
        elif age <= 1: ppsf *= 1.06
        if park == 'Yes': ppsf *= 1.03
        price = round((ppsf * area) / 100000 * np.random.uniform(0.99, 1.01), 2)
        price = max(20, price)
        rows.append({
            'Location'   : loc,
            'BHK'        : bhk,
            'Area_sqft'  : area,
            'Price_Lakhs': price,
            'Age_Years'  : age,
            'Parking'    : park,
            'Status'     : np.random.choice(['Available','Sold'], p=[0.55,0.45]),
        })

df = pd.DataFrame(rows).sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('sample_properties.csv', index=False)
print(f"Generated {len(df)} properties across {len(city_config)} locations")
print(f"Price range: Rs.{df['Price_Lakhs'].min()}L - Rs.{df['Price_Lakhs'].max()}L")