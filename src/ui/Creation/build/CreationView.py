
from pathlib import Path


from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def CreationView(parent):

    parent.geometry("1395x800")
    parent.configure(bg = "#FFFFFF")

    canvas = Canvas(
        parent,
        bg = "#FFFFFF",
        height = 800,
        width = 1395,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        590.0,
        1.0,
        1395.0,
        801.0,
        fill="#BBA1DC",
        outline="")

    canvas.create_text(
        642.0,
        631.0,
        anchor="nw",
        text="Stitch Count:",
        fill="#FFFFFF",
        font=("Karla Regular", 36 * -1)
    )

    canvas.create_text(
        647.0,
        707.0,
        anchor="nw",
        text="Row Count:",
        fill="#FFFFFF",
        font=("Karla Regular", 36 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        989.0,
        244.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        340.0,
        183.0,
        554.0,
        218.71775817871094,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        352.0,
        183.0,
        558.0,
        219.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        429.0,
        307.0,
        558.0,
        343.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        394.0,
        245.0,
        558.0,
        281.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        340.0,
        183.0,
        554.0,
        218.71775817871094,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        398.0,
        243.0,
        554.0,
        278.71775817871094,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        639.0,
        562.0,
        820.0,
        568.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        906.0,
        631.0,
        999.0,
        682.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        906.0,
        708.0,
        999.0,
        759.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=374.0,
        y=694.0,
        width=184.0,
        height=77.48383331298828
    )

    canvas.create_text(
        406.0,
        187.0,
        anchor="nw",
        text="single",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        468.0,
        245.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        406.0,
        187.0,
        anchor="nw",
        text="single",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        269.0,
        185.0,
        anchor="nw",
        text="type:",
        fill="#000000",
        font=("Karla Medium", 24 * -1)
    )

    canvas.create_text(
        269.0,
        312.0,
        anchor="nw",
        text="stitch or row:",
        fill="#000000",
        font=("Karla Medium", 24 * -1)
    )

    canvas.create_text(
        269.0,
        245.0,
        anchor="nw",
        text="amount:",
        fill="#000000",
        font=("Karla Medium", 24 * -1)
    )

    canvas.create_text(
        457.0,
        309.0,
        anchor="nw",
        text="select",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=22.0,
        y=192.51617431640625,
        width=215.0,
        height=148.48382568359375
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=275.0,
        y=575.0,
        width=215.0,
        height=77.48383331298828
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=22.0,
        y=572.0,
        width=215.0,
        height=77.48383331298828
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=20.0,
        y=419.0,
        width=215.0,
        height=77.48383331298828
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=20.0,
        y=677.0,
        width=296.0,
        height=94.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=1121.0,
        y=687.0,
        width=256.0,
        height=94.0
    )

    canvas.create_text(
        639.0,
        520.0,
        anchor="nw",
        text="Details",
        fill="#FFFFFF",
        font=("Karla Bold", 36 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        148.0,
        67.0,
        image=image_image_2
    )

    canvas.create_text(
        20.0,
        127.0,
        anchor="nw",
        text="Create your own pattern!",
        fill="#000000",
        font=("Karla Bold", 32 * -1)
    )

    canvas.create_rectangle(
        20.0,
        380.0,
        558.0,
        383.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        20.0,
        166.0,
        558.0,
        169.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        20.0,
        532.0,
        558.0,
        535.0,
        fill="#D9D9D9",
        outline="")
    parent.resizable(False, False)
    parent.mainloop()

CreationView(Tk())