import bpy
import os
import math
class CrochetStitch:
    # different 3D design per stitch
    def __init__(self):
        self.abbrev = "st"
        self.turning_num = 0
        self.hook_dist_num = 0
        self.object_name = "NurbsCurve"
        self.import_name = "NurbsCurve"
        self.rotation = 0

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

    def get_abbrev(self):
        return self.abbrev

    def to_string(self):
        # how many stitches to put in row
        st_string = f"({self.abbrev} in every stitch across) x insert_amount"
        return st_string

    def to_string_turning(self):
        # how many stitches to chain when starting a new row
        st_string = f"ch {self.turning_num} and turn. "
        return st_string

    def to_string_from_stitch(self):
        # when starting a new row, this guides where to put the stitch
        st_string = f"yo, insert hook {self.hook_dist_num} stitches away from hook. "
        return st_string

    # def to_string_switch_stitch(self):
    #     st_string = f"ch {self.turning_num}"
    #     return st_string

    def switch_string(self, stitch):
        #  how much to ch when going from one stitch type to another
        st_string = ""
        if self.turning_num >= stitch.turning_num:
            return st_string
        else:
            st_string = f"ch {stitch.turning_num- self.turning_num}, "
            return st_string


class SingleCrochet(CrochetStitch):
    def __init__(self):
        super().__init__()
        self.object_name = "SingleCrochet"
        self.abbrev = "sc"
        self.turning_num = 1
        self.hook_dist_num = 2

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/single-crochet.blend"
        return file_path

class Chain(CrochetStitch):
    def __init__(self):
        super().__init__()
        self.object_name = "ChainStitch"
        self.abbrev = "ch"
        self.turning_num = 0
        self.hook_dist_num = 0

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/chain-stitch.blend"
        return file_path

    def to_string(self):
        st_string = "ch insert_amount"
        return st_string

    def to_string_turning(self):
        empty_str = ""
        return empty_str

    def to_string_from_stitch(self):
        empty_str = ""
        return empty_str

class SlipStitch(CrochetStitch):
    def __init__(self):
        super().__init__()
        self.object_name = "SlipStitch"
        self.abbrev = "sl st"
        self.turning_num = 0
        self.hook_dist_num = 2


    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/slip-stitch.blend"
        return file_path

    def to_string_turning(self):
        empty_str = ""
        return empty_str

class DoubleCrochet(CrochetStitch):

    def __init__(self):
        super().__init__()
        self.object_name = "DoubleCrochet"
        self.abbrev = "dc"
        self.turning_num = 3
        self.hook_dist_num = 4

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/double-crochet.blend"
        return file_path

class HalfDouble(CrochetStitch):

    def __init__(self):
        super().__init__()
        self.object_name = "HalfDouble"
        self.abbrev = "hdc"
        self.turning_num = 2
        self.hook_dist_num = 3

    def get_file_path(self):
        file_path = os.getcwd() + "/models/assets/half-double-crochet.blend"
        return file_path

class Row():

    def __init__(self, array_size=0, max_size = float('inf')):
        self.stitch_array = []
        self.array_size = array_size
        self.tuples = []
        self.max_height = 0
        self.height_dict = {"DoubleCrochet": 0.035634, "HalfDouble": 0.028855, "ChainStitch": 0.007266,
                            "SingleCrochet":0.009214, "SlipStitch": 0.006553}
        self.width_dict = {"DoubleCrochet": 0.02, "HalfDouble": 0.02, "ChainStitch": 0.02,
                            "SingleCrochet": 0.02, "SlipStitch": 0.02}
        self.modified_stack = []

    def get_array(self):
        return self.stitch_array

    def get_array_size(self):
        return self.array_size

    def get_max_height(self):
        return self.max_height

    def add_stitch(self, stitch):
        #print("here is modified", self.modified_stack)
        self.stitch_array.append(stitch)
        self.array_size += 1
        height = self.height_dict[stitch().object_name]
        if height > self.max_height:
            self.max_height = height

    def undo(self):
        last_modified = self.modified_stack.pop()
        print(last_modified, len(self.stitch_array))
        for idx in reversed(last_modified):
            self.stitch_array.pop(idx) #removes modified items from stitch array
        self.array_size = len(self.stitch_array)
        self.tuples.pop()

    def add_to_tuples(self, stitch, amount, modified_indexes):
        self.modified_stack.append(modified_indexes)
        self.tuples.append((stitch, amount))

    def get_tuples(self):
        return self.tuples

    def to_string(self):
        count = 0
        row_string = ""
        for stitch, amount in self.tuples:
            last_tuple = self.tuples[-1]

            row_string += stitch.to_string().replace("insert_amount", str(amount))
            if (stitch, amount) != last_tuple:
                row_string += ", "
                next_tuple = self.tuples[count+1]
                row_string += stitch.switch_string(next_tuple[0])

            count += 1
        return row_string




if __name__ == "__main__":
    row = Row()
    row.add_stitch(SingleCrochet())
    row.add_stitch(Chain())
    row.add_stitch(SingleCrochet())
    row.add_stitch(SingleCrochet())