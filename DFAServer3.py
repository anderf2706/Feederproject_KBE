from PathPlanner import PathPlanner
import math

def run():

    # Stores the path to DFAServer working directory
    pathToApp = "C:\\Users\\Anders Fredriksen\\Desktop\\Schuul\\Auto2\\flask_project3\\"

    # Read the templates content of the template file
    f1 = open(pathToApp + "templates_DFA\\Curved_Rail_general.dfa", "r")
    dataGeneral = f1.read()
    print("data from template GENERAL:", dataGeneral)

    f2 = open(pathToApp + "templates_DFA\\Curved_Rail_line.dfa", "r")
    dataLine = f2.read()
    print("data from template LINE:", dataLine)

    f3 = open(pathToApp + "templates_DFA\\Curved_Rail_curve.dfa", "r")
    dataCurve = f3.read()
    print("data from template CURVE:", dataCurve)

    f4 = open(pathToApp + "templates_DFA\\Rail_beam.dfa", "r")
    dataBeam = f4.read()
    print("data from template BEAM:", dataBeam)

    x = 0
    y = 0
    z = 0

    # Intializing the points
    pointA = (0, 0)
    pointB = (0, 1000)
    pointC = (1500, 4000)
    # pointD = (10000, 10000)
    pointD = (3500, -4000)
    pointE = (10000, 6000)
    pointF = (-1000, 5900)
    pointG = (-2000, -2000)
    pointH = (-7000, -1000)
    pointI = (0, 8500)
    pointJ = (11000, 9500)
    pointK = (11500, -6000)
    pointL = (2000, -7500)
    pointM = (0, -500)
    dataPoints = [pointA,
                  pointB, pointC, pointD, pointE, pointF, pointG, pointH, pointI, pointJ, pointK, pointL, pointM]

    # Intializing the obstacles.
    obstacle1 = (-1, 500, 100, 100, -70)
    obstacles = [obstacle1]

    pathPlanner = PathPlanner(2000)
    path = pathPlanner.getPath(dataPoints)

    # Now update the templates and generate the final result.
    data = dataGeneral.replace("<GLOBAL_X>", str(x))  # data was initialized from dataGeneral...
    data = data.replace("<GLOBAL_Y>", str(y))
    data = data.replace("<GLOBAL_Z>", str(z))

    # Insert path elements
    pathElementsVarsTMP = ""  # placeholder for path element vars

    i = 0  # index of the path element
    pathElements = ""
    for p in path:
        i += 1
        if len(p) == 2:
            # Make the line - line_rail_path_N
            pathElements = pathElements + dataLine.replace("<ID>", str(i))
            pathElements = pathElements.replace("<START_X>", str(p[0][0]))
            pathElements = pathElements.replace("<START_Y>", str(p[0][1]))
            pathElements = pathElements.replace("<START_Z>", str(z))
            pathElements = pathElements.replace("<END_X>", str(p[1][0]))
            pathElements = pathElements.replace("<END_Y>", str(p[1][1]))
            pathElements = pathElements.replace("<END_Z>", str(z))
            if i == 1:
                pathElementsVarsTMP = "line_rail_path_1:,"
            else:
                pathElementsVarsTMP += "line_rail_path_" + str(i) + ":,"

        else:
            # Make the curve - curve_rail_path_N
            pathElements = pathElements + dataCurve.replace("<ID>", str(i))
            pathElements = pathElements.replace("<CURVE_RADIUS>", str(2000))
            pathElements = pathElements.replace("<START_ANG>", str(p[0] / math.pi * 180))
            pathElements = pathElements.replace("<END_ANG>", str(p[1] / math.pi * 180))
            pathElements = pathElements.replace("<CENTER_X>", str(p[2][0]))
            pathElements = pathElements.replace("<CENTER_Y>", str(p[2][1]))
            pathElements = pathElements.replace("<CENTER_Z>", str(z))
            pathElementsVarsTMP += "curve_rail_path_" + str(i) + ":,"

    # Now insert the path elements to the common template
    data = data.replace("<PATH_ELEMENTS>", pathElements)

    # Insert the vars for path elements - by this time we know what are
    # those - <PATH_ELEMENTS_VARS>
    pathElementsVars = pathElementsVarsTMP
    data = data.replace("<PATH_ELEMENTS_VARS>", pathElementsVars)

    print(data)

    # Write the results to the common file
    f = open(pathToApp + "A_Curved_Rail.dfa", "w")
    f.write(data)
    beams = ""
    for i in range(len(dataPoints)):
        beams = beams + dataBeam.replace("<ID>", str(i))
        beams = beams.replace("<START_X>", str(dataPoints[i][0]))
        beams = beams.replace("<START_Y>", str(dataPoints[i][1]))
        beams = beams.replace("<ROOF_HEIGHT>", str(3000)) #Må erstatte hardkoden med input-høyde fra brukeren
    f.write(beams)
    f.close()

#run()
