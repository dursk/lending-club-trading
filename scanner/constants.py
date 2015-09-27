class Field(object):
    LOAN_ID = 0
    NOTE_ID = 1
    ORDER_ID = 2
    OUTSTANDING_PRINCIPAL = 3
    ACCRUED_INTEREST = 4
    STATUS = 5
    ASK_PRICE = 6
    MARKUP_OR_DISCOUNT = 7
    YIELD_TO_MATURITY = 8
    DAYS_SINCE_LAST_PAYMENT = 9
    CREDIT_SCORE_TREND = 10
    FICO_END_RANGE = 11
    DATE_LISTED = 12
    NEVER_LATE = 13
    LOAN_CLASS = 14
    LOAN_MATURITY = 15
    ORIGINAL_LOAN_AMOUNT = 16
    INTEREST_RATE = 17
    REMAINING_PAYMENTS = 18
    PRINCIPAL_AND_INTEREST = 19

    bool_fields = {
        NEVER_LATE,
    }

    datetime_fields = {
        DATE_LISTED,
    }

    decimal_fields = {
        OUTSTANDING_PRINCIPAL,
        ACCRUED_INTEREST,
        ASK_PRICE,
        MARKUP_OR_DISCOUNT,
        YIELD_TO_MATURITY,
        ORIGINAL_LOAN_AMOUNT,
        INTEREST_RATE,
        PRINCIPAL_AND_INTEREST,
    }

    integer_fields = {
        LOAN_ID,
        NOTE_ID,
        ORDER_ID,
        DAYS_SINCE_LAST_PAYMENT,
        REMAINING_PAYMENTS,
    }


class CreditScoreTrend(object):
    UP = 'UP'
    DOWN = 'DOWN'
    FLAT = 'FLAT'


class Status(object):
    ISSUED = 'Issued'
    CURRENT = 'Current'
    GRACE = 'In Grace Period'
    LATE_16_TO_30 = 'Late (16-30 Days)'
    LATE_31_TO_120 = 'Late (31-120 Days)'


class LoanClass(object):
    A = {'A1', 'A2', 'A3', 'A4', 'A5'}
    B = {'B1', 'B2', 'B3', 'B4', 'B5'}
    C = {'C1', 'C2', 'C3', 'C4', 'C5'}
    D = {'D1', 'D2', 'D3', 'D4', 'D5'}
    E = {'E1', 'E2', 'E3', 'E4', 'E5'}
    F = {'F1', 'F2', 'F3', 'F4', 'F5'}


class LoanMaturity(object):
    THIRTY_SIX_MONTHS = '36'
    SIXTY_MONTHS = '60'
