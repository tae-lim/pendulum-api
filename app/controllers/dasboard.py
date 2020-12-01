from typing import List, Optional, Dict

import pymongo

from app.controllers.user import User


class Dashboard:
    def __init__(self, user: User, start_date: int, end_date: int, brands: Optional[list], vendors: Optional[List]):
        """

        Args:
            user (app.controllers.user.User: User object
            start_date (int): format = yyyymmdd
            end_date (int): format = yyyymmdd
            brands optional(list): a list of brands, or None
            vendors optional(list): a list of vendors, or None
        """
        self._user = user
        self._start_date = start_date
        self._end_date = end_date
        self._brands = brands
        self._vendors = vendors

    def get_dashboard_data(self, collection: pymongo.collection.Collection) -> Dict[str, List[dict]]:
        """Get json data for each dashboard component

        Args:
            collection (pymongo.collection.Collection): pymongo database collection object

        Returns:

        """

        return {
            "product_assortment": [{}],
            "top_colors": [{}],
            "top_style": [{}],
            "top_performancer": [{}],
            "price_range": [{
                "farfetch": {"min": 100, "max": 500, "avg": 125},  #TODO: get according to vendors defined in settings
                "macys": {"min": 100, "max": 500, "avg": 125}
            }],
            "promotion": [{}],
            "top_material": [{}],
            "top_print": [{}],
            "newsletter_tracking": [{}],
            "trend_report": [{}]


        }
