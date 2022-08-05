#This function will be calculating the approximate number of paint
# cans required to paint a wall of a given width and height
def paint_calc(height,width,cover):
    num_cans = (height+width)/cover
    return f"the number of cans required is: {round(num_cans)}"
h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = int(input("Enter the coverage 1 can gives: "))
print(paint_calc(height=h, width=w, cover=coverage))

