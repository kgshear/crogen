
from pathlib import Path


from tkinter import Canvas, Button, PhotoImage, Frame, StringVar, OptionMenu, Entry
import numpy as np
from PIL import Image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class CreationView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg="#FFFFFF")
        self.set_empty()
        self.row_count = "0"
        self.stitch_count = "0"

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=800,
            width=1395,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            590.0,
            1.0,
            1395.0,
            801.0,
            fill="#BBA1DC",
            outline="")

        self.canvas.create_text(
            642.0,
            631.0,
            anchor="nw",
            text="Row Count:",
            fill="#FFFFFF",
            font=("Karla Regular", 36 * -1)
        )

        self.canvas.create_text(
            647.0,
            707.0,
            anchor="nw",
            text="Stitch Count:",
            fill="#FFFFFF",
            font=("Karla Regular", 36 * -1)
        )

        self.canvas.create_rectangle(
            340.0,
            183.0,
            554.0,
            218.71775817871094,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            352.0,
            183.0,
            558.0,
            219.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            429.0,
            307.0,
            558.0,
            343.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            394.0,
            245.0,
            558.0,
            281.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            340.0,
            183.0,
            554.0,
            218.71775817871094,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            398.0,
            243.0,
            554.0,
            278.71775817871094,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            639.0,
            562.0,
            820.0,
            568.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            906.0,
            631.0,
            999.0,
            682.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            906.0,
            708.0,
            999.0,
            759.0,
            fill="#FFFFFF",
            outline="")
        # label = Label(label_frame, text=”  # Text which you want to show in label”)
        # self.row_label = Label(930, 660.0, text=self.stitch_count, font=("Karla Regular", 36 * -1))
        self.row_text = self.canvas.create_text(930, 660.0, text=self.row_count, fill="black", font=("Karla Regular", 36 * -1))
        self.stitch_text = self.canvas.create_text(930, 737.0, text=self.stitch_count, fill="black", font=("Karla Regular", 36 * -1))

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.ClearButton = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.ClearButton.place(
            x=374.0,
            y=694.0,
            width=184.0,
            height=77.48383331298828
        )

        self.stitch_type = StringVar(self)
        self.stitch_type.set("Chain")  # Default selection
        self.stitch_dropdown = OptionMenu(self, self.stitch_type, "Chain")
        self.canvas.create_window(380, 205.0, window=self.stitch_dropdown)

        self.amount_select = StringVar(self)
        self.amount_select.set("1")  # Default selection
        self.amount_entry = Entry(self, textvariable= self.amount_select,  bg="lightgray")
        self.canvas.create_window(430, 265.0, window=self.amount_entry)

        self.canvas.create_text(
            270.0,
            190.0,
            anchor="nw",
            text="type:",
            fill="#000000",
            font=("Karla Medium", 24 * -1)
        )

        self.canvas.create_text(
            270.0,
            250.0,
            anchor="nw",
            text="amount:",
            fill="#000000",
            font=("Karla Medium", 24 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.AddButton = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.AddButton.place(
            x=22.0,
            y=192.51617431640625,
            width=215.0,
            height=148.48382568359375
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.RedoButton = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.RedoButton.place(
            x=275.0,
            y=575.0,
            width=215.0,
            height=77.48383331298828
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.UndoButton = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.UndoButton.place(
            x=22.0,
            y=572.0,
            width=215.0,
            height=77.48383331298828
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.NewButton = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.NewButton.place(
            x=20.0,
            y=419.0,
            width=215.0,
            height=77.48383331298828
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.BackButton = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.BackButton.place(
            x=20.0,
            y=677.0,
            width=296.0,
            height=94.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.CreateButton = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.CreateButton.place(
            x=1121.0,
            y=687.0,
            width=256.0,
            height=94.0
        )

        self.canvas.create_text(
            639.0,
            520.0,
            anchor="nw",
            text="Details",
            fill="#FFFFFF",
            font=("Karla Bold", 36 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            148.0,
            67.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            20.0,
            127.0,
            anchor="nw",
            text="Create your own pattern!",
            fill="#000000",
            font=("Karla Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            20.0,
            380.0,
            558.0,
            383.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            20.0,
            166.0,
            558.0,
            169.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            20.0,
            532.0,
            558.0,
            535.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            635,
            30,
            1343,
            491.5,
            fill="#FFFFFF",
            outline="")

        self.model_image = PhotoImage(file=relative_to_assets("model.png"))
        self.model_object = self.canvas.create_image(989.0,
                                                     260.0, image=self.model_image)
        self.canvas.pack()

    def update_png(self):
        self.model_image = PhotoImage(file=relative_to_assets("model.png"))


    def set_empty(self):
        img = np.zeros([100, 100, 3], dtype=np.uint8)
        img.fill(255)  # numpy array!
        im = Image.fromarray(img)  # convert numpy array to image
        im.save(relative_to_assets("model.png"))
        self.update_png()

    def update_stitch_count(self, new_count):
        self.stitch_count = new_count
        self.canvas.itemconfigure(self.stitch_text, text=self.stitch_count)

    def update_row_count(self, new_count):
        self.row_count = new_count
        self.canvas.itemconfigure(self.row_text, text=self.row_count)

    def update_stitch_dropdown(self, update_list):
        self.stitch_dropdown["menu"].delete(0, "end")
        for item in update_list:
            self.stitch_dropdown["menu"].add_command(
                label=item,
                command=lambda value=item: self.stitch_type.set(value)
            )
        self.stitch_type.set(update_list[0])