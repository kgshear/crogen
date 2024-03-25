from .CrochetStitch import CrochetStitch, Row, Chain, SingleCrochet
import bpy
import os


class CrochetModel:
    # use method to add

    def __init__(self):
        self.row_length = 0
        self.observers = []
        self.cur_row = Row()
        self.rows = []
        self.model_dict = {"Single": SingleCrochet, "Chain": Chain}
        self.camera = None
        self.light = None
        self.init_stitches()
        self.modified_objects = []


    def init_stitches(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.object.camera_add(location=(0, 0, 0), rotation=(-90 * 3.14159 / 180, 180* 3.14159 / 180,0))
        bpy.context.scene.render.resolution_x = 708
        bpy.context.scene.render.resolution_y = 495
        self.camera = bpy.context.object
        bpy.context.scene.camera = self.camera
        bpy.ops.object.light_add(type='POINT', location=(0, .5, .5))
        self.light = bpy.context.object
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'

    def addToRow(self, type, amount):
        self.modified_objects.clear()
        stitch = self.model_dict[type]
        if self.cur_row == None:
            self.newRow()
        for n in range(0, amount):
            self.cur_row.add_stitch(stitch)
            self.modified_objects.append(self.cur_row.array_size-1) #index of modified stitch
        self.build()



    def newRow(self):
        if self.cur_row.array_size > 0:
            self.rows.append(self.cur_row)
            self.cur_row = Row()
            self.row_length += 1
        for row in self.rows:
            print(row.stitch_array)

    def addStitch(self, type):
        self.cur_row.add_stitch(type)

    def clearPattern(self):
        self.row_length = 0
        self.rows = []
        self.cur_row = None
        self.init_stitches()

    def init_build(self):
        pass


    def build(self):
        output_blend_file_path = os.getcwd() + "/models/assets/new_pattern.blend"
        png_file_path = os.getcwd() + "/ui/creation/build/assets/model.png"
        offset_xyz = [0.01, 0, 0]
        new_z = 0
        all_rows = self.rows + [self.cur_row]
        new_x = 0
        for index, row in enumerate(all_rows):

            new_x = 0
            if (index == len(all_rows) - 1): # if at cur_row
                stitch_tuples = row.get_tuples(self.modified_objects)
                for tpl_idx, tpl in enumerate(stitch_tuples):
                    type, count = tpl
                    print(type.get_object_name())
                    if (tpl_idx == len(stitch_tuples)-1): #if it is the modified stitch
                        model = type.get_model()
                        if (model != None):
                            print(type.get_object_name(), " ", count, (new_x, 0, new_z))
                            model.location = (new_x, 0, new_z)
                            array_modifier = model.modifiers.new(name="Array", type='ARRAY')
                            array_modifier.count = count
                            array_modifier.use_relative_offset = False
                            array_modifier.use_constant_offset = True
                            array_modifier.constant_offset_displace[0] = offset_xyz[0]
                            array_modifier.constant_offset_displace[1] = offset_xyz[1]
                            array_modifier.constant_offset_displace[2] = offset_xyz[2]
                    new_x += offset_xyz[0] * count

            new_z += .005
        if (new_z == 0):
            new_z = .001
        self.camera.location = (new_x/2, (new_x + new_z) * 2, new_z/2 )

        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.filepath = png_file_path


        bpy.ops.render.render(write_still=True)

        bpy.ops.wm.save_as_mainfile(filepath=output_blend_file_path)



    # def save_png(self, output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 32, rotation_angle = 360.0, subject = bpy.context.object):
    #     original_rotation = subject.rotation_euler
    #     for step in range(0, rotation_steps):
    #         subject.rotation_euler[2] = radians(step * (rotation_angle / rotation_steps))
    #         bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
    #         bpy.ops.render.render(write_still=True)
    #     subject.rotation_euler = original_rotation
    def redo(self):
        pass

    def undo(self):
        pass

    # def addObserver(self, observer: PatternObserver):
    #     self.observers.append(observer)
    #
    # def removeObserver(self, observer: PatternObserver):
    #     self.observers.remove(observer)

    # def notifyObservers(self):
    #     for observer in self.observers:
    #         observer.update(self)

    # self.build()


if __name__ == "__main__":
    model = CrochetModel()
    model.newRow()
    model.addToRow("Single", 20)
    model.addToRow("Chain", 20)
    model.newRow()
    model.addToRow("Single", 20)

