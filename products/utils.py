from datetime import datetime
from django.template.defaultfilters import date


def get_queryset_column_model_names(model, queryset):
    if queryset is None:
        return []

    columns = []
    def append_column(x): return columns.append((column, x))
    for column in queryset.keys():
        column_name = model.get_column_name(column)

        if column_name is None:
            column_name = date(datetime.strptime(
                column, '%Y-%m-%d'), 'd F Y')

        append_column(column_name)

    return columns
