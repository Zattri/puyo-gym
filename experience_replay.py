import json
import numpy as np
import skimage.measure
import matplotlib.pyplot as plt

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class ExperienceReplay():
    observations = []

    def appendObservation(self, image_array, action_array):
        obs_tuple = (image_array, action_array)
        self.observations.append(obs_tuple)

    def saveFile(self, file_name="data", folder="experiences"):
        file_path = folder + "/" + file_name + ".json"
        print(f"Saving observations to {file_path}...")
        with open(file_path, "w") as fjson:
            json.dump(self.observations, fjson, cls=NumpyEncoder)
            fjson.close()
        print("Finished Saving!")

    def getObservation(self, x_index, y_index): # Won't work anymore - rejig
        return np.asarray(self.observations[x_index][y_index])

    def compressObservation(self, obs):
        return skimage.measure.block_reduce(obs, (2, 2, 1), np.max)

    #def readObservationsFromFile(self, file_path):
        #json_load = json.loads(json_dump)
        #a_restored = np.asarray(json_load["a"])