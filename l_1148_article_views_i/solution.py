import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    authors_own = views["author_id"][views["author_id"] == views["viewer_id"]]
    authors_uniq = authors_own.unique()
    authors_uniq_df = pd.DataFrame({"id": authors_uniq})

    return authors_uniq_df.sort_values("id")
