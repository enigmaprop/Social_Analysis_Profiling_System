class NodeModel:
    label = None
    required_fields = []

    def __init__(self, **props):
        self.props = props

    def to_dict(self):
        return self.props
