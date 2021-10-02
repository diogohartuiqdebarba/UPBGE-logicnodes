from uplogic.nodes import GEConditionNode
from uplogic.nodes import is_waiting


class GEKeyPressed(GEConditionNode):
    def __init__(self, pulse=False, key_code=None):
        GEConditionNode.__init__(self)
        self.pulse = pulse
        self.key_code = key_code
        self.network = None

    def setup(self, network):
        self.network = network

    def evaluate(self):
        keycode = self.get_socket_value(self.key_code)
        if is_waiting(keycode):
            return
        self._set_ready()
        keystat = self.network.keyboard_events[keycode]
        if self.pulse:
            self._set_value(
                (
                    keystat.active or keystat.activated
                )
            )
        else:
            self._set_value(keystat.activated)
