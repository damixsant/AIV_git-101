SUFFIXES = ['KB', 'MB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    # Convert a file size to human-readable form.
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple:
        if size < multiple:
            return f'{size}{suffix}'
    raise ValueError('number 8==D')