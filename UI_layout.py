import PySimpleGUI as sg
class WindowLayout:
    def __init__(self, initAvgArr) -> None:
        self.buttonPadding = ' '*6
        self.class_Av_button = self.buttonPadding[:4] + "class average:" + self.buttonPadding[:4]
        self.test_Av_button = self.buttonPadding[:4] + "class test avg:" + self.buttonPadding[:4]
        self.clear_button = self.buttonPadding[:2] + "change section:" + self.buttonPadding[:0]
        self.class_work_avg= self.buttonPadding[:2] + "class work avg:" + self.buttonPadding[:1]
        # program info stuff
        self.progNam = "Grade Book"
        self.verNum = "v1.1.5"
        self.aboutMsg = f'About {self.progNam} {self.verNum}'
        self.placeHolder = '_DEFAULT_'
        # top menu bar layout
        # ------  Menu Definition ------ #    
        #  |  -------------------------  |
        #  |  | New | graphs | Help      |
        #  --------------------------------
        # new has more then one possible menu context, 
        # the main menu is a logical grouping of the sub-menus events,
        # so the sub-menu events should be the events listened for.
        self.menu_def = [['New', ['Create Student', 'Create Section', 'Exit'  ]],
                    ['File',['Save', 'Load', 'delete student']],      
                        ['graphs', ['scatter plot', self.placeHolder, self.placeHolder, ]],      
                        ['Help', 'About...'], ]
        # this list is used to create the table layout for the student names   
        self.class_list_column = [
            [sg.Submit(key="-class avg-",
                        button_text=self.class_Av_button),
            sg.Text(initAvgArr[0], 
                        key="avg")],
            [sg.Submit(key="-test avg-",
                        button_text=self.test_Av_button), 
            sg.Text(initAvgArr[1], 
                        key="avg test")],
            
            [sg.Text("---student grades----"),],
            
            [
                sg.Listbox(values=initAvgArr[2], 
                        enable_events=True, 
                        size=(60, 30), 
                        key="-grade list-")
            ],
        ]
        # this list is used to create the table layout for the student grades
        self.grade_viewer_column = [
        
            [sg.Submit(key="-show-",
                        button_text=self.clear_button),
                        sg.Text(initAvgArr[3], 
                        key='-sect view-')],
            
            [sg.Submit(key="-work avg-",
                        button_text=self.class_work_avg),
            sg.Text(initAvgArr[4][0:5], 
                        key="class work avg")],
            
            [sg.Text("Choose a student from list on left:", 
                        key="-student name-", 
                        size=(24, 1))],
            
            [sg.Listbox(size=(60, 30),values=["Choose a student"], 
                        enable_events=True, 
                        key="-chose student-")],    
        ]
        # version info on screen bottom
        self.bottom_row = [sg.Text(size=(60,1)), sg.Text(size=(45,1)),sg.Text(self.verNum)]
        
    def get_window_elements(self):
        layout= [
                    [sg.Menu(self.menu_def, )],
                    [   sg.Column(self.class_list_column),
                        sg.VSeperator(),
                        sg.Column(self.grade_viewer_column)],
                    self.bottom_row,   
                ]
        return layout, self.progNam
    
    def get_about_txt(self):
        return self.aboutMsg