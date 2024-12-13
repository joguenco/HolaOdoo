import logging

from odoo import models

logger = logging.getLogger(__name__)


class CustomIrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _slug(cls, value: models.BaseModel | tuple[int, str]) -> str:
        try:
            return super()._slug(value)
        except ValueError as e:
            logger.error("Error in custom_slug.py file, when call _slug() method:", e)
            return ""
