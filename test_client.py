import math

import rospy
from hsr_agent.agent import Agent
from utils.axis_transform import Axis_transform
from utils.depth_to_pc import Depth2PC
import numpy as np
import cv2
import time

if __name__ == '__main__':
    rospy.init_node('test_client_hsr')
    axis_transform = Axis_transform()
    agent = Agent()
    while True:
        command = input('task : ')
        # move_abs
        if command == 'start_1':
            agent.move_abs('start_1')
        elif command == 'zero':
            agent.move_abs('zero')
        elif command == 'dev_front':
            agent.move_abs('dev_front')
        elif command == 'table_front':
            agent.move_abs('table_front')
        elif command == "seat_scan":
            agent.move_abs_safe('seat_scan')
        elif command == 'table_side':
            agent.move_abs('table_side')
        elif command == 'shelf_front':
            agent.move_abs('shelf_front')
        elif command == 'shelf_front':
            agent.move_abs('shelf_front')
        elif command == 'bin' :
            agent.move_abs('bin')
        elif command == 'sofa_view':
            agent.move_abs('sofa_view')
        elif command == 'door_handle':
            agent.move_abs('door_handle')
        elif command == 'door_bypass':
            agent.move_abs('door_bypass')
        elif command == 'cloth_scan':
            agent.move_abs_safe('cloth_scan')
        elif command == 'dishwasher':
            agent.move_abs('dishwasher')
        elif command == 'breakfast_test':
            agent.move_abs_safe('breakfast_table')
        elif command == 'table_front_test':
            agent.move_abs_safe('table_front')
        elif command == 'table_side_test':
            agent.move_abs_safe('table_side')
        elif command == 'breakfast_table':
            agent.move_abs('breakfast_table')
        # robot pose
        elif command == 'move_pose':
            agent.pose.move_pose()
        elif command == 'neutral_pose':
            agent.pose.neutral_pose()
        elif command == 'pick_side_pose':
            agent.pose.pick_side_pose(table='kitchen_table')
        elif command == 'pick_top_pose':
            agent.pose.pick_top_pose(table='breakfast_table')
        elif command == 'arm_lift_up':
            length = input("Give the arm_lift_up in length(0 ~ 0.69) : ")
            agent.pose.arm_lift_up(float(length))
        elif command == 'head_tilt':
            angle = input("Give the head tilt angle in degrees(-90 ~ 30) : ")
            agent.pose.head_tilt(angle)
        elif command == 'wrist_roll':
            angle = input("Give the wrist roll angle in degrees(-110 ~ 210) : ")
            agent.pose.wrist_roll(angle)
        elif command == 'head_pan':
            angle = input("Give the head pan angle in degrees(-90 ~ 30) : ")
            agent.pose.head_pan(angle)
        elif command == 'wrist_flex':
            angle = input("Give the wrist flex angle in degrees : ")
            agent.pose.wrist_flex(angle)
        elif command == 'arm_flex':
            angle = input("Give the arm flex angle in degrees : ")
            agent.pose.arm_flex(angle)
        elif command == 'arm_roll':
            angle = input("Give the arm roll angle in degrees : ")
            agent.pose.arm_roll(angle)
        # extra function
        elif command == 'distancing':
            from utils.distancing import distancing, distancing_horizontal
            print(distancing(agent.yolo_module.pc, 'kitchen_table'))
        elif command == 'q' or command == 'quit':
            break
        elif command == 'tts':
            sentence = input('sentence : ')
            agent.say(sentence)
        elif command == 'stt':
            result = agent.stt(5.)
            rospy.loginfo(f'STT Result: {result}')
        elif command == 'l': # open gripper
            agent.open_gripper()
        elif command == 'p': # pick
            agent.grasp()
        elif command == 'weak': # pick
            agent.grasp(weak=True)
        elif command == 'w':
            agent.move_rel(.3, 0, wait=True)
        elif command == 's':
            agent.move_rel(-0.3, 0)
        elif command == 'a':
            agent.move_rel(0, 0.3)
        elif command == 'd':
            agent.move_rel(0, -0.3)
        elif command == 'z':
            agent.move_rel(0, 0, yaw=1.57)
        elif command == 'c':
            agent.move_rel(0, 0, yaw=-1.57)
        elif command == 'head_show_text':
            show_text = input('head_show_text : ')
            agent.head_show_text(show_text=show_text)
        elif command == 'getp':
            agent.get_pose()
        elif command == 'detect_3d_unseen':
            agent.yolo_module.detect_3d_unseen('desk')[0]

        else:
            print('invalid command')

# shoe_scan [1.4227, 1.1802, -1.5106]
# door pose [-2.439925046798405, 3.741186220829006, 1.6161519211842417]
# pick pose  [0.3110857689895185, -0.009397325880122043, 0.016862118362033503]

