def validate_config(config):
	for key, value in config.iteritems():
		assert isinstance(key, int)
		assert len(value) == 2
		assert 'value' in value
		assert 'condition' in value
		assert hasattr(value['condition'], '__call__')
