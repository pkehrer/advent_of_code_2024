import time

def get_input(filename):
    with open(f'input/{filename}.txt', 'r') as f:
        return list(map(lambda l: l.strip(), f.readlines()))


def time_fn(fn):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    seconds = end - start
    timestr = f'{seconds:.2f}s' if seconds > 1 else f'{(seconds * 1000):.1f}ms'
    print(f'function executed in {timestr}')