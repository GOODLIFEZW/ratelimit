class RateLimitException(Exception):
    def __init__(self, message, period_remaining):
        '''
        param string message: Custom exception message.
        param float period_remaining: The time remaining until the rate limit is reset.
        '''
        super(RateLimitException, self).__init__(message)
        self.period_remaining = period_remaining