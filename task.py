"""
Class definition for task object.

TO DO:
* make task metaclass?
* task handles event loop, with list of functions to call each iteration?
"""

import initializers
import controller, display
from psychopy.core import monotonicClock, Clock
import psychopy.event as event

class Task:
    def __init__(self, taskname, subject):
        self.taskname = taskname
        self.subject = subject
        self.keep_running = True
        self.setup()

    def setup(self):
        self.pars = initializers.setup_pars("parameters.json")
        self.win = initializers.setup_window()
        self.display = display.Display(self.win, self.pars)
        # plexon init here ...
        self.outfile = initializers.setup_data_file(self.taskname, 
            self.subject)
        self.controller = controller.Controller()
        self.data = []

    def teardown(self):
        # plexon close here...
        self.win.close()

    def run(self):
        self.start_time = monotonicClock.getTime()

        self.display.draw()
        event.waitKeys()
        self.display.onset(3, 'go')
        clk = Clock()
        while clk.getTime() < 2:
            self.display.draw()
        self.display.offset(3)
        clk.reset() 
        while clk.getTime() < 2:
            self.display.draw()

        event.waitKeys()