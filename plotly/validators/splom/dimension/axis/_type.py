import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='type', parent_name='splom.dimension.axis', **kwargs
    ):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+clearAxisTypes',
            role='info',
            values=['linear', 'log', 'date', 'category'],
            **kwargs
        )
