from PIL import Image
import random
im = Image.open("cat.jpg") #Can be many different formats.
picture = im.load()
width, height = im.size


def get_list_of_pixels_by_row(im,width,height):
    pixellist= []
    for y in range(height -1):
        row = []
        for x in range(width -1):
            r,g,b = im.getpixel((x,y))
            name = get_random_name()
            row.append((name, (r,g,b)))
        pixellist.append(row)
    return pixellist



def get_random_name():
    random_name=""
    for i in range(8):
        new_let=random.choice('abcdefghijklmnopqrstyvwxyz')
        random_name += new_let
    return random_name

def template_areas(pixels_by_row,width,height):
    template_areas=""
    for y in range(height-1):
        new_row = []
        for x in range(width-1):
            name, rgb = pixels_by_row[y][x]
            new_row.append(name)
        newer_row = " ".join(new_row)
        template_areas += '"{}"\n'.format(newer_row)
    template_areas += ';'
    return template_areas

def html_classes(pixels_by_row,width,height):
    classes=""
    for y in range(height-1):
        new_row = []
        for x in range(width-1):
            name, rgb = pixels_by_row[y][x]
            classes += '<div class="{}"><p>.</p></div>'.format(name)
    return classes

def css(pixels_by_row,width,height):
    css=""
    for y in range(height-1):
        new_row = []
        for x in range(width-1):
            name, rgb = pixels_by_row[y][x]
            css += '.{} {{grid-area: {}; background: rgb{};}}'.format(name,name,rgb)
    return css

pixels_by_row= get_list_of_pixels_by_row(im,width,height)


f = open('pixel_grid.html','w')




f.write("<!DOCTYPE html><html><head><style>")
f.write("p {color: rgba(255, 0, 0, 0.0); font-size: 4px;} ")
f.write("main {")
f.write(
"display:grid; \n grid-template-areas: \n {} \n justify-items: stretch; \n align-items:stretch; \n".format(template_areas(pixels_by_row,width,height)))
f.write("}")
f.write(css(pixels_by_row,width,height))
f.write("</style></head><body>"
)

f.write('<main class="grid_container">')
f.write(html_classes(pixels_by_row,width,height))
f.write('</main>')
f.write("</body></html>")



f.close()

