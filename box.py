class Box:
   def __init__(self, length, width, height, thickness):
      self.length = length
      self.width = width
      self.height = height
      self.thickness = thickness

      self.slotlength = 0.75
      self.margin = self.thickness*2
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

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness, 
                self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.thickness)

      # Tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY)

      # Second Spacer
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness, 
                self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                self.originY + self.thickness)

      # First vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY,
                self.originX + self.tab_space_length() + self.margin + self.thickness,
                self.originY + self.thickness)

      # second vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness)

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness + self.height, 
                self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.thickness + self.height)

      # Tab
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.height + 2*self.thickness,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.height + 2*self.thickness)

      # Second Spacer
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height, 
                self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height)

      # First vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness, 
                self.originY + self.height + self.thickness,
                self.originX + self.tab_space_length() + self.margin + self.thickness,
                self.originY + self.thickness + self.height + self.thickness)

      # second vertical line
      self.draw_line(self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.height + self.thickness,
                self.originX + self.tab_space_length() + self.margin + self.thickness + self.tab_length(),
                self.originY + self.thickness + self.height + self.thickness)

      self.draw_line(self.originX, 
                     self.originY + self.thickness,
                     self.originX,
                     self.originY + self.thickness + self.height)

      self.draw_line(self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                     self.originY + self.thickness,
                     self.originX + 2*self.tab_space_length() + 2*self.margin + 2*self.thickness + self.tab_length(),
                     self.originY + self.thickness + self.height)

      self.draw_rect(self.originX + self.margin, self.originY + self.thickness + ((1-self.slotlength)/2) * self.height, 
                     self.thickness, self.slotlength * self.height)

      self.draw_rect(self.originX + self.margin + self.width + self.thickness, self.originY + self.thickness + ((1-self.slotlength)/2) * self.height, 
                     self.thickness, self.slotlength * self.height)

   def sides(self):


      tab_space_length = self.height * ((1 - self.slotlength)/2)
      tab_length = self.height * self.slotlength

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness, 
                self.originX + tab_space_length, 
                self.originY + self.thickness)

      # Tab
      self.draw_line(self.originX + tab_space_length, 
                self.originY,
                self.originX + tab_space_length + tab_length,
                self.originY)

      # Second Spacer
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.thickness, 
                self.originX + 2*tab_space_length + tab_length,
                self.originY + self.thickness)

      # First vertical line
      self.draw_line(self.originX + tab_space_length, 
                self.originY,
                self.originX + tab_space_length,
                self.originY + self.thickness)

      # second vertical line
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY,
                self.originX + tab_space_length + tab_length,
                self.originY + self.thickness)

      # First spacer
      self.draw_line(self.originX,
                self.originY + self.thickness + self.length, 
                self.originX + tab_space_length, 
                self.originY + self.thickness + self.length)

      # Tab
      self.draw_line(self.originX + tab_space_length, 
                self.originY + self.length + 2*self.thickness,
                self.originX + tab_space_length + tab_length,
                self.originY + self.length + 2*self.thickness)

      # Second Spacer
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.thickness + self.length, 
                self.originX + 2*tab_space_length + tab_length,
                self.originY + self.thickness + self.length)

      # First vertical line
      self.draw_line(self.originX + tab_space_length, 
                self.originY + self.length + self.thickness,
                self.originX + tab_space_length,
                self.originY + self.thickness + self.length + self.thickness)

      # second vertical line
      self.draw_line(self.originX + tab_space_length + tab_length,
                self.originY + self.length + self.thickness,
                self.originX + tab_space_length + tab_length,
                self.originY + self.thickness + self.length + self.thickness)

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
      self.draw_rect(self.originX, self.originY, self.width + 2*self.thickness + 2*self.margin, self.length + 2*self.thickness + 2*self.margin); 
      self.draw_rect(self.originX + self.thickness + self.margin + (self.width * (1 - self.slotlength))/2, self.originY + self.margin, self.width * self.slotlength, self.thickness);
      self.draw_rect(self.originX + self.thickness + self.margin + (self.width * (1 - self.slotlength))/2, self.originY + self.margin + self.thickness + self.length, self.width * self.slotlength, self.thickness);


if __name__ == '__main__':


   print '<?xml version="1.0" encoding="utf-8" ?>'
   print '<svg baseProfile="full" self.height="100%" version="1.1" self.width="100%" '
   print 'xmlns="http://www.w3.org/2000/svg" '
   print 'xmlns:ev="http://www.w3.org/2001/xml-events" '
   print 'xmlns:xlink="http://www.w3.org/1999/xlink">'
   print '<defs />'

# length, width, height, thickness
   myBox = Box(50, 100, 25, 3)

   #myBox.front_back_tab();
   #myBox.top_bottom();
   myBox.sides();

   print '</svg>';

