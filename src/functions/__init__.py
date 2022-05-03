from src.functions.ackley import ackley, get_acley_domain
from src.functions.levy import levy, get_levy_domain
from src.functions.rastrigin import rastrigin, get_rastrigin_domain
from src.functions.rosenbrock import rosenbrock, get_rosenbrock_domain
from src.functions.schwefel import schwefel, get_schwefel_domain

function_dict = {
    "ackley": (ackley, get_acley_domain()),
    "levy": (levy, get_levy_domain()),
    "rastrigin": (rastrigin, get_rastrigin_domain()),
    "rosenbrock": (rosenbrock, get_rosenbrock_domain()),
    "schwefel": (schwefel, get_schwefel_domain()),
}
