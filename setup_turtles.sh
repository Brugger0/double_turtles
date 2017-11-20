echo 'reseting turtlesim'
rosservice call /reset

echo 'killing default turtle'
rosservice call /kill turtle1

echo 'spawning left turtle'
rosservice call /spawn 4 5 0 turtle_left

echo 'spawning right turtle'
rosservice call /spawn 4 4 0 turtle_right
