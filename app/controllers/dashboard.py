from typing import List, Optional, Dict

import pymongo

from app.config import dashboard as c
from app.controllers.user import User
from app.database import aggregate_features


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

        Returns (dict): {
            "product_assortment": [{}],
            "top_colors": [{}],
            "top_style": [{}],
            "top_performancer": [{}],
            "price_range": [{
                "farfetch": {"min": 100, "max": 500, "avg": 125},
                "macys": {"min": 100, "max": 500, "avg": 125} }],
            "promotion": [{}],
            "top_material": [{}],
            "top_print": [{}],
            "newsletter_tracking": [{}],
            "trend_report": [{}]


        """

        product_assortment_count, product_assortment_aggr = aggregate_features(collection,
                                                                               feature=c.PRODUCT_SUBCATEGORY_0,
                                                                               brands=self._brands,
                                                                               vendors=self._vendors,
                                                                               start_date=self._start_date,
                                                                               end_date=self._end_date)
        color_count, top_colors_aggr = aggregate_features(collection,
                                                          feature=c.COLOR_VAR_NAME,
                                                          brands=self._brands,
                                                          vendors=self._vendors,
                                                          start_date=self._start_date,
                                                          end_date=self._end_date)

        product_assortment = [
            {"name": x[c.PRODUCT_SUBCATEGORY_0],
             "percentage": round(x["count"] / product_assortment_count, 2) * 100
             } for x in product_assortment_aggr[:c.NUMBER_TOP_SUBCATEGORIES_DASHBOARD]]

        top_colors = [
            {"name": x[c.COLOR_VAR_NAME],
             "percentage": round(x["count"] / color_count, 2) * 100
             } for x in top_colors_aggr[:c.NUMBER_TOP_COLORS_DASHBOARD]]

        return {
            "product_assortment": product_assortment,
            "top_colors": top_colors,
            "top_style": [{}],
            "top_performancer": [{}],
            "price_range": [{
                "farfetch": {"min": 100, "max": 500, "avg": 125},  # TODO: get according to vendors defined in settings
                "macys": {"min": 100, "max": 500, "avg": 125}}],
            "promotion": [{}],
            "top_material": [{}],
            "top_print": [{}],
            "newsletter_tracking": [{}],
            "trend_report": [{}]
        }
