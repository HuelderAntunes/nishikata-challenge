from django.db import models


class ProductUrl(models.Model):
    product_url = models.URLField()
    consult_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    image = models.URLField(blank=True, null=True)
    store_url = models.URLField()
    sales = models.IntegerField(default=0)

    def get_column_name(column):
        names = {
            'product_url': 'Produto',
            'created_at': 'Data inserção na loja',
            'sales': 'Total de vendas',
            'image': 'Imagens',
            'consult_date': 'Data de Consulta',
        }

        return names.get(column)

    def __str__(self):
        return self.product_url
