# Copyright © 2020 United States Government as represented by the Administrator of the National Aeronautics and Space Administration.  All Rights Reserved.

from prog_algs import state_estimator

class TemplateStateEstimator(state_estimator.StateEstimator):
    """
    Template for State Estimator
    """
    t = 0 # Last timestep

    # REPLACE THE FOLLOWING LIST WITH CONFIGURED PARAMETERS
    parameters = { # Default Parameters, used as config for UKF
        'Example Parameter': 0.0
    } 

    def __init__(self, model, options = {}):
        """
        Constructor
        """
        self.model = model

        self.parameters.update(options)# Merge configuration options into default
        # ADD PARAMETER CHECKS HERE

    def estimate(self, t, z):
        """
        Perform one state estimation step (i.e., update the state estimate)

        Parameters
        ----------
        t : double
            Current timestamp in seconds (≥ 0.0)
            e.g., t = 3.4
        u : dict
            Measured inputs, with keys defined by model.inputs.
            e.g., u = {'i':3.2} given inputs = ['i']
        z : dict
            Measured outputs, with keys defined by model.outputs.
            e.g., z = {'t':12.4, 'v':3.3} given inputs = ['t', 'v']
        """
        # REPLACE WITH UPDATE STATE ESTIMATION
        pass

    @property
    def x(self):
        """
        Getter for property 'x', the current estimated state. 

        Example
        -------
        state = observer.x
        """
        # REPLACE THE FOLLOWING WITH THE LOGIC TO CONSTRUCT/RETURN THE STATE
        x = {key: 0.0 for key in self.model.states}

        return x