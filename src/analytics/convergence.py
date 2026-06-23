# convergence.py
import numpy as np
import time 

class convergence():

    def __init__(self):
        return None

    def analysis(self, sample_sizes, repeat_draw_size, sampler, targets, estimator, track_runtime=False):
        
        # Storing data.
        estimator_mean = []
        estimator_sdev = []
        estimator_rmse = []
        error_abs_mean = []
        runtime_mean = []

        # Start loop.
        repeat_draws = range(1, repeat_draw_size + 1)
        for sample_size in sample_sizes:
            # Storing data per sample size.
            estimator_tracker = []
            error_abs_tracker = []
            if track_runtime:
                runtime = []
            # Get repeated draws for this sample size.
            for draw in repeat_draws:
                if track_runtime:
                    time_start = time.perf_counter()

                # Draw the random numbers.
                # >>> This part you should update because we are explicitly defining the data here.
                # but in practice this should parameterize the data call ie make it more abstract.
                # I'm not sure if I like the way this is done. For now it is like we are sampling the same thing at varying sizes.
                # And it is abstract enough that it can be ANY sampler.
                samples = sampler(sample_size)
                # np.random.normal(loc=0.0, scale=1.0, size=sample_size)
                
                # Calculate estimator based on this sample.
                mu_n = estimator(samples)
                estimator_tracker.append(mu_n)
                error_abs_tracker.append(abs(mu_n - targets))
                
                if track_runtime:
                    time_end = time.perf_counter()
                    runtime.append(time_end - time_start)

            # Calculate the mean and error of estimates at this sample size.
            estimator_mean.append(np.mean(estimator_tracker))
            error_abs_mean.append(np.mean(error_abs_tracker))
            if track_runtime:
                runtime_mean.append(np.mean(runtime))

            # Compute standard deviation and the RMSE of estimates.
            estimator_sdev.append(np.std(estimator_tracker, ddof=1))
            estimator_rmse.append(np.sqrt(np.mean((np.array(estimator_tracker) - np.array(targets)) ** 2)))

        if track_runtime:
            return estimator_mean, estimator_sdev, estimator_rmse, error_abs_mean, track_runtime
        return estimator_mean, estimator_sdev, estimator_rmse, error_abs_mean
        
    def data_store():
        return None
