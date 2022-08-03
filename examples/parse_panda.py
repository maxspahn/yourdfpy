import os

from yourdfpy import urdf
import yourdfpy

__author__ = "Clemens Eppner"
__copyright__ = "Clemens Eppner"
__license__ = "MIT"


DIR_CURRENT = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
DIR_MODELS = os.path.abspath(os.path.join(DIR_CURRENT, "../tests/models"))

def parse_panda():
    urdf_fname = os.path.join(DIR_MODELS, "franka", "franka.urdf")
    urdf_model: urdf.URDF = urdf.URDF.load(urdf_fname)
    urdf_model.update_cfg([0.1, 0, 0, -1.501, 0.0, 1.8675, 0.0, 0.0])
    tf1 = urdf_model.get_transform("panda_link8", frame_from="panda_link0")
    print(tf1)
    urdf_model.show()

if __name__ == "__main__":
    parse_panda()
