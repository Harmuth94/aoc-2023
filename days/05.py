def process_map(raw_map, lookup_ranges):
    output_ranges = []
    while True:
        if len(lookup_ranges) == 0:
            return output_ranges
        _range = lookup_ranges.pop(0)

        cut = False

        for line in raw_map[1:]:
            # either no overlap, partial overlap, or full overlap
            destination, source, range = [int(x) for x in line.split(' ')]
            delta =  destination - source
            start = source
            end = source + range - 1
            if _range[0] <= end and _range[1] >= start: # any overlap
                # overlap
                if _range[0] >= start and _range[1] <= end:
                    # within
                    output_ranges.append((_range[0] + delta, _range[1] + delta))
                    cut = True
                    
                elif _range[0] < start:
                    # over overlap
                    lookup_ranges.append((start, _range[1]))    
                    lookup_ranges.append((_range[0], start - 1))
                    cut = True
                    
                elif _range[1] > end:
                    # partial overlap
                    lookup_ranges.append((end + 1, _range[1]))
                    lookup_ranges.append((_range[0], end))
                    cut = True
                break

        
        if not cut:
            output_ranges.append(_range)

        

if __name__ == '__main__':
    
    with open('data/input05.txt') as f:
        data = [x.splitlines() for x in f.read().split('\n\n')]

    seeds = [int(x) for x in data[0][0].split(': ')[1].split(' ')]
    seed_to_soil_raw = data[1]
    soil_to_fertilizer_raw = data[2]
    fertilizer_to_seed_water_raw = data[3]
    water_to_light_raw = data[4]
    light_to_temperature_raw = data[5]
    temperature_to_humidity_raw = data[6]
    humidity_to_location_raw = data[7]
    output = []

    # part 1
    for idx, seed in enumerate(seeds):
        
        seed_to_soil = process_map(seed_to_soil_raw, [(seed,seed)])
        soil_to_fertilizer = process_map(soil_to_fertilizer_raw, seed_to_soil)
        fertilizer_to_seed_water = process_map(fertilizer_to_seed_water_raw, soil_to_fertilizer)
        water_to_light = process_map(water_to_light_raw, fertilizer_to_seed_water)
        light_to_temperature = process_map(light_to_temperature_raw, water_to_light)
        temperature_to_humidity = process_map(temperature_to_humidity_raw, light_to_temperature)
        humidity_to_location = process_map(humidity_to_location_raw, temperature_to_humidity)
        output.append(humidity_to_location)
    
    
    print(min([x[0][0] for x in output]))
    output = []

    # part 2
    for idx, seed in enumerate(seeds):
        if idx % 2 != 0:
            continue

        seed_to_soil = process_map(seed_to_soil_raw, [(seed,seed + seeds[idx + 1] -1 )])
        soil_to_fertilizer = process_map(soil_to_fertilizer_raw, seed_to_soil)
        fertilizer_to_seed_water = process_map(fertilizer_to_seed_water_raw, soil_to_fertilizer)
        water_to_light = process_map(water_to_light_raw, fertilizer_to_seed_water)
        light_to_temperature = process_map(light_to_temperature_raw, water_to_light)
        temperature_to_humidity = process_map(temperature_to_humidity_raw, light_to_temperature)
        humidity_to_location = process_map(humidity_to_location_raw, temperature_to_humidity)
        output.append(humidity_to_location)

    # flatten list of lists
    output_flat = [item for sublist in output for item in sublist]

    print(min([x[0] for x in output_flat]))