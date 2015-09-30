import csv
from decimal import Decimal

from .constants import CreditScoreTrend, Field, Status
from .converters import convert_to_python
from .lookups import equal, greater_than


example_config = {
    Field.CREDIT_SCORE_TREND: {
        'value': CreditScoreTrend.UP,
        'condition': equal
    },
    Field.OUTSTANDING_PRINCIPAL: {
        'value': Decimal('0.2'),
        'condition': greater_than
    }
}


def evaluate_note(note, search_config):
    return all(
        config['condition'](note[field], config['value'])
        for field, config in search_config.items()
    )


def scan_notes(notes, search_config):
    return [
        note for note in notes
        if evaluate_note(convert_to_python(note), search_config)
    ]


def scan_csv(filename, search_config, to_csv=False):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = reader.next()
        notes = scan_notes(reader, search_config)

    if not to_csv:
    	return notes

    with open('output.csv', 'w') as f:
    	writer = csv.writer(f)
    	for row in [header] + notes:
    		writer.writerow(row)
