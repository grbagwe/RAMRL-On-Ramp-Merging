from gym.spaces import Box
import numpy as np
from config_file.customFeatureExtractor import CustomCombinedExtractor
#from customFeatureExtractor import CustomCombinedExtractor
policy_kwargs = dict(
    features_extractor_class=CustomCombinedExtractor,
    features_extractor_kwargs=dict(cnn_output_dim=2046),

    net_arch=[1024, dict(vf=[512, 128, 32], pi=[512, 128, 32])],
                    )

action_space = {'high': 3,
                'low': -4.5}
image_shape = (200, 768,3)
obsspaces = {
    'image': Box(low=0, high=255, shape=image_shape, dtype=np.uint8),

}

weights = {'alphasl0': 0.5,
           'alphasl1': 0.5,
           'rSuccess': 150,
           'alphaO': 0.1,
           'rTimeAlpha': 0.01,
           'alphaD': 0.25,
           'rC': -150,
           'alphaDistance': 0.5,
           'alphaP': 0.5,
           'alphaJ': 0.08
           }
sumoParameters = {'maxSpeed':30 ,
                  'episodeLength': 600
                  }


