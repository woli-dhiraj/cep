CREATE TABLE energy_usage (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_type VARCHAR(50),
    location VARCHAR(100),
    building_size FLOAT,
    occupants INT,
    heating_system VARCHAR(50),
    cooling_system VARCHAR(50),
    high_power_devices INT,
    num_fans INT,
    num_lights INT,
    usage_hours VARCHAR(50),
    energy_source VARCHAR(50)
);
