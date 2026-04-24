import pandas as pd
import random

random.seed(42)

NAMES = [
    "Tochi Fabric","Frejol Velvet","Jessy Fabric","Bari Leatherette",
    "Alejandro Velvet","Miranda Chenille","Andres Chenille","Luxor Leatherette",
    "Scandic Wooden","Casper Velvet","Nordic Linen","Elegance Suede",
    "Brio Polyester","Luxe PU Leather","Heritage Teak","Studio Cotton",
    "Zen Recliner","Classic Leather","Bloom Jacquard","Futon Convertible",
    "Royale Silk Velvet","Maven Faux Leather","Comfort Plus Fabric","Aria Fabric",
    "Imperio PU Leather","Meadow Handloom","Posh Velvet","Serene Microsuede",
    "Tropicana Printed","Monarch Leather","Plush Fabric","Vintage Reclaimed",
    "Alesund Fabric","Regal Chesterfield","Compact Polyester","Comfy Microfiber",
    "Havana Leather","Porto Velvet","Cairo Linen","Oslo Fabric",
    "Kyoto Suede","Lima Cotton","Vienna Chenille","Berlin Fabric",
    "Roma Leatherette","Seoul Velvet","Dubai Leather","Paris Jacquard",
    "Tokyo Microfiber","Sydney Fabric",
]

BRANDS = [
    "Wakefit","Urban Ladder","Pepperfry","Hometown","Godrej Interio",
    "Nilkamal","Durian","Stanley","FabIndia","Woodcraft",
    "Recliners India","Springwel","Sarita Handa","IKEA","Furlenco",
    "@home","Evok","Zuari","Featherlite","Damro",
]

MATERIALS = [
    "Fabric","Velvet","Leatherette","Chenille","Linen",
    "Microfiber","PU Leather","Genuine Leather","Suede","Cotton Fabric",
    "Polyester","Jacquard Fabric","Silk Velvet","Faux Leather",
    "Microsuede","Handloom Cotton","Printed Fabric","Top Grain Leather",
]

COLORS = [
    "Grey","Cream","Beige","Dark Brown","Carbon Grey","Ivory",
    "Ash Grey","Teal","Dark Blue","Tan","Off White","Charcoal",
    "Red","Black","Mustard Yellow","Caramel","Floral Pink",
    "Olive Green","Royal Blue","White","Steel Grey","Dusty Rose",
    "Sky Blue","Burgundy","Earthy Brown","Dark Green","Cognac",
    "Light Brown","Graphite","Rustic Brown",
]

STYLES = [
    "Contemporary","Modern","Scandinavian","Mid-Century Modern",
    "Casual","Classic","Minimalist","Bohemian","Artisanal",
    "Traditional","Luxury","Vintage","Industrial","Rustic",
]

CUSHIONS = [
    "Foam","High Density Foam","Foam + Fibre","Pocket Spring",
    "Coil Spring","Memory Foam","Foam + Spring","Feather + Foam",
    "High Resilience Foam","Bonded Foam",
]

LEGS = [
    "Wood","Metal","Solid Wood","Sheesham Wood","Teak Wood",
    "Mango Wood","Walnut Wood","Reclaimed Wood","Brass Finished Wood",
    "Solid Rosewood","Plastic","Stainless Steel","Solid Oak",
]

DIMS = [
    "160x70x75","165x72x78","168x73x78","168x74x82","168x78x80",
    "170x75x80","172x76x82","172x76x84","174x78x84","175x78x82",
    "176x79x84","176x80x84","178x80x84","178x80x86","180x80x85",
    "180x82x84","180x82x86","182x80x88","183x84x88","185x80x88",
    "185x82x88","185x84x86","188x86x92","190x85x90","192x88x105",
]

PRICE_BANDS = [(10000,20000),(20001,35000),(35001,55000),(55001,90000)]
WARRANTY    = [1,1,1,2,2,3,3,5,7,10]

records = []
for i in range(1, 201):
    name     = NAMES[i % len(NAMES)]
    color    = random.choice(COLORS)
    brand    = random.choice(BRANDS)
    material = random.choice(MATERIALS)
    style    = random.choice(STYLES)
    cushion  = random.choice(CUSHIONS)
    leg      = random.choice(LEGS)
    dims     = random.choice(DIMS)
    assembly = random.choice(["Yes","No"])
    warranty = random.choice(WARRANTY)
    band     = random.choice(PRICE_BANDS)
    mrp      = random.randint(band[0], band[1])
    disc_pct = random.randint(5, 25)
    sp       = round(mrp * (1 - disc_pct/100) / 100) * 100
    weight   = round(random.uniform(35, 90), 1)
    rating   = round(random.uniform(3.5, 5.0), 1)
    reviews  = random.randint(20, 600)
    in_stock = random.choices(["Yes","No"], weights=[90,10])[0]

    records.append({
        "product_id":           f"P{i:03d}",
        "product_name":         f"{name} 2 Seater Sofa In {color} Colour",
        "brand":                brand,
        "price_inr":            mrp,
        "discounted_price_inr": sp,
        "discount_percent":     disc_pct,
        "material":             material,
        "color":                color,
        "seater_type":          "2 Seater",
        "dimensions_cm":        dims,
        "weight_kg":            weight,
        "rating":               rating,
        "num_reviews":          reviews,
        "style_category":       style,
        "cushion_type":         cushion,
        "leg_material":         leg,
        "assembly_required":    assembly,
        "warranty_years":       warranty,
        "in_stock":             in_stock,
    })

df = pd.DataFrame(records)
df.to_csv("pepperfry_sofas.csv", index=False)
print(f"Done! Saved {len(df)} rows to pepperfry_sofas.csv")
print(df.head())