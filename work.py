# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Work']


class Work:
    __metaclass__ = PoolMeta
    __name__ = 'project.work'
    galatea = fields.Boolean('Galatea',
        help='Allow to show at Galatea')

    @classmethod
    def __setup__(cls):
        super(Work, cls).__setup__()
        cls.party.states['invisible'] = []
        cls.party_address.states['invisible'] = []

    @staticmethod
    def default_galatea():
        return True

    @fields.depends('parent')
    def on_change_with_party(self):
        if self.parent and self.parent.party:
            return self.parent.party.id

    @fields.depends('parent')
    def on_change_with_party_address(self):
        if self.parent and self.parent.party_address:
            return self.parent.party_address.id
