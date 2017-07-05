import pandas as pd
from sklearn.preprocessing import scale


def targeted():

	auto = pd.read_csv("Auto1-DS-TestData.csv")
	# Cleaning data
	auto = auto[auto['normalized-losses'] != '?']
	auto = auto[auto['price'] != '?']
	auto = auto[auto['num-of-doors'] != '?']
	auto = auto[auto['bore'] != '?']
	auto = auto[auto['stroke'] != '?']
	auto = auto[auto['horsepower'] != '?']
	auto = auto[auto['peak-rpm'] != '?']
	auto['normalized-losses'] = auto['normalized-losses'].astype(float)
	auto['price'] = auto['price'].astype(float)
	auto['peak-rpm'] = auto['peak-rpm'].astype(float)
	auto['bore'] = auto['bore'].astype(float)
	auto['stroke'] = auto['stroke'].astype(float)
	auto = auto.reset_index()
	return auto['symboling']


def auto_numeric():
	"""Import dataset, keep numerical and scale"""

	auto = pd.read_csv("data/Auto1-DS-TestData.csv")
	# Cleaning data
	auto = auto[auto['normalized-losses'] != '?']
	auto = auto[auto['price'] != '?']
	auto = auto[auto['num-of-doors'] != '?']
	auto = auto[auto['bore'] != '?']
	auto = auto[auto['stroke'] != '?']
	auto = auto[auto['horsepower'] != '?']
	auto = auto[auto['peak-rpm'] != '?']
	auto[auto['num-of-cylinders'] == 'four'] = 4
	auto[auto['num-of-cylinders'] == 'eight'] = 8
	auto[auto['num-of-cylinders'] == 'five'] = 5
	auto[auto['num-of-cylinders'] == 'six'] = 6
	auto[auto['num-of-cylinders'] == 'three'] = 3
	auto[auto['num-of-cylinders'] == 'twelve'] = 12
	auto[auto['num-of-cylinders'] == 'two'] = 2
	auto['normalized-losses'] = auto['normalized-losses'].astype(float)
	auto['price'] = auto['price'].astype(float)
	auto['peak-rpm'] = auto['peak-rpm'].astype(float)
	auto['bore'] = auto['bore'].astype(float)
	auto['stroke'] = auto['stroke'].astype(float)
	auto = auto.reset_index()

	_auto_numeric = {}
	for _columns in auto:
	    if (auto[_columns].dtypes == 'float64') or (auto[_columns].dtypes == 'int64'):
	        _auto_numeric[_columns] = auto[_columns]
	_auto_numeric = pd.DataFrame(_auto_numeric)
	del _auto_numeric['symboling']

	_auto_numeric = pd.DataFrame(scale(_auto_numeric), columns = _auto_numeric.columns)

	return _auto_numeric


def auto_category():
	"""Import dataset, keep numerical and scale"""

	auto = pd.read_csv("data/Auto1-DS-TestData.csv")
	# Cleaning data
	auto = auto[auto['normalized-losses'] != '?']
	auto = auto[auto['price'] != '?']
	auto = auto[auto['num-of-doors'] != '?']
	auto = auto[auto['bore'] != '?']
	auto = auto[auto['stroke'] != '?']
	auto = auto[auto['horsepower'] != '?']
	auto = auto[auto['peak-rpm'] != '?']
	auto[auto['num-of-cylinders'] == 'four'] = 4
	auto[auto['num-of-cylinders'] == 'eight'] = 8
	auto[auto['num-of-cylinders'] == 'five'] = 5
	auto[auto['num-of-cylinders'] == 'six'] = 6
	auto[auto['num-of-cylinders'] == 'three'] = 3
	auto[auto['num-of-cylinders'] == 'twelve'] = 12
	auto[auto['num-of-cylinders'] == 'two'] = 2
	auto['normalized-losses'] = auto['normalized-losses'].astype(float)
	auto['price'] = auto['price'].astype(float)
	auto['peak-rpm'] = auto['peak-rpm'].astype(float)
	auto['bore'] = auto['bore'].astype(float)
	auto['stroke'] = auto['stroke'].astype(float)
	auto = auto.reset_index()

	auto_category = {}
	for _columns in auto:
	    if not((auto[_columns].dtypes == 'float64') or (auto[_columns].dtypes == 'int64')):
	        auto_category[_columns] = auto[_columns]
	auto_category = pd.DataFrame(auto_category)


	return auto_category
