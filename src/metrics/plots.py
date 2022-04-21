
import matplotlib.pyplot as plt
def plot(experiment_name, function_names, values, normalized = True):
    if (normalized):
        values = normalize(values)

    for func, value in zip(function_names, values):
        plt.plot(range(len(value)), value, label = func)
    plt.xlabel('Epochs')
    # plt.ylabel('KS and Auroc') 
    plt.legend()
    plt.savefig(experiment_name)

def normalize(values):
    for value in values:
            dmax = max(value)
            dmin = min(value)
            for i, v in enumerate(value):
                value[i] = (value[i] - dmin)/(dmax-dmin)
    return values