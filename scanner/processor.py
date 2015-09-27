import csv

from .constants import CreditScoreTrend, Field, Status
from .lookups import equal


example_config = {
	Field.CREDIT_SCORE_TREND: {
		'value': CreditScoreTrend.UP,
		'condition': equal
	}
}


def scan_notes(notes, search_config):
	profitable_notes = []
	for note in notes:
		meets_criteria = True
		for field, config in search_config.items():
			value = config['value']
			condition = config['condition']
			if not condition(note[field], value):
				meets_criteria = False
				break
		if meets_criteria:
			profitable_notes.append(note)
	return profitable_notes


def scan_csv(filename, search_config):
	with open(filename, 'r') as f:
		reader = csv.reader(f)
		reader.next()
		return scan_notes(reader, search_config)