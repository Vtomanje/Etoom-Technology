from django.db import models


class EntryManager(models.Manager):
    """ porcedimiento para entradas"""
    
    def entrada_en_banner(self):
        return self.filter(
            public=True,
            banner=True,
        ).order_by('-created').first()
        
    def entradas_en_home(self):
        #devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
        
    def entradas_recientes(self):
        #devuelve las ultimas 6 entradas en home
        return self.filter(
            public=True,
            in_home=True
        ).order_by('-created')[:6]
    
    def buscar_entrada(self, kword, categoria):
        # procedimiento para buscar entradas por categorias o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')