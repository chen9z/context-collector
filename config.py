class Config:
    def __init__(self, args):
        self.path = args.path
        self.output = args.output
        self.user_ignores = args.user_ignores
        self.include_patterns = args.include_patterns
        self.exclude_patterns = args.exclude_patterns
