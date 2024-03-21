from models import CrochetModel
from ui.View import View
from controllers.Controller import Controller

def main():
    model = CrochetModel.CrochetModel()
    view = View()
    controller = Controller(model, view)
    controller.start()
    pass

if __name__ == "__main__":
    main()