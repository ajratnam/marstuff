class NamedException(Exception):
    def __new__(cls, name, err=None):
        def __init__(self, error):
            super(Exception, self).__init__(error)

        new_class = type(name, (Exception,), {'__init__': __init__})
        return new_class(err) if err else new_class

InvalidAPIKeyError = NamedException("InvalidAPIKeyError")
