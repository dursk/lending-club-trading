import csv


def validate_config(config):
    for key, value in config.iteritems():
        assert isinstance(key, int)
        assert len(value) == 2
        assert 'value' in value
        assert 'condition' in value
        assert hasattr(value['condition'], '__call__')


def config_matches_csv(config, csv_file):
    with open(csv_file, 'r') as f:
        row = csv.reader(f).next()
        assert len(row) >= max(config)
