import bpy
import os
class CrochetStitch:
    # different 3D design per stitch
    def __init__(self):
        self.object_name = "NurbsCurve"
        pass

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

        imported_object = bpy.context.scene.objects[self.object_name]
        return imported_object

class SingleCrochet(CrochetStitch):
    def __init__(self):
        super().__init__()


    def get_file_path(self):
        file_path = os.getcwd() + "/assets/single-crochet.blend"
        return file_path



class Chain(CrochetStitch):
    def __init__(self):
        super().__init__()

    def get_file_path(self):
        file_path = "/assets/chain-stitch.blend"
        return file_path

class Slip(CrochetStitch):
    def __init__(self):
        super().__init__()

class DoubleCrochet(CrochetStitch):
    def __init__(self):
        super().__init__()

class HalfDouble(CrochetStitch):
    def __init__(self):
        super().__init__()


class Row():
    stitch_array = None
    array_size = None
    max_size = None
    remainder = None

    def __init__(self, stitch_array=None, array_size=0, max_size = float('inf')):
        self.stitch_array = stitch_array
        self.array_size = array_size
        self.max_size = max_size
        self.remainder = []
        self.row_finished = False

    def set_array(self, stitch_array):
        self.stitch_array = stitch_array

    def set_array_size(self, array_size):
        self.array_size = array_size

    def set_max_size(self, max_size):
        self.max_size = max_size

    def get_array(self):
        return self.stitch_array

    def get_array_size(self):
        return self.array_size

    def get_max_size(self):
        return self.max_size

    def add_stitch(self, stitch):
        if self.max_size < (self.array_size + 1):
            self.remainder.append(stitch)
            self.row_finished = True
        else:
            self.stitch_array.append(stitch)
            self.array_size += 1

    def add_n_stitches(self, amount, stitch):
        for n in range(amount):
            self.add_stitch(stitch)

    def to_string(self):
        pass



