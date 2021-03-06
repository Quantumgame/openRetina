# -*- coding: utf8 -*-
from __future__ import division, print_function
"""
openRetina : a basic thalamic layer

See https://github.com/laurentperrinet/openRetina

"""
__author__ = "(c) Pierre Albiges, Victor Boutin & Laurent Perrinet INT - CNRS"

import subprocess
p = subprocess.Popen(['./photoreceptors.py'])

from openRetina import openRetina
thalamus = openRetina(model=dict(layer='thalamus', # label for this layer
                             input=['stream'], # input: can be the camera, noise, a movie (TODO)
                             output=['display','capture'],
                             #output=['capture'], # output: can be stream, display, capture,...
                             T_SIM=20))
thalamus.run()
