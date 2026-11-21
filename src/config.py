# ============================================================
# PROJECT: SOLAR-BATTERY ENERGY OPTIMISATION
# Domain: Energy Economics and Optimisation
# Location: Mumbai, Maharashtra, India
# ============================================================


# 1. GENERAL PROJECT INFORMATION

PROJECT_NAME = "Solar-Battery Energy Optimisation"

LOCATION = "Mumbai, Maharashtra, India"

BUILDING_TYPE = "Commercial"

TIME_INTERVAL_HOURS = 1

SIMULATION_HOURS = 8760  # 365 days x 24 hours


# 2. SOLAR PV SYSTEM PARAMETERS

PV_CAPACITY_KW = 20

PV_MODULE_TYPE = "Monocrystalline Silicon"

INVERTER_EFFICIENCY = 0.96  # Provisional modelling assumption


# 3. BATTERY ENERGY STORAGE PARAMETERS

BATTERY_CAPACITIES_KWH = [0, 5, 10, 15, 20, 25]

BATTERY_POWER_KW = 5

CHARGING_EFFICIENCY = 0.95

DISCHARGING_EFFICIENCY = 0.95

MIN_SOC = 0.20

MAX_SOC = 0.90

INITIAL_SOC = 0.50


# 4. BUILDING PARAMETERS

# These will be refined after analysing
# the building's hourly electricity demand.

BUILDING_LOAD_PROFILE = "commercial"

PEAK_DEMAND_KW = None


# 5. ELECTRICITY TARIFF PARAMETERS

# Actual tariff values will be added after
# researching the applicable Mumbai tariff.

OFF_PEAK_TARIFF = None

NORMAL_TARIFF = None

PEAK_TARIFF = None


# 6. FINANCIAL PARAMETERS

PROJECT_LIFETIME_YEARS = 10

DISCOUNT_RATE = 0.10

BATTERY_COST_PER_KWH = None

BATTERY_OM_COST_PER_YEAR = None

BATTERY_REPLACEMENT_YEAR = None


# 7. OPTIMISATION PARAMETERS

OPTIMISATION_OBJECTIVE = "Minimise Total Energy Cost"

OPTIMISATION_METHOD = "Mixed Integer Linear Programming"

ALLOW_GRID_IMPORT = True

ALLOW_SOLAR_EXPORT = False


# 8. DATA CONFIGURATION

RAW_DATA_PATH = "data/raw/"

PROCESSED_DATA_PATH = "data/processed/"

RESULTS_PATH = "results/"

PLOTS_PATH = "results/plots/"

TABLES_PATH = "results/tables/"


# ============================================================
# END OF CONFIGURATION
# ============================================================
