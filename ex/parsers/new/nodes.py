

class Node(object):
    pass

class RangeNode(Node):
    def __init__(self,
            start_line=None,
            end_line=None,
            must_recompute_start_line=False):
        self.start_line = start_line
        self.end_line = end_line
        self._must_recompute_start_line = must_recompute_start_line
        self.start_offset = []
        self._end_offset = []
        self.right_hand_side = False

    def __repr__(self):
        return ('<{0}(start:{1}, end:{2}, loffset:{3}, roffset:{4}, semicolon:{5}]>'
            .format(self.__class__.__name__, self.start_line, self.end_line,
                self.start_offset, self.end_offset, self.must_recompute_start_line))

    def __eq__(self, other):
        if not isinstance(other, RangeNode):
            return False
        return (self.start_line == other.start_line and
                self.end_line == other.end_line and
                self.must_recompute_start_line == other.must_recompute_start_line and
                self.start_offset == other.start_offset and
                self.end_offset == other.end_offset)

    @property
    def must_recompute_start_line(self):
        return self._must_recompute_start_line

    @must_recompute_start_line.setter
    def must_recompute_start_line(self, value):
        if self._must_recompute_start_line is True:
            raise ValueError("must_recompute_start_line is already set")
        self._must_recompute_start_line = value

    @property
    def end_offset(self):
        return self._end_offset

    @end_offset.setter
    def end_offset(self, value):
        if len(self._end_offset) > 0:
            raise ValueError("end_offset is already set")
        self._end_offset = value


class CommandNode(Node):
    def __init__(self, command_token):
        self.name = command_token.content
        self.arguments = command_token.params
        self.flags = command_token.params.get('flags', [])
        self.count = command_token.params.get('count', 1)


class CommandLineNode(Node):
    def __init__(self, line_range, command):
        self.line_range = line_range
        self.command = command