# Copyright © 2021 United States Government as represented by the Administrator of the National Aeronautics and Space Administration. All Rights Reserved.

from prog_models.models import BatteryCircuit
from prog_algs import *
from prog_algs.uncertain_data import UnweightedSamples
# from prog_algs.visualize import plot_hist
# import matplotlib.pyplot as plt

def run_example():
    ## Setup
    def future_loading(t, x = None):
        # Variable (piece-wise) future loading scheme 
        if (t < 600):
            i = 2
        elif (t < 900):
            i = 1
        elif (t < 1800):
            i = 4
        elif (t < 3000):
            i = 2
        else:
            i = 3
        return {'i': i}

    batt = BatteryCircuit()

    ## State Estimation - perform a single ukf state estimate step
    filt = state_estimators.UnscentedKalmanFilter(batt, batt.parameters['x0'])

    import matplotlib.pyplot as plt  # For plotting
    print("Prior State:", filt.x.mean)
    print('\tSOC: ', batt.event_state(filt.x.mean)['EOD'])
    example_measurements = {'t': 32.2, 'v': 3.915}
    t = 0.1
    filt.estimate(t, future_loading(t), example_measurements)
    print("Posterior State:", filt.x.mean)
    print('\tSOC: ', batt.event_state(filt.x.mean)['EOD'])

    ## Prediction - Predict EOD given current state
    # Setup prediction
    mc = predictors.UnscentedKalmanPredictor(batt)

    # Predict with a step size of 0.1
    (times, inputs, states, outputs, event_states, eol) = mc.predict(filt.x, future_loading, dt=0.1)
    print(eol)
    # eol.plot_hist()
    # plt.show()

# This allows the module to be executed directly 
if __name__ == '__main__':
    run_example()
