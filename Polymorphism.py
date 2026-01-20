width = int(input('กว้าง'))
hight = int(input('ยาว'))

def area (width, hight):
    reg = width * hight
    cir = (1/2) * width * hight
    return (reg, cir)

area_reg, area_tri = area(width, hight)
print(f"พื้นที่สี่เหลี่ยม: {reg}")
print(f"พื้นที่วงกลม: {cir}")