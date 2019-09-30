#!/usr/bin/env python

import rospy
import sys
import cv2
import numpy as np
from std_msgs.msg import Float64
from std_msgs.msg import String
from sensor_msgs.msg import Image
from dynamixel_msgs.msg import JointState
from cv_bridge import CvBridge, CvBridgeError
from math import pi

# Classe responsável por todas as variáveis, funções e métodos usados no movimento dos motores
class motor_movement():

    def __init__(self):

        # subscribers dos tópicos de feedback dos dynamixels
        self.dyna1_sub = rospy.Subscriber("/joint3_controller/state", JointState, self.dyna1_callback)
        self.dyna2_sub = rospy.Subscriber("/joint4_controller/state", JointState, self.dyna2_callback)

        # publishers que publicam nos tópicos de comando dos dynamixels
        self.pub_dyna1 = rospy.Publisher("/joint3_controller/command", Float64, queue_size=10)          # motor 1
        self.pub_dyna2 = rospy.Publisher("/joint4_controller/command", Float64, queue_size=10)         # motor 2

        # variáveis iniciais
        self.dyna1_position = 0
        self.dyna2_position = 0

    # callback do primeiro motor
    def dyna1_callback(self, msg):
        self.dyna1_position = msg.current_pos
    
    #callback do segundo motor
    def dyna2_callback(self, msg):
        self.dyna2_position = msg.current_pos

    # método para saber a posição atual do motor 1
    def get_dyna1_position(self):
        return self.dyna1_position

    # método para saber a posição atual do motor 2
    def get_dyna2_position(self):
        return self.dyna2_position
        
    # método responsável por especificar o que será pubicado em cada tópico
    def pub_movement(self, dyna1, dyna2):
        self.pub_dyna1.publish(dyna1)
        self.pub_dyna2.publish(dyna2)

    # método responsável pelas ppublicações dos comandos para os motores
    def movement(self):
        # Esse comando fará as rodas darem uma volta completa, o que por sua vez fará o robô andar um pouco para frente
        self.mm.pub_movement(2*pi,2*pi)

def main():

    # Inicia o nó do ROS de uma forma anônima pra evitar repetição do nome
    rospy.init_node("pan_tilt", anonymous=True)

    # Essa linha é responsável por iniciar a classe que controla os comandos de movimento do motor
    mm = motor_movement()

    # Essa linha da propriamente dito o comando pro robô andar
    mm.movement()

    rospy.spin()

if __name__ == "__main__":
    main()