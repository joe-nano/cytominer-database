"""

"""

import perturbation.base
import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import sqlalchemy.orm.exc


class Well(perturbation.base.Base):
    """

    """

    __tablename__ = 'wells'

    position_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('coordinates.id'))
    position = sqlalchemy.orm.relationship('Coordinate')

    plates = sqlalchemy.orm.relationship('Plate', backref='wells')
