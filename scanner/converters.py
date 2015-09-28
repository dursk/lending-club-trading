from datetime import datetime
from decimal import Decimal, InvalidOperation

from .constants import Field


def to_int(val):
    try:
        return int(val)
    except ValueError:
        return 0


def to_decimal(val):
    try:
        return Decimal(val)
    except InvalidOperation:
        return Decimal('0')


def convert_to_python(note):
    for field in Field.integer_fields:
        note[field] = to_int(note[field])
    for field in Field.decimal_fields:
        note[field] = to_decimal(note[field])
    for field in Field.datetime_fields:
        note[field] = datetime.strptime(note[field], '%m/%d/%Y')
    for field in Field.bool_fields:
        note[field] = True if note[field] == 'true' else False
    credit_score = to_int(note[Field.FICO_END_RANGE].split('-')[0])
    note[Field.FICO_END_RANGE] = credit_score
    return note
