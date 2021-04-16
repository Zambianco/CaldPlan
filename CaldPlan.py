from dxfwrite import DXFEngine as dxf
import math



def pol2cart(r, phi):
    """Converte coordenadas polares em cartesianas
    r = raio, phi = ângulo"""
    x = r * math.cos(math.radians(phi))
    y = r * math.sin(math.radians(phi))
    return(x, y)

def ChapeuChines(h, r):
    """
    Pede:
        h = altura;
        d = diametro externo inferior;
    Retorna:
        R = Raio externo superior;
        a = Ângulo da abertura;
        C = Corda da abertura.
    """
    r = float(r)
    R = math.sqrt((h**2 + r**2))
    a = 360 - (((180 * r) / R) * 2)
    C = math.sin(math.radians(47/2)) * (R * 2)

    drawing = dxf.drawing('chapeuchines.dxf')
    arc = dxf.arc(r, (0.0, 0.0), 0, 360 - a) #Parâmetros do arco
    line1 = dxf.line((0.0, 0.0), (70.0, 0.0))#Parâmentros para a linha 1
    x2, y2 = pol2cart(70, 360 - a)
    line2 = dxf.line((0.0, 0.0), (x2, y2)) #Parâmetros da linha 2
    drawing.add(arc) #desenho do arco
    drawing.add(line1) #desenho da linha 1
    drawing.add(line2) #desenho da linha 2
    
    drawing.save() #Salvamento do desenho

    return R, a, C



    
    
