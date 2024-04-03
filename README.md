# crogen


SRC contains all the relevant code for the project

CrochetModel.py contains all of the functions for making changes to the 3D model. This file is incomplete.
CrochetStitch.py contains all of the different stitch types 
Crogen.py will be used to run the application

In the folder ui:
contains Creation, Build, and Detail. Also contains View.py which holds the different views

Creation contains all of the files related to the creation window
> build contains assets and CreationView
> assets are pictures used in the CreationView and CreationView contains the Tkinter Code for the Creation Window gui

Detail contains all of the files related to the creation window
> build contains assets and DetailView
> assets are pictures used in the DetailView and DetailView contains the Tkinter Code for the Detail Window gui

Pattern contains all of the files related to the pattern window
> build contains assets and PatternView
> assets are pictures used in the PatternView and PatternView contains the Tkinter Code for the Pattern Window gui


In the folder Controller:
contains controllers for the various view files, manages views

In the folder Model:
contains 3D models and contains the CrochetModel and CrochetStitch classes which hold the data of the 3D model the user is creating
