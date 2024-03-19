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
        self.init_stitches()

    def init_stitches(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        sc = CrochetStitch.SingleCrochet()
        ch = CrochetStitch.Chain()
        self.stitch = sc.get_model()
        self.chain = ch.get_model()


    def addRow(self, amount, type: CrochetStitch):
        for n in range(0, amount):
            self.cur_row.add_stitch(type)

    def newRow(self):
        self.cur_row = CrochetStitch.Row()

    def addStitch(self, type: CrochetStitch):
        self.cur_row.add_stitch(type)
        self.notifyObservers()

    def build(self):

        # Path to the .blend file
        output_blend_file_path = os.getcwd() + "/assets/new_pattern.blend"
        new_y = 0
        for row in self.rows:
            stitch_tuples = row.get_tuples()
            # TODO : go through tuple list and add to arraymodifier accordingly





        # Name of the object you want to add the array modifier to
        object_one = "SingleCrochet"
        object_two = "ChainStitch"
        # Number of duplicates you want to create
        stitch_count = 2
        chain_count = 3
        # Offset values for X, Y, and Z axes
        offset_x = 0.01
        offset_y = 0
        offset_z = 0

        bpy.ops.wm.read_factory_settings(use_empty=True)

        # Load the .blend file
        with bpy.data.libraries.load(blend_file_path) as (data_from, data_to):
            data_to.objects = [name for name in data_from.objects if name == object_one]

        # Link the object to the scene
        for obj in data_to.objects:
            bpy.context.collection.objects.link(obj)

        # Load the .blend file
        with bpy.data.libraries.load(other_blend) as (data_from, data_to):
            data_to.objects = [name for name in data_from.objects if name == object_two]

        # Link the object to the scene
        for obj in data_to.objects:
            bpy.context.collection.objects.link(obj)

        # Set the current scene object to the imported object
        chain = next(obj for obj in bpy.context.scene.objects if obj.name.startswith(object_one))
        stitch = next(obj for obj in bpy.context.scene.objects if obj.name.startswith(object_two))

        array_modifier = chain.modifiers.new(name="Array", type='ARRAY')
        array_modifier.count = chain_count
        array_modifier.use_relative_offset = False
        array_modifier.use_constant_offset = True
        array_modifier.constant_offset_displace[0] = offset_x
        array_modifier.constant_offset_displace[1] = offset_y
        array_modifier.constant_offset_displace[2] = offset_z
        # array_modifier.merge = True  # Enable merge option

        # Add array modifier to oranges
        x_loc = offset_x * chain_count
        stitch.location = (x_loc, 0.0, 0.0)
        array_modifier = stitch.modifiers.new(name="Array", type='ARRAY')
        array_modifier.count = stitch_count
        array_modifier.use_relative_offset = False
        array_modifier.use_constant_offset = True

        array_modifier.constant_offset_displace[0] = offset_x
        array_modifier.constant_offset_displace[1] = offset_y
        array_modifier.constant_offset_displace[2] = offset_z

        # Apply the modifier to generate the duplicates
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

        self.build()
