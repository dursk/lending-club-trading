from datetime import datetime
from decimal import Decimal, InvalidOperation

from .constants import Field


def convert_to_python(note):
    for field in Field.integer_fields:
        try:
            note[field] = int(note[field])
        except ValueError:
            note[field] = 0
    for field in Field.decimal_fields:
        try:
            note[field] = Decimal(note[field])
        except InvalidOperation:
            note[field] = Decimal('0')
    for field in Field.datetime_fields:
        note[field] = datetime.strptime(note[field], '%m/%d/%Y')
    for field in Field.bool_fields:
        note[field] = True if note[field] == 'true' else False
    credit_score = int(note[Field.FICO_END_RANGE].split('-')[0])
    note[Field.FICO_END_RANGE] = credit_score
    return note
