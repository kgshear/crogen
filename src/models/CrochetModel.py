from .CrochetStitch import CrochetStitch, Row, Chain, SingleCrochet, VerticalChain, SlipStitch, DoubleCrochet, HalfDouble
import bpy
import os


class CrochetModel:
    # use method to add

    def __init__(self):
        self.row_length = 0
        self.observers = []
        self.cur_row = Row()
        self.rows = []
        self.model_dict = {"Single": SingleCrochet, "Chain": Chain, "Double": DoubleCrochet, "Slip": SlipStitch, "Half-Double": HalfDouble}
        self.light = None
        self.init_scene()
        self.modified_objects = []
        self.history = []
        self.redo_stack = []
        self.build_count = 0



    def init_scene(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.context.scene.render.resolution_x = 708
        bpy.context.scene.render.resolution_y = 495

        cam = bpy.data.cameras.new("Camera 1")
        cam_obj = bpy.data.objects.new("Camera 1", cam)
        cam_obj.location = (0, 0, 0)
        cam_obj.rotation_euler = (-90 * 3.14159 / 180, 180* 3.14159 / 180,0)
        bpy.context.scene.collection.objects.link(cam_obj)
        bpy.context.scene.camera = cam_obj

        bpy.ops.object.light_add(type='POINT', location=(0, .5, .5))
        self.light = bpy.context.object
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
        bpy.ops.ed.undo_push(message="init")

    def get_camera_object(self):
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA':
                return obj


    def addToRow(self, type, amount, isRedo):
        self.modified_objects.clear()
        stitch = self.model_dict[type]
        if self.cur_row == None:
            self.newRow(isRedo)
        for n in range(0, amount):
            self.cur_row.add_stitch(stitch)
            self.modified_objects.append(self.cur_row.array_size-1) #index of modified stitch

        self.cur_row.add_to_tuples(stitch, amount, self.modified_objects.copy())
        self.build()
        action = {"type": "add_to_row", "param": (type, amount)}
        if not isRedo:
            self._add_to_history(action)



    def newRow(self, isRedo):
        if self.cur_row.array_size > 0:
            self.rows.append(self.cur_row)
            self.cur_row = Row()
            self.row_length += 1
            action = {"type": "new_row"}
            if not isRedo:
                self._add_to_history(action)
            # self.cur_row.add_stitch(VerticalChain) #new row- add verticle chain to end of row
            # self.modified_objects.append(self.cur_row.array_size - 1)
            # self.build()
        for row in self.rows:
            print(row.stitch_array)


    def addStitch(self, type):
        self.cur_row.add_stitch(type)

    def clearPattern(self):
        self.row_length = 0
        self.rows = []
        self.cur_row = Row()
        self.init_scene()

    def build(self):
        # TODO fix camera angles
        # TODO fix stitch overlap
        # TODO redo not working

        #bpy.context.window_manager.print_undo_steps()
        offset_xyz = [0.01, 0, 0]
        new_z = 0
        all_rows = self.rows + [self.cur_row]
        new_x = 0
        for index, row in enumerate(all_rows):
            new_x = 0
            if (index == len(all_rows) - 1): # if at cur_row
                stitch_tuples = row.get_tuples()
                for tpl_idx, tpl in enumerate(stitch_tuples):
                    type, count = tpl
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
            new_z += row.get_max_height() * .7
        if (new_z == 0):
            new_z = .001
        camera = self.get_camera_object()
        camera.location = (new_x/2, (new_x + new_z) * 2, new_z/2 )
        bpy.ops.ed.undo_push(message=str(self.build_count))
        self.save_png()
        self.build_count += 1

    def save_png(self):
        output_blend_file_path = os.getcwd() + "/models/assets/new_pattern.blend"
        png_file_path = os.getcwd() + "/ui/creation/build/assets/model.png"
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
        if self.redo_stack:
            isRedo = True
            action = self.redo_stack.pop()
            if action["type"] == "add_to_row":
                type, amount = action["param"]
                self.addToRow(type, amount, isRedo)
            elif action["type"] == "new_row":
                self.newRow(isRedo)
            self.history.append(action)

    def _add_to_history(self, action):
        self.history.append(action)
        # Clear redo stack whenever a new action is performed
        self.redo_stack = []

    def undo(self): #pressing undo when they have no stitches in their row means they want to undo "add row"
        if self.history:
            action = self.history.pop()
            if action["type"] == "add_to_row":
                print("undoing")
                # print(self.camera)
               # bpy.context.window_manager.print_undo_steps()
                bpy.ops.ed.undo()
                print("undone")
               # bpy.context.window_manager.print_undo_steps()
                self.cur_row.undo()
                self.save_png()
                # print(self.camera)
            elif action["type"] == "new_row":
                self.cur_row = self.rows.pop(-1)
            self.redo_stack.append(action)

if __name__ == "__main__":
    model = CrochetModel()
    model.newRow()
    model.addToRow("Single", 20)
    model.addToRow("Chain", 20)
    model.newRow()
    model.addToRow("Single", 20)

