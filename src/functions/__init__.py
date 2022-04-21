from src.functions.ackley import ackley, get_acley_domain
from src.functions.levy import levy, get_levy_domain
from src.functions.rastrigin import rastrigin, get_rastrigin_domain
from src.functions.rosenbrock import rosenbrock, get_rosenbrock_domain
from src.functions.schwefel import schwefel, get_schwefel_domain

function_dict = {"ackley": ackley, "levy": levy, "rastrigin": rastrigin, "rosenbrock": rosenbrock, "schwefel": schwefel}
domains = [get_acley_domain(), get_levy_domain(), get_rastrigin_domain(), get_rosenbrock_domain(), get_schwefel_domain()]