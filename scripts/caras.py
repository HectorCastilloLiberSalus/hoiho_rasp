#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import pyglet
import sys
reload(sys)


def callback(data):
	sys.setdefaultencoding('Cp1252')
        print("recibida")
	if (data == 1):
		ag_file = "Alegre1.gif"
	        print("recibida")
        else: 
		ag_file = "Alegre1.gif"
                print("recibida")
	animation = pyglet.resource.animation(ag_file)
	print("bien")
	sprite = pyglet.sprite.Sprite(animation)

	# create a window and set it to the image size
	##screen = display.get_screens()
	win = pyglet.window.Window(fullscreen=True)
	# set window background color = r, g, b, alpha
	# each value goes from 0.0 to 1.0
	green = 1, 1, 1, 1
	pyglet.gl.glClearColor(*green)
	@win.event
	def on_draw():
		win.clear()
		sprite.draw()
        pyglet.app.run()
def caras():


    rospy.init_node('caras', anonymous=True)

    rospy.Subscriber('/expresion', Int16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    caras()
