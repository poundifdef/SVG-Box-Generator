#import svgwrite
#from svgwrite import cm, mm   
    
#def basic_shapes(name):
#    dwg = svgwrite.Drawing(filename=name, debug=True)
#    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
#    for y in range(20):
#        hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
#    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
#    for x in range(17):
#        vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
#    shapes = dwg.add(dwg.g(id='shapes', fill='red'))
#
#    # set presentation attributes at object creation as SVG-Attributes
#    shapes.add(dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue',
#                          stroke_width=3))
#
#    # override the 'fill' attribute of the parent group 'shapes'
#    shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm),
#                        fill='blue', stroke='red', stroke_width=3))
#
#    # or set presentation attributes by helper functions of the Presentation-Mixin
#    ellipse = shapes.add(dwg.ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
#    ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])
#    dwg.save()

def draw_line(x1, y1, x2, y2):
   print '<line fill="none" stroke="rgb(0,0,255)" stroke-width="0.01mm" x1="%smm" x2="%smm" y1="%smm" y2="%smm" />' % (x1, y1, x2, y2)

def draw_rect(x, y, width, height):
   print '<rect fill="none" stroke="rgb(0,0,255)" stroke-width="0.01mm" x="%smm" y="%smm" width="%smm" height="%smm" />' % (x, y, width, height)


if __name__ == '__main__':

   originX = 10
   originY = 10

   thickness = 3
   width = 100
   length = 50
   height = 25

   print '<?xml version="1.0" encoding="utf-8" ?>'
   print '<svg baseProfile="full" height="100%" version="1.1" width="100%" '
   print 'xmlns="http://www.w3.org/2000/svg" '
   print 'xmlns:ev="http://www.w3.org/2001/xml-events" '
   print 'xmlns:xlink="http://www.w3.org/1999/xlink">'
   print '<defs />'

   slotLength = 0.75 

   draw_rect(originX, originY, width + 4*thickness, length + 4*thickness); 
   draw_rect(originX + 2*thickness + (width * (1 - slotLength))/2, originY + thickness, width * slotLength, thickness);
   draw_rect(originX + 2*thickness + (width * (1 - slotLength))/2, originY + length + 2*thickness, width * slotLength, thickness);

   print '</svg>';

#    basic_shapes('basic_shapes.svg')
   #dwg = svgwrite.Drawing('basic_shapes.svg')
   #dwg.add(dwg.line(start=(50*mm, 0), end=(50*mm, 50*mm), stroke=svgwrite.rgb(0, 0, 255, 'RGB'), fill='none', stroke_width=0.010*mm))
   #dwg.save()i;

