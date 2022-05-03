
from turtle import right
import matplotlib.pyplot as plt
import numpy as np
import os

def plot(experiment_alias, function_names, values, normalized = True):
    if (normalized):
        values = normalize(values)
    #Variable for x_axis control
    current_x = 0
    for func, value in zip(function_names, values):
        x = len(value)
        plt.yscale("log")
        plt.plot(range(x), value, label = func)
        if (x>current_x):
            current_x = x
            plt.xlim(right = current_x)
    plt.xlabel('Epochs')
    # plt.ylabel('KS and Auroc') 
    plt.legend()
    curr_path = os.path.abspath(__file__)
    save_dir = os.path.join(curr_path, "experiment_results")
    plt.savefig(experiment_alias + ".png")
    plt.cla()
    plt.clf()

def normalize(values):
    for value in values:
        for i, v in enumerate(value):
            value[i] = 10000/(1 + np.exp(-v))
    #teste = values.copy()
    #teste = sorted(teste)
    #if teste[0] < 0:
    #    "ihh raapaz"
    return values
