#!/usr/bin/env python
from __future__ import division
from random import random
from math import pi
import matplotlib.pyplot as plt


"""
Script para simular puntos en un campo cuadrado. 
Contando el número de puntos en el círculo de radio inscrito igual a la longitud del campo. 
La relación entre el número de puntos en el círculo y el número total de puntos muestra una estimación "PI"

"""

#Cantidad de puntos
def rain_drop(length_of_field=1):

    return [(.5 - random()) * length_of_field, (.5 - random()) * length_of_field]

#Punto dentro del circulo
def is_point_in_circle(point, length_of_field=1):

    return (point[0]) ** 2 + (point[1]) ** 2 <= (length_of_field / 2) ** 2

#Funcion para dibujar los puntos
def plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field=1, format='pdf'):

    number_of_drops_in_circle = len(drops_in_circle)
    number_of_drops_out_of_circle = len(drops_out_of_circle)
    number_of_drops = number_of_drops_in_circle + number_of_drops_out_of_circle
    plt.figure()
    plt.xlim(-length_of_field / 2, length_of_field / 2)
    plt.ylim(-length_of_field / 2, length_of_field / 2)
    plt.scatter([e[0] for e in drops_in_circle], [e[1] for e in drops_in_circle], color='blue', label="Puntos dentro del círculo")
    plt.scatter([e[0] for e in drops_out_of_circle], [e[1] for e in drops_out_of_circle], color='black', label="Puntos fuera del circulo")
    plt.legend(loc="center")
    plt.title("%s drops: %s puntos en el círculo, PI estimado: $\pi$ as %.4f." % (number_of_drops, number_of_drops_in_circle, 4 * number_of_drops_in_circle / number_of_drops))
    plt.savefig("%s_drops.%s" % (number_of_drops, format))

#Funcion para generar la lluvia de puntos
def rain(number_of_drops=1000, length_of_field=1, plot=True, format='pdf', dynamic=False):

    number_of_drops_in_circle = 0
    drops_in_circle = []
    drops_out_of_circle = []
    pi_estimate = []
    for k in range(number_of_drops):
        d = (rain_drop(length_of_field))
        if is_point_in_circle(d, length_of_field):
            drops_in_circle.append(d)
            number_of_drops_in_circle += 1
        else:
            drops_out_of_circle.append(d)
        if dynamic:  # Nos permite crear animaciones dinámicas simuladas.
            print ("Número de puntos trazados: %s" % (k + 1))
            plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field, format)
        pi_estimate.append(4 * number_of_drops_in_circle / (k + 1))  # Actualiar los valors de estimación
    # Trazar estiamciones de PI
    plt.figure()
    plt.scatter(range(1, number_of_drops + 1), pi_estimate)
    max_x = plt.xlim()[1]
    plt.hlines(pi, 0, max_x, color='black')
    plt.xlim(0, max_x)
    plt.title("$\pi$ Estimación contra el número de puntos")
    plt.xlabel("Número de puntos")
    plt.ylabel("$\pi$")
    plt.savefig("Pi_estimate_for_%s_result.pdf" % number_of_drops)

    if plot and not dynamic:

        plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field, format)

    return [number_of_drops_in_circle, number_of_drops]


if __name__ == "__main__":

    from sys import argv
    number_of_drops = 100
    if len(argv) > 1: #Si se pasa un argumento, cambie el numero de gotas que se simularan.
        number_of_drops = eval(argv[1])

    #r = rain(number_of_drops, plot=True, format='png', dynamic=True)
    r = rain(number_of_drops, plot=True, format='png', dynamic=False)
    # Print:
    print ("----------------------")
    print ("%s Puntos" % number_of_drops)
    print ("PI estimado :")
    print ("\t%s" % (4 * r[0] / r[1]))
    print ("----------------------")
