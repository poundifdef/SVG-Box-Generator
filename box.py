class Box:
   def __init__(self, length, width, height, thickness):
      # Length, Width, and Height of the box
      self.length = length
      self.width = width
      self.height = height

      # Thickness of material we are cutting
      self.thickness = thickness

      # The box's interlocking parts span this percentage of the side's length
      self.slotlength = 0.75

      # The kerf of the laser. That is, how much material the laser burns away
      self.kerf = 0.20

      # How much margin between the interlocking slot and the edge of the panel
      self.margin = self.thickness

      # The "origin" from whence we draw onto the SVG canvas
      self.originX = 10
      self.originY = 10

   def draw_line(self, x1, y1, x2, y2):
      print '<line fill="none" stroke="rgb(0,0,255)" stroke-width="0.01mm" x1="%smm" y1="%smm" x2="%smm" y2="%smm" />' % (x1, y1, x2, y2)

   def draw_rect(self, x, y, width, height):
      print '<rect fill="none" stroke="rgb(0,0,255)" stroke-width="0.01mm" x="%smm" y="%smm" width="%smm" height="%smm" />' % (x, y, width, height)

   def tab_length(self):
      return self.width*self.slotlength

   def tab_space_length(self):
      return self.width * ((1 - self.slotlength)/2)

   def front_back_tab(self):

      ####################################
      #     ASCII ART OF THIS PANEL      #
      #          ____      ____          #
      #  _______|    |____|    |_______  #
      # |   _                      _   | #
      # |  | |                    | |  | #
      # |  | |                    | |  | #
      # |  |_|                    |_|  | #
      # |_______      ____      _______| #
      #         |____|    |____|         #
      #                                  #
      ####################################

      ## Top tabs
      # Space before left tab 
      self.draw_line(self.originX,
                self.originY + self.thickness, 
                self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.thickness)

      # First vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY,
                self.originX + self.tab_space_length() + self.margin + self.thickness,
                self.originY + self.thickness)

      # Top left tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                     self.originY,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY)

      # Second vertical line
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.thickness)

      # Space between tabs
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.thickness, 
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.thickness)

      # Third vertical line
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY,
                    self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.thickness)

      # Top right tab
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length() ,
                     self.originY)

      # fourth vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness)

      # Space after right tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness, 
                self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                self.originY + self.thickness)



      ## Bottom tab
      # Space before left tab 
      self.draw_line(self.originX,
                self.originY + self.thickness + self.height, 
                self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.thickness + self.height)

      # First vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.height + self.thickness,
                self.originX + self.tab_space_length() + self.margin + self.thickness,
                self.originY + self.thickness + self.height + self.thickness)

      # Top left tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                     self.originY + self.height + 2*self.thickness,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.height + 2*self.thickness)

      # Second vertical line
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.height + self.thickness,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.thickness + self.height + self.thickness)

      # Space between tabs
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length()/4,
                     self.originY + self.thickness + self.height, 
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.thickness + self.height)

      # Third vertical line
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.height + self.thickness,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.thickness + self.height + self.thickness)

      # Top right tab
      self.draw_line(
                     self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.height + 2*self.thickness,
                     self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length() ,
                     self.originY + self.height + 2*self.thickness)

      # fourth vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.height + self.thickness,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height + self.thickness)

      # Space after right tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height, 
                self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height)


      # Left edge of piece
      self.draw_line(self.originX, 
                     self.originY + self.thickness,
                     self.originX,
                     self.originY + self.thickness + self.height)

      # Right edge of piece
      self.draw_line(self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                     self.originY + self.thickness,
                     self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                     self.originY + self.thickness + self.height)


      ## Slots for tabs
      #  Left tab slot
      self.draw_rect(self.originX + self.margin,
                     self.originY + self.thickness + ((1-self.slotlength)/2) * self.height, 
                     self.thickness,
                     self.slotlength * self.height/4)

      self.draw_rect(self.originX + self.margin,
                     self.originY + self.thickness + ((1-self.slotlength)/2) * self.height +
                        self.slotlength * self.height - self.slotlength * self.height/4, 
                     self.thickness,
                     self.slotlength * self.height/4)

     # Right tab slot
      self.draw_rect(self.originX + self.margin + self.width + self.thickness,
                     self.originY + self.thickness + ((1-self.slotlength)/2) * self.height, 
                     self.thickness,
                     self.slotlength * self.height/4)

      self.draw_rect(self.originX + self.margin + self.width + self.thickness,
                     self.originY + self.thickness + ((1-self.slotlength)/2) * self.height +
                        self.slotlength * self.height - self.slotlength * self.height/4, 
                     self.thickness,
                     self.slotlength * self.height/4)


   def sides(self):


      tab_space_length = self.height * ((1 - self.slotlength)/2)
      tab_length = self.height * self.slotlength

      ## Top

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness, 
                self.originX + tab_space_length, 
                self.originY + self.thickness)

      # First vertical line
      self.draw_line(self.originX + tab_space_length, 
                self.originY,
                self.originX + tab_space_length,
                self.originY + self.thickness)

      # First Tab
      self.draw_line(self.originX + tab_space_length, 
                     self.originY,
                     self.originX + tab_space_length + self.slotlength * self.height/4,
                     self.originY)

      # Second vertical line
      self.draw_line(self.originX + tab_space_length + self.slotlength * self.height/4, 
                self.originY,
                self.originX + tab_space_length + self.slotlength * self.height/4,
                self.originY + self.thickness)

      # Second spacer
      self.draw_line(self.originX + tab_space_length + self.slotlength * self.height/4,
                self.originY + self.thickness, 
                self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY + self.thickness)

      # Third vertical line

      self.draw_line(self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY,
                self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY + self.thickness)

      # Second tab
      self.draw_line(#self.originX  + ((1-self.slotlength)/2) * self.height +
                     #   self.slotlength * self.height - self.slotlength * self.height/4, 
                     self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                     self.originY,
                     self.originX + tab_space_length + tab_length,
                     self.originY)


      # fourth vertical line
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY,
                self.originX + tab_space_length + tab_length,
                self.originY + self.thickness)

      # third Spacer
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.thickness, 
                self.originX + 2*tab_space_length + tab_length,
                self.originY + self.thickness)





      ## Bottom

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness + self.length, 
                self.originX + tab_space_length, 
                self.originY + self.thickness + self.length)

      # First vertical line
      self.draw_line(self.originX + tab_space_length, 
                self.originY + self.length + self.thickness,
                self.originX + tab_space_length,
                self.originY + self.length + self.thickness + self.thickness)

      # First Tab
      self.draw_line(self.originX + tab_space_length, 
                     self.originY + self.length + 2*self.thickness,
                     self.originX + tab_space_length + self.slotlength * self.height/4,
                     self.originY + self.length + 2*self.thickness)

      # Second vertical line
      self.draw_line(self.originX + tab_space_length + self.slotlength * self.height/4, 
                self.originY + self.length + self.thickness,
                self.originX + tab_space_length + self.slotlength * self.height/4,
                self.originY + self.length + self.thickness + self.thickness)

      # Second spacer
      self.draw_line(self.originX + tab_space_length + self.slotlength * self.height/4,
                self.originY + self.thickness + self.length, 
                self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY + self.thickness + self.length)

      # Third vertical line

      self.draw_line(self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY + self.length + self.thickness,
                self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                self.originY + self.length + self.thickness + self.thickness)

      # Second tab
      self.draw_line(#self.originX  + ((1-self.slotlength)/2) * self.height +
                     #   self.slotlength * self.height - self.slotlength * self.height/4, 
                     self.originX + (self.height/2) + (self.height*self.slotlength)/4,
                     self.originY + self.length + 2*self.thickness,
                     self.originX + tab_space_length + tab_length,
                     self.originY + self.length + 2*self.thickness)


      # fourth vertical line
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.length + self.thickness,
                self.originX + tab_space_length + tab_length,
                self.originY + self.length + self.thickness + self.thickness)

      # third Spacer
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.thickness + self.length, 
                self.originX + 2*tab_space_length + tab_length,
                self.originY + self.thickness + self.length)


      ## Sides
      self.draw_line(self.originX, 
                     self.originY + self.thickness, 
                     self.originX,
                     self.originY + self.thickness + self.length)

      self.draw_line(self.originX + 2*tab_space_length + tab_length,
                     self.originY + self.thickness,
                     self.originX + 2*tab_space_length + tab_length,
                     self.originY + self.thickness + self.length)

   def top_bottom(self):
      # Top/Bottom #

      # Outer border
      self.draw_rect(self.originX,
                     self.originY,
                     self.width + 2*self.thickness + 2*self.margin,
                     self.length + 2*self.thickness + 2*self.margin); 

      # Top slots
      self.draw_rect(self.originX + self.thickness + self.margin + (self.width * (1 - self.slotlength))/2,
                     self.originY + self.margin,
                     self.tab_length()/4, 
                     self.thickness);


      self.draw_rect(self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.margin,
                     self.tab_length()/4, 
                     self.thickness);

      # Bottom slots
      self.draw_rect(self.originX + self.thickness + self.margin + (self.width * (1 - self.slotlength))/2,
                     self.originY + self.margin + self.thickness + self.length,
                     self.tab_length()/4, 
                     self.thickness);


      self.draw_rect(self.originX + self.tab_space_length() + self.margin + self.thickness + 3*self.tab_length()/4,
                     self.originY + self.margin + self.thickness + self.length,
                     self.tab_length()/4, 
                     self.thickness);

   def print_all_faces(self):
      print '<?xml version="1.0" encoding="utf-8" ?>'
      print '<svg baseProfile="full" version="1.1"'
      print ' width="%dmm" height="%dmm">' % (self.width+2*self.thickness+2*self.margin+2*self.originX, self.length+self.width+self.height+6*self.thickness+2*self.margin+2*self.originY + 40)
      print 'xmlns="http://www.w3.org/2000/svg" '
      print 'xmlns:ev="http://www.w3.org/2001/xml-events" '
      print 'xmlns:xlink="http://www.w3.org/1999/xlink">'
      print '<defs />'

      self.front_back_tab();
      self.originY += self.height + 20
      self.top_bottom();
      self.originY += self.length + 20
      self.sides();

      print '</svg>';

if __name__ == '__main__':

   # length, width, height, thickness (units are millimeters)
   myBox = Box(40, 30, 20, 3)
   myBox.print_all_faces()


