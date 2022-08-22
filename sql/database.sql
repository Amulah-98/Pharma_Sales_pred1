CREATE TABLE IF NOT EXISTS `TB` 
(
    'Store': 'INT NOT NULL',
    'DayOfWeek': 'INT NOT NULL',
    'DayOfWeek': 'DATETIME NOT NULL',
    'Sales': 'FLOAT NOT NULL',
    'Open': 'INT DEFAULT NULL',
    'Promo': 'INT DEFAULT NULL',
    'StateHoliday': 'INT DEFAULT NULL',
    'SchoolHoliday': 'INT DEFAULT NULL',
    'StoreType': 'INT DEFAULT NULL',
    'Assortment': 'VARCHAR(10) DEFAULT NULL',
    'CompetitionDistance': 'FLOAT DEFAULT NULL',
    'CompetitionOpenSinceMonth': 'INT DEFAULT NULL',
    'CompetitionOpenSinceYear': 'INT DEFAULT NULL',
    'Promo2': 'INT DEFAULT NULL',
    'Promo2SinceWeek': 'INT DEFAULT NULL',
    'Promo2SinceYear': 'INT DEFAULT NULL',
    'PromoInterval': 'VARCHAR(40) DEFAULT NULL',
    PRIMARY KEY (`Store`)
)