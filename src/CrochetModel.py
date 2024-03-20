import CrochetStitch
import PatternObserver
import bpy
import os

class CrochetModel:
    # use method to add

    def __init__(self):
        self.chain = None
        self.stitch = None
        self.row_length = 0
        self.observers = []
        self.cur_row = CrochetStitch.Row()
        self.rows = []
        self.model_dict = {}
        self.init_stitches()


    def init_stitches(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        sc = CrochetStitch.SingleCrochet()
        ch = CrochetStitch.Chain()
        self.model_dict[sc.get_object_name()] = sc.get_model()
        self.model_dict[ch.get_object_name()] = ch.get_model()


    def addToRow(self, type: CrochetStitch, amount):
        for n in range(0, amount):
            self.cur_row.add_stitch(type)

    def newRow(self):
        self.cur_row = CrochetStitch.Row()
        self.rows.append(self.cur_row)

    def addStitch(self, type: CrochetStitch):
        self.cur_row.add_stitch(type)
        self.notifyObservers()

    def build(self):

        output_blend_file_path = os.getcwd() + "/assets/new_pattern.blend"

        offset_xyz = [0.01, 0, 0]
        new_z = 0
        bpy.ops.wm.read_factory_settings(use_empty=True)
        for row in self.rows:
            stitch_tuples = row.get_tuples()
            print(stitch_tuples)
            new_x = 0
            for type, count in stitch_tuples:
                model = self.model_dict[type.get_object_name()] #TODO fix this (everything worked before i tried adding 3 rows vs 2)
                model.location = (new_x, 0, new_z)
                array_modifier = model.modifiers.new(name="Array", type='ARRAY')
                array_modifier.count = count
                array_modifier.use_relative_offset = False
                array_modifier.use_constant_offset = True
                array_modifier.constant_offset_displace[0] = offset_xyz[0]
                array_modifier.constant_offset_displace[1] = offset_xyz[1]
                array_modifier.constant_offset_displace[2] = offset_xyz[2]
                new_x = offset_xyz[0] * count
            new_z += .007
        bpy.ops.wm.save_as_mainfile(filepath=output_blend_file_path)

    def redo(self):
        pass

    def undo(self):
        pass

    def addObserver(self, observer: PatternObserver):
        self.observers.append(observer)

    def removeObserver(self, observer: PatternObserver):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self)

        # self.build()


if __name__ == "__main__":
    model = CrochetModel()
    model.newRow()
    model.addToRow(CrochetStitch.SingleCrochet(), 5)
    model.newRow()
    model.addToRow(CrochetStitch.Chain(), 5)
    # model.newRow()
    # model.addToRow(CrochetStitch.SingleCrochet, 5)
    model.build()

