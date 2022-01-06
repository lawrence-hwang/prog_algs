# Copyright © 2021 United States Government as represented by the Administrator of the National Aeronautics and Space Administration.  All Rights Reserved.

from .monte_carlo import MonteCarlo
from .predictor import Predictor
from .prediction import Prediction, UnweightedSamplesPrediction
from .toe_prediction_profile import ToEPredictionProfile
from .unscented_transform import UnscentedTransformPredictor

# For naming consistancy
# Unortionately, prog_algs was released with inconsistant naming (UnscentedTransformPredictor vs MonteCarlo).
# For naming consistancy and to avoid confusion, we created aliases for the two classes.
# They can be called by the name of the method (e.g., UnscentedTranform) or with 'predictor' at the end (e.g., UnscentedTransformPredictor).
UnscentedTransform = UnscentedTransformPredictor
MonteCarloPredictor = MonteCarlo

__all__ = ['predictor', 'monte_carlo', 'monte_carlo2', 'unscented_transform', 'MonteCarlo', 'Predictor', 'Prediction', 'UnweightedSamplesPrediction', 'ToEPredictionProfile', 'UnscentedTransformPredictor', 'UnscentedTransform', 'MonteCarloPredictor']
