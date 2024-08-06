input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

filtered_dict = {k: v for k, v in input_dict.items() if v is not None}

for key, value in filtered_dict.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
