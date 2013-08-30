class Empresa(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'empresa':
            return 'empresa'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'empresa':
            return 'empresa'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'empresa' or \
           obj2._meta.app_label == 'empresa':
           return True
        return None

    def allow_syncdb(self, db, model):
        return True