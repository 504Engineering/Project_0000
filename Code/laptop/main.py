# GUI library
from ast import arguments
import PySimpleGUI as sg
import queue
import threading

# Input data library
import pygame

# Serial library
import serial

# Camera library
import cv2

# Extra libraries
import numpy as np

# server connection library
import socket

# data variables send and recieve
s_data = [0, 0, 0, 0, 0, 0, 0]
r_data = np.zeros(8)

joy_a = np.zeros(4)
joy_b = np.zeros(12)
joy1_h = 0

sg.theme('DarkGrey14')

init_layout = [[    sg.Text('504 Engineering Control Apparatus')],
               [    sg.Text('Click connect to control via joystick'), sg.Button('Connect')],
               [    sg.Text('Click start to control manipulator via graphical interface'), sg.Button('Start')]]

ccol1 = [
    [sg.Frame('Stepper 1', [[sg.Text(key='-SS1-')]])],
    [sg.Frame('Recieve Stepper 1', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS1-')]])]
]

ccol2 = [
    [sg.Frame('Stepper 2', [[sg.Text(key='-SS2-')]])],
    [sg.Frame('Recieve Stepper 2', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS2-')]])]
]

ccol3 = [
    [sg.Frame('Stepper 3', [[sg.Text(key='-SS3-')]])],
    [sg.Frame('Recieve Stepper 3', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS3-')]])]
]

ccol4 = [
    [sg.Frame('Stepper 4', [[sg.Text(key='-SS4-')]])],
    [sg.Frame('Recieve Stepper 4', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS4-')]])]
]

ccol5 = [
    [sg.Frame('Stepper 5', [[sg.Text(key='-SS5-')]])],
    [sg.Frame('Recieve Stepper 5', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS5-')]])]
]

ccol6 = [
    [sg.Frame('Stepper 6', [[sg.Text(key='-SS6-')]])],
    [sg.Frame('Recieve Stepper 6', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS6-')]])]
]

ccol7 = [
    [sg.Frame('Stepper 7', [[sg.Text(key='-SS7-')]])],
    [sg.Frame('Recieve Stepper 7', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS7-')]])]
]

ncol1 = [[sg.Frame('Stepper 1', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S1-')]])],
        [sg.Frame('Recieve Stepper 1', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS1-')]])]]

ncol2 = [[sg.Frame('Stepper 2', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S2-')]])],
        [sg.Frame('Recieve Stepper 2', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS2-')]])]]

ncol3 = [[sg.Frame('Stepper 3', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S3-')]])],
        [sg.Frame('Recieve Stepper 3', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS3-')]])]]

ncol4 = [[sg.Frame('Stepper 4', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S4-')]])],
        [sg.Frame('Recieve Stepper 4', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS4-')]])]]

ncol5 = [[sg.Frame('Stepper 5', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S5-')]])],
        [sg.Frame('Recieve Stepper 5', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS5-')]])]]

ncol6 = [[sg.Frame('Stepper 6', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S6-')]])],
        [sg.Frame('Recieve Stepper 6', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS6-')]])]]

ncol7 = [[sg.Frame('Stepper 7', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-S7-')]])],
        [sg.Frame('Recieve Stepper 7', [[sg.Slider((-1.0, 1.0), default_value=0, resolution=0.1, orientation='vertical', key='-RS7-')]])]]

conn_layout = [
               [sg.Column(ccol1, element_justification='c' ), 
                sg.Column(ccol2, element_justification='c'), 
                sg.Column(ccol3, element_justification='c'), 
                sg.Column(ccol4, element_justification='c'),
                sg.Column(ccol5, element_justification='c'),
                sg.Column(ccol6, element_justification='c'),
                sg.Column(ccol7, element_justification='c')]
               ]

no_conn_layout = [
               [sg.Column(ncol1, element_justification='c' ), 
                sg.Column(ncol2, element_justification='c'), 
                sg.Column(ncol3, element_justification='c'), 
                sg.Column(ncol4, element_justification='c'),
                sg.Column(ncol5, element_justification='c'),
                sg.Column(ncol6, element_justification='c'),
                sg.Column(ncol7, element_justification='c')]
               ]
               
layout = [  [sg.Column(init_layout, key='-COL0-'), sg.Column(conn_layout, visible=False, key='-COL1-'), sg.Column(no_conn_layout, visible=False, key='-COL2-')] ]

window = sg.Window('Control Apparatus', layout)

layout = 0
connect = 0

qui_que = queue.Queue()

pygame.init()
pygame.joystick.init()

def read_data():
    joy_d = np.array(7)

    joy = pygame.joystick.Joystick(0)
    joy.init()

    joy_a = [0, 1, 2, 3]
    joy_b = []
    return

while True:
    event, values = window.read(timeout=100)
    # print(connect)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Connect':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
        connect = 1
    if event == 'Start':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
        connect = 0
    if connect == 1:
        
        print(values['-S1-'], "    ", values['-RS1-'], "    ", s_data)
        
window.close()