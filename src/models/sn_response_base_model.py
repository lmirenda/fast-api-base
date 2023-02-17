from datetime import datetime
from typing import Optional

from .sn_base_model import SNBaseModel


class SNResponseBaseModel(SNBaseModel):
    echo_request: dict = {}
    data: Optional[dict]
    errors: Optional[list[dict]]
    timestamp: datetime = datetime.now()
