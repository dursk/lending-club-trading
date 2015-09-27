# Quickstart

Define a search config:

    >>> from scanner.constants import Field, LoanClass
    >>> from scanner.lookups import greater_than, is_in
    >>> my_config = {
            Field.OUTSTANDING_PRINCIPAL: {
                'value': 50,
                'condition': greater_than
            },
            Field.LOAN_CLASS: {
                'value': LoanClass.B,
                'condition': is_in
            }
        }

And then process a CSV file:

    >>> from scanner.processor import scan_csv
    >>> scan_csv('my_csv_file.csv', my_config)

You will get back a list of all the notes which
meet the criteria.
