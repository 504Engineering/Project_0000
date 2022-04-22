import PySimpleGUI as sg
import yaml
import numpy as np
import os, sys
import cv2

class GUI:
    def __init__(self):
        sg.theme('DarkAmber')

        # window dimensions
        window_dimensions = (1280, 720)
        self.start = 0
        self.wl = \
[   
    [ 
        sg.Column(
        [
            [ 
                sg.Button('Start', key='-START-') 
            ]  
        ], expand_x=True, element_justification='left', vertical_alignment='center'),
        sg.Column(
        [  
            [ 
                sg.Text("504 Engineering Control Apparatus", font=('Helvetica', 11, 'bold'), auto_size_text=True, justification='right') 
            ] 
        ], expand_x=True, element_justification='right', vertical_alignment='center')  
    ],
    [
        [
            sg.Column (
                [
                    [
                        sg.Text('Controllers Configuration', font=('Helvetica', 14, 'bold'))
                    ],
                    [
                        sg.Text("   "),
                        sg.Text("Button Mappings:", font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('Activate Stepper Group 1: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Activate Stepper Group 2: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Activate Stepper Group 3: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Reset Positioning: ', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-ASG1-')
                                ],
                                [
                                    sg.Text('0', key='-ASG2-')
                                ],
                                [
                                    sg.Text('0', key='-ASG3-')
                                ],
                                [
                                    sg.Text('0', key='-RS1-')
                                ],
                            ], element_justification='left', vertical_alignment='center'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            ),
            sg.Column (
                [
                    [
                        sg.Text('   ', font=('Helvetica', 14, 'bold'))
                    ],
                    [
                        sg.Text("   "),
                        sg.Text("Inverted Controls:", font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('X_Flip: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Y_Flip: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Z_Flip: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('S_Flip: ', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-ICV1-')
                                ],
                                [
                                    sg.Text('0', key='-ICV2-')
                                ],
                                [
                                    sg.Text('0', key='-ICV3-')
                                ],
                                [
                                    sg.Text('0', key='-ICV4-')
                                ],
                            ], element_justification='left', vertical_alignment='center'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            ),
            sg.Column (
                [
                    [
                        sg.Image(filename='', key='webcam1')
                    ]
                ], element_justification='right', vertical_alignment='center', size=(640, 480)
            )
        ]
    ],
    [
        [
            sg.Column (
                [
                    [
                        sg.Text('   '),
                        sg.Text(' Axis Mappings:', font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('JoyX: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('JoyY: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('JoyZ: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('JoyS: ', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-AMX-')
                                ],
                                [
                                    sg.Text('0', key='-AMY-')
                                ],
                                [
                                    sg.Text('0', key='-AMZ-')
                                ],
                                [
                                    sg.Text('0', key='-AMS-')
                                ],
                            ], element_justification='left', vertical_alignment='center'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            ),
            sg.Column (
                [
                    [
                        sg.Text('   '),
                        sg.Text('DeadZones:', font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('X_Deadzone: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Y_Deadzone: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Z_Deadzone: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('S_Deadzone: ', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-DZX-')
                                ],
                                [
                                    sg.Text('0', key='-DZY-')
                                ],
                                [
                                    sg.Text('0', key='-DZZ-')
                                ],
                                [
                                    sg.Text('0', key='-DZS-')
                                ],
                            ], element_justification='left', vertical_alignment='center'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            )
        ]
    ],
    [
        [
            sg.Column (
                [
                    [
                        sg.Text('   '),
                        sg.Text(' Autonomous Controls:', font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('Record: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Stop Recording: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Playback: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Save: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Autonomous Trigger 1:', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Autonomous Trigger 2:', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Autonomous Trigger 3:', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Autonomous Trigger 4:', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-AUR-')
                                ],
                                [
                                    sg.Text('0', key='-AUSR-')
                                ],
                                [
                                    sg.Text('0', key='-AUP-')
                                ],
                                [
                                    sg.Text('0', key='-AUS-')
                                ],
                                [
                                    sg.Text('0', key='-AU1-')
                                ],
                                [
                                    sg.Text('0', key='-AU2-')
                                ],
                                [
                                    sg.Text('0', key='-AU3-')
                                ],
                                [
                                    sg.Text('0', key='-AU4-')
                                ]
                            ], element_justification='left', vertical_alignment='upper'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            ),
            sg.Column (
                [
                    [
                        sg.Text('   '),
                        sg.Text('Camera Config:', font=('Helvetica', 12))
                    ],
                    [
                        sg.Column (
                            [
                                [
                                    sg.Text('       '),
                                    sg.Text('Camera Resolution: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Camera FPS: ', font=('Helvetica', 10))
                                ],
                                [
                                    sg.Text('       '),
                                    sg.Text('Number of Cameras: ', font=('Helvetica', 10))
                                ]
                            ]
                        ),
                        sg.Column (
                            [
                                [
                                    sg.Text('0', key='-CSWH-')
                                ],
                                [
                                    sg.Text('0', key='-CFPS-')
                                ],
                                [
                                    sg.Text('0', key='-C#C-')
                                ]
                            ], element_justification='left', vertical_alignment='center'
                        )
                    ]
                ], element_justification='left', vertical_alignment='center', size=(280, 180)
            )
        ]
    ],
    [
        
    ]
]
        
        self.window = sg.Window("Main", self.wl, size=window_dimensions)

    def controllers_config(self):
        with open("config/controllers.yml", "r") as confile:
            self.controllers_config_file = yaml.load(confile, Loader=yaml.SafeLoader)

        self.window['-ASG1-'].update(self.controllers_config_file['Button_Mappings'].get('Activate_Stepper_Group_1'))
        self.window['-ASG2-'].update(self.controllers_config_file['Button_Mappings'].get('Activate_Stepper_Group_2'))
        self.window['-ASG3-'].update(self.controllers_config_file['Button_Mappings'].get('Activate_Stepper_Group_3'))
        self.window['-RS1-'].update(self.controllers_config_file['Button_Mappings'].get('Reset_Positioning'))
        self.window['-AMX-'].update(self.controllers_config_file['Axis_Mappings'].get('JoyX'))
        self.window['-AMY-'].update(self.controllers_config_file['Axis_Mappings'].get('JoyY'))
        self.window['-AMZ-'].update(self.controllers_config_file['Axis_Mappings'].get('JoyZ'))
        self.window['-AMS-'].update(self.controllers_config_file['Axis_Mappings'].get('JoyS'))
        self.window['-ICV1-'].update(self.controllers_config_file['Inverted_Controls'].get('X_Flip'))
        self.window['-ICV2-'].update(self.controllers_config_file['Inverted_Controls'].get('Y_Flip'))
        self.window['-ICV3-'].update(self.controllers_config_file['Inverted_Controls'].get('Z_Flip'))
        self.window['-ICV4-'].update(self.controllers_config_file['Inverted_Controls'].get('S_Flip'))
        self.window['-DZX-'].update(self.controllers_config_file['DeadZones'].get('X_Deadzone'))
        self.window['-DZY-'].update(self.controllers_config_file['DeadZones'].get('Y_Deadzone'))
        self.window['-DZZ-'].update(self.controllers_config_file['DeadZones'].get('Z_Deadzone'))
        self.window['-DZS-'].update(self.controllers_config_file['DeadZones'].get('S_Deadzone'))
        self.window['-AUR-'].update(self.controllers_config_file['Autonomous_Controls'].get('Record'))
        self.window['-AUSR-'].update(self.controllers_config_file['Autonomous_Controls'].get('Stop_Recording'))
        self.window['-AUP-'].update(self.controllers_config_file['Autonomous_Controls'].get('Playback'))
        self.window['-AUS-'].update(self.controllers_config_file['Autonomous_Controls'].get('Save'))
        self.window['-AU1-'].update(self.controllers_config_file['Autonomous_Controls'].get('A1'))
        self.window['-AU2-'].update(self.controllers_config_file['Autonomous_Controls'].get('A2'))
        self.window['-AU3-'].update(self.controllers_config_file['Autonomous_Controls'].get('A3'))
        self.window['-AU4-'].update(self.controllers_config_file['Autonomous_Controls'].get('A4'))
        self.window['-CSWH-'].update(self.controllers_config_file['Camera_Config'].get('size'))
        self.window['-CFPS-'].update(self.controllers_config_file['Camera_Config'].get('fps'))
        self.window['-C#C-'].update(self.controllers_config_file['Camera_Config'].get('numofcams'))
        
    def autonomous_config(self):
        with open("config/autonomous.yml", "r") as confile:
            self.controllers_config_file = yaml.load(confile, Loader=yaml.SafeLoader)
        
        # for section in self.controllers_config_file:
        #     print(type(section))
        #     print(section)
        #     print(type(self.controllers_config_file[section]))
        #     print(self.controllers_config_file[section])

    def cam_read(self, cam):
        try:
            self.cap = cv2.VideoCapture(cam)
            ret, frame = self.cap.read()
            self.imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        except (RuntimeError, TypeError, NameError, cv2.error):
            print("image failing to load")
        self.window['webcam1'].update(data=self.imgbytes)

    def run(self):
        event, values = self.window.read(timeout=100)
        b = 0
        if self.start == 1:
            self.cam_read(0)
        if event == sg.WIN_CLOSED or event == 'Close':
            b = 1
            self.cap.release
        if event == '-START-':
            self.controllers_config()
            self.autonomous_config()
            self.start = 1
        return b

a = GUI()

while True:
    c = a.run()
    if c == 1:
        break