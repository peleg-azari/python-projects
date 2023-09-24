from pyproj import Transformer

# Define the transformer for ICS to ITM conversion
ics_to_itm_transformer = Transformer.from_crs("EPSG:2039", "EPSG:2039", always_xy=True)  # Israeli Cassini-Soldner to Israeli Transverse Mercator

# Input ICS coordinates
ics_x = 726020
ics_y = 532970

# Convert ICS to ITM
itm_x, itm_y = ics_to_itm_transformer.transform(ics_x, ics_y)

print("ITM Coordinates:", itm_x, itm_y)
