cities = {
    'New York': [32, 25, 30, 28, 35],
    'Los Angelse': [75, 18, 22, 25, 15],
    'Chicago': [20, 18, 22, 25, 15]
}

averages = {city: sum(temp) / len(temp) for city, temp in cities.items()}
print("Average Temperation :",averages) 
