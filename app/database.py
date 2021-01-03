from typing import Optional, List, Tuple, Any
import time


def aggregate_features(collection, feature="color_normalname", brands: List = [], vendors: List = [],
                       start_date: int = 20200101, end_date: Optional[int] = None) -> Tuple[Any, Any]:

    filters = []
    if not end_date:
        end_date = int(time.strftime("%Y%m%d", time.gmtime()))

    filters.append({"$gte": ["$date", start_date]})

    filters.append({"$lte": ["$date", end_date]})

    count_filter = {"date": {"$gte": start_date, "$lte": end_date}}

    if brands:
        filters.append({"$in": ["$brand", brands]})
        count_filter.update({"brand": {"$in": brands}})

    if vendors:
        filters.append({"$in": ["$vendor", vendors]})
        count_filter.update({"vendor": {"$in": vendors}})

    return collection.count_documents(count_filter), collection.aggregate([
        {
            "$match": {
                feature: {"$not": {"$size": 0}}
            }
        },
        {"$unwind": f"${feature}"},
        {
            "$group": {
                "_id": {"$toLower": f'${feature}'},
                "count": {"$sum": {"$cond": [{"$and": filters}, 1, 0]}}
            }
        },
        {
            "$match": {
                "count": {"$gte": 2}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 100},
        {"$project": {
            "_id": 0, feature: "$_id",
            "count": "$count",

        }
        }
    ])
