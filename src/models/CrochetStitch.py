import bpy
import os
import math
class CrochetStitch:
    # different 3D design per stitch
    def __init__(self):
        self.object_name = "NurbsCurve"
        self.import_name = "NurbsCurve"
        self.rotation = 0


    def to_string(self):
        # this will be how we transcribe pattern in a written format
        pass
    def get_file_path(self):
        pass

    def get_model(self):
        file_path = self.get_file_path()
        with bpy.data.libraries.load(file_path) as (data_from, data_to):
            data_to.objects = [name for name in data_from.objects if name == self.object_name]

        for obj in data_to.objects:
            bpy.context.collection.objects.link(obj)

        print("import_name", self.import_name)
        highest_object = None
        highest_num = 0
        for obj in bpy.context.scene.objects:
            if obj.name.startswith(self.object_name):
                name = obj.name.replace(self.object_name, "")
                if len(name) > 0:
                    name = int(name.strip("."))
                    if name > highest_num:
                        highest_object = obj
                        highest_num = name
                else:
                    highest_object = obj
        imported_object = highest_object
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        # rotation_angle = math.radians(self.rotation)  # Convert rotation to radians
        # imported_object.rotation_euler.rotate_axis("Y", rotation_angle)
        return imported_object

    def get_object_name(self):
        return self.object_name

    def reset_count(self):
        pass

class SingleCrochet(CrochetStitch):
    object_name = "SingleCrochet"
    def __init__(self):
        super().__init__()
        self.object_name = "SingleCrochet"

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/single-crochet.blend"
        return file_path

class Chain(CrochetStitch):
    object_name = "ChainStitch"
    def __init__(self):
        super().__init__()
        self.object_name = "ChainStitch"

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/chain-stitch.blend"
        return file_path

class VerticalChain(CrochetStitch):
    object_name = "ChainStitch"
    def __init__(self):
        super().__init__()
        self.object_name = "ChainStitch"
        self.rotation = 50

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/chain-stitch.blend"
        return file_path

class SlipStitch(CrochetStitch):
    object_name = "SlipStitch"
    def __init__(self):
        super().__init__()
        self.object_name = "SlipStitch"


    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/slip-stitch.blend"
        return file_path

class DoubleCrochet(CrochetStitch):
    object_name = "DoubleCrochet"

    def __init__(self):
        super().__init__()
        self.object_name = "DoubleCrochet"

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/double-crochet.blend"
        return file_path

class HalfDouble(CrochetStitch):
    object_name = "HalfDouble"
    def __init__(self):
        super().__init__()
        self.object_name = "HalfDouble"

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/half-double-crochet.blend"
        return file_path

class Row():

    def __init__(self, array_size=0, max_size = float('inf')):
        self.stitch_array = []
        self.array_size = array_size
        self.tuples = []
        self.max_height = 0
        self.height_dict = {"DoubleCrochet": 0.029654, "HalfDouble": 0.026165, "ChainStitch": 0.007266,
                            "SingleCrochet":0.00921, "SlipStitch": 0.006553}
        self.width_dict = {"DoubleCrochet": 0.021465, "HalfDouble": 0.018758, "ChainStitch": 0.017289,
                            "SingleCrochet": 0.009214, "SlipStitch": 0.021793}
        self.modified_stack = []

    def get_array(self):
        return self.stitch_array

    def get_array_size(self):
        return self.array_size

    def get_max_height(self):
        return self.max_height

    def add_stitch(self, stitch):
        print("here is modified", self.modified_stack)
        self.stitch_array.append(stitch)
        self.array_size += 1
        height = self.height_dict[stitch.object_name]
        if height > self.max_height:
            self.max_height = height

    def to_string(self):
        pass

    def undo(self):
        last_modified = self.modified_stack.pop()
        print(last_modified, len(self.stitch_array))
        for idx in reversed(last_modified):
            self.stitch_array.pop(idx) #removes modified items from stitch array
        self.array_size = len(self.stitch_array)
        self.tuples.pop()

    def add_to_tuples(self, stitch, amount, modified_indexes):
        self.modified_stack.append(modified_indexes)
        self.tuples.append((stitch(), amount))


    def get_tuples(self):
        return self.tuples


if __name__ == "__main__":
    row = Row()
    row.add_stitch(SingleCrochet())
    row.add_stitch(Chain())
    row.add_stitch(SingleCrochet())
    row.add_stitch(SingleCrochet())