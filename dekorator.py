
import time
import functools

def timer_decorator(unit):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.time()
            value = func(*args, **kwargs)
            end_time = time.time()
            run_time = end_time - start_time
            if unit == 'seconds':
                print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            elif unit == 'microseconds':
                print(f"Finished {func.__name__!r} in {run_time * 1e6:.4f} microsecs")
            else:
                raise ValueError("Invalid unit. Must be 'seconds' or 'microseconds'.")
            return value
        return wrapper_timer
    return decorator

#uzycie 
@timer_decorator('seconds')
def slow_function():
    time.sleep(2)  # tworzenie wolnej func

@timer_decorator('microseconds')
def fast_function():
    for i in range(10000):
        pass  # szybka funkcja

slow_function()
fast_function()