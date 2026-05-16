#The Cargo Load Balancer
total_weight=0
cargo_weights=[45,120,30,200,50]
for weight in cargo_weights:
    if weight>100:
        print(f"item too heavy({weight})kg.Skipping...")
        continue
    else:
        print(f"Loading item({weight}kg...)")
        total_weight+=weight
print(f"\nloading complete.Total weight onboard:{total_weight}kg")
            