#fatyellowrectangle = Rectangle(20, 5 , 'yellow')
#fatyellowrectangle.height = 5 
#fatyellowrectangle.width = 20
#fatyellowrectangle.color = 'yellow'
#
#fatyellowrectangle.drawRectangle#

#C1 = Circle(4, "yellow")
#
#class Circle (Object):
#    def__init__(self,radius,color):
#        self.radius = 4;
#        self.color = yellow;


class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points(1,2)
p1.print_point()
