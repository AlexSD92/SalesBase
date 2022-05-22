OPEN = 'Op'
INPROGRESS = 'Ip'
CLOSEDWON = 'Cw'
CLOSEDLOST = 'Cl'
OPP_STATUS_CHOICES = [(OPEN, 'Open (New)'), (INPROGRESS, 'In Progress'), (CLOSEDWON, 'Closed Won'), (CLOSEDLOST, 'Closed Lost')]


ACTIVE = 'AC'
INACTIVE = 'IN'
ACC_CON_STATUS_CHOICES = [(ACTIVE, 'Active'), (INACTIVE, 'Inactive')]


ACCOMMODATION_FOOD_SERVICE = 'AFS'
ADMINISTRATIVE_SUPPORT_SERVICE = 'ASP'
AGRICULTURE_FORESTRY_FISHING = 'AFF'
ARTS_ENTERTAINMENT_RECREATION = 'AER'
CONSTRUCTION = 'CON'
EDUCATION = 'EDU'
ELECTRICITY_GAS_STEAM_AIR_CONDITIONING_SUPPLY = 'EGA'
FINANCIAL_INSURANCE = 'FII'
HUMAN_HEALTH_SOCIAL_WORK = 'HSW'
INFORMATION_COMMUNICATION = 'ICO'
MANUFACTURING = 'MAN'
MINING_QUARRYING = 'MIQ'
OTHER_SERVICE = 'OTH'
PROFESSIONAL_SCIENTIFIC_TECHNICAL = 'PST'
REAL_ESTATE = 'RES'
TRANSPORTATION_STORAGE = 'TRS'
WATER_SUPPLY_SEWERAGE_WASTE_MANAGEMENT_REMEDIATION = 'WWM'
WHOLESALE_RETAIL_TRADE = 'WRT'
ADVISORY_FINANCIAL_SERVICES = 'ADF'
CONSUMER_GOODS_SERVICES = 'CGS'
ONLINE_RETAIL = 'ONR'
SPECIALIST_ENGINEERING_INFRASTRUCTURE_CONTRACTORS = 'EIC'
TECHNOLOGY = 'TEC'


INDUSTRY_CHOICES = [(ACCOMMODATION_FOOD_SERVICE, 'Accommodation and Food Service Activities'),
                    (ADMINISTRATIVE_SUPPORT_SERVICE, 'Administrative and Support Service Activities'),
                    (AGRICULTURE_FORESTRY_FISHING, 'Agriculture, Forestry and Fishing'),
                    (ARTS_ENTERTAINMENT_RECREATION, 'Arts, Entertainment and Recreation'),
                    (CONSTRUCTION, 'Construction'),
                    (EDUCATION, 'Education'),
                    (ELECTRICITY_GAS_STEAM_AIR_CONDITIONING_SUPPLY, 'Electricity, Gas, Steam and Air Conditioning Supply'),
                    (FINANCIAL_INSURANCE, 'Financial and Insurance Activities'),
                    (HUMAN_HEALTH_SOCIAL_WORK, 'Human Health and Social Work Activities'),
                    (INFORMATION_COMMUNICATION, 'Information and Communication'),
                    (MANUFACTURING, 'Manufacturing'),
                    (MINING_QUARRYING, 'Mining and Quarrying'),
                    (OTHER_SERVICE, 'Other Service Activities'),
                    (PROFESSIONAL_SCIENTIFIC_TECHNICAL, 'Professional, Scientific and Technical Activities'),
                    (REAL_ESTATE, 'Real Estate Activities'),
                    (TRANSPORTATION_STORAGE, 'Transportation and Storage'),
                    (WATER_SUPPLY_SEWERAGE_WASTE_MANAGEMENT_REMEDIATION, 'Water Supply: Sewerage, Waste Management and Remediation Activities'),
                    (WHOLESALE_RETAIL_TRADE, 'Wholesale and Retail Trade'),
                    (ADVISORY_FINANCIAL_SERVICES, 'Advisory & Financial Services'),
                    (CONSUMER_GOODS_SERVICES, 'Consumer Goods & Services'),
                    (ONLINE_RETAIL, 'Online Retail'),
                    (SPECIALIST_ENGINEERING_INFRASTRUCTURE_CONTRACTORS, 'Specialist Engineering, Infrastructure & Contractors'),
                    (TECHNOLOGY, 'Technology')]


