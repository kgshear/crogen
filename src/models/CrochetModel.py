from .CrochetStitch import CrochetStitch, Row, Chain, SingleCrochet, SlipStitch, DoubleCrochet, HalfDouble, VerticalChain
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

        self.cur_row.add_to_tuples(stitch(), amount, self.modified_objects.copy())
        self.build()
        action = {"type": "add_to_row", "param": (type, amount)}
        if not isRedo:
            self._add_to_history(action)

    def newRow(self, isRedo):
        if self.cur_row.array_size > 0:
            next_row_turned = False
            if self.cur_row.get_row_turned() == False:
                next_row_turned = True
            self.rows.append(self.cur_row)
            self.cur_row = Row()
            self.cur_row.set_row_turned(next_row_turned)
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
        self.history = []
        self.redo_stack = []

    def build(self):
        # TODO vertical chain stitches where necessary
        # TODO restrict illegal crochet moves

        offset_xyz = [0.5, 0, 0]
        new_z = 0
        all_rows = self.rows + [self.cur_row]
        new_x = 0
        max_length = 0
        last_stitch = None
        last_row = None
        for index, row in enumerate(all_rows):
            length = row.get_array_size() * .01
            if length > max_length:
                max_length = length
            if (index == len(all_rows) - 1): # if at cur_row
                turned = row.get_row_turned()
                stitch_tuples = row.get_tuples()
                if turned:
                    new_x = length + .01
                else:
                    new_x = 0
                for tpl_idx, tpl in enumerate(stitch_tuples):
                    stitch, count = tpl
                    if (tpl_idx == len(stitch_tuples)-1): #if it is the modified stitch
                        if turned:
                            stitch.set_turned()
                        model = stitch.get_model()
                        if (model != None):
                            model.location = (new_x, 0, new_z)
                            array_modifier = model.modifiers.new(name="Array", type='ARRAY')
                            array_modifier.count = count 
                            array_modifier.use_relative_offset = True
                            array_modifier.use_constant_offset = False
                            array_modifier.relative_offset_displace[0] = 0.5
                            array_modifier.relative_offset_displace[1] = 0
                            array_modifier.relative_offset_displace[2] = 0
                            pos_z = new_z
                            if last_stitch != None:
                                num_vert = last_stitch.calc_num_vectical(stitch)
                                if num_vert > 0:
                                    vertical_chain = VerticalChain()
                                    vert_model = vertical_chain.get_model()
                                    vert_model.location = (new_x, 0, pos_z)
                                    array_mod = vert_model.modifiers.new(name="Array", type='ARRAY')
                                    array_mod.count = num_vert
                                    array_mod.use_relative_offset = True
                                    array_mod.use_constant_offset = False
                                    array_mod.relative_offset_displace[0] = 0
                                    array_mod.relative_offset_displace[1] = 0
                                    array_mod.relative_offset_displace[2] = .5
                            elif last_stitch == None and last_row != None: # if need turning stitches
                                last_stitch = last_row.get_tuples()[-1][0]
                                num_vert = last_stitch.get_turning_num()
                                if num_vert > 0:
                                    pos_z -= new_z
                                    vert_x = 0
                                    vertical_chain = VerticalChain()

                                    if turned:
                                        vert_x = last_row.get_array_size() * .01
                                        vertical_chain.set_turn_left()
                                    else:
                                        vertical_chain.set_turn_right()

                                    vert_model = vertical_chain.get_model()
                                    pos_z -= last_stitch.get_turning_num()

                                    vert_model.location = (vert_x, 0, pos_z)
                                    array_mod = vert_model.modifiers.new(name="Array", type='ARRAY')
                                    array_mod.count = num_vert
                                    array_mod.use_relative_offset = True
                                    array_mod.use_constant_offset = False
                                    array_mod.relative_offset_displace[0] = 0
                                    array_mod.relative_offset_displace[1] = 0
                                    array_mod.relative_offset_displace[2] = .5

                    last_stitch = stitch
                    if not turned:
                        new_x += .01 * count

            else:
                last_row =  row
            new_z += row.get_max_height() * .9
        if (new_z == 0):
            new_z = .001
        camera = self.get_camera_object()
        camera.location = (max_length/2, max_length * 2 + new_z, new_z/2 )
        bpy.ops.ed.undo_push(message=str(self.build_count))
        self.save_png()
        self.build_count += 1
        self.generate_written_pattern()

    def save_png(self):
        output_blend_file_path = os.getcwd() + "/models/assets/new_pattern.blend"
        png_file_path = os.getcwd() + "/ui/creation/build/assets/model.png"
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.filepath = png_file_path
        bpy.ops.render.render(write_still=True)
        bpy.ops.wm.save_as_mainfile(filepath=output_blend_file_path)

    def generate_written_pattern(self):

       # chain and turn
        # hdc 2
        # dc 3
        # slip, sc ch 1

       # after first row
       # hdc 3 from hook
       # dc 4 from hook
       # sc 2 from hook

        written_pattern = []
        row_num = 1
        all_rows = self.rows + [self.cur_row]
        first_row = all_rows[0]
        last_row = all_rows[-1]

        for idx, row in enumerate(all_rows):
            if row.get_array_size() != 0:
                row_string = f'Row {row_num}: '
                if row != first_row:
                    # if not first row, determine how many stitches away from
                    # current stitch to insert hook
                    first_stitch = row.get_tuples()[0][0]
                    row_string += first_stitch.to_string_from_stitch()

                row_string += f'{row.to_string()}'
                if row != last_row:
                    # if not last row, determine how many chain stitches need to be made
                    # to accomodate stitch in next row
                    next_row = all_rows[idx+1]
                    if next_row.get_array_size() != 0:
                        next_stitch = next_row.tuples[0][0]
                        row_string += f", {next_stitch.to_string_turning()}"
                row_num += 1
                row_string += "\n"
                written_pattern.append(row_string)

        print("written pattern ", written_pattern)
        written_pattern = "".join(written_pattern)
        return written_pattern






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

    def get_stitch_count(self):
        count = 0
        for row in self.rows:
            count += row.get_array_size()
        count += self.cur_row.get_array_size()
        return count

    def get_row_count(self):
        count = len(self.rows)
        if self.cur_row.get_array_size() > 0:
            count += 1
        return count

if __name__ == "__main__":
    model = CrochetModel()
    # model.newRow()
    # model.addToRow("Single", 20)
    # model.addToRow("Chain", 20)
    # model.newRow()
    # model.addToRow("Single", 20)

