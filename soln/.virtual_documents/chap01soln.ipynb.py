try:
    import pint
except ImportError:
    get_ipython().getoutput("pip install pint")
    import pint


try:
    from modsim import *
except ImportError:
    get_ipython().getoutput("pip install modsim")
    from modsim import *


# Configure Jupyter so figures appear in the notebook
get_ipython().run_line_magic("matplotlib", " inline")

# Configure Jupyter to display the assigned value after an assignment
get_ipython().run_line_magic("config", " InteractiveShell.ast_node_interactivity='last_expr_or_assign'")


get_ipython().getoutput("python --version")


get_ipython().getoutput("jupyter --version")


meter = UNITS.meter


second = UNITS.second


UNITS.


a = 9.8 * meter / second**2


t = 4 * second


a * t**2 / 2


# Solution

a * t


# Solution

# a + t


h = 381 * meter


t = sqrt(2 * h / a)


v = a * t


mile = UNITS.mile
hour= UNITS.hour


v.to(mile/hour)


# Solution

foot = UNITS.foot
pole_height = 10 * foot

h + pole_height


# Solution
pole_height + h


# Solution

v_terminal = 18 * meter / second 


# Solution

t1 = v_terminal / a
print('Time to reach terminal velocity', t1)


# Solution

h1 = a * t1**2 / 2
print('Height fallen in t1', h1)


# Solution

t2 = (h - h1) / v_terminal
print('Time to fall remaining distance', t2)


# Solution

t_total = t1 + t2
print('Total falling time', t_total)



