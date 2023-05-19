import analytix
from analytix import Client

# Let's enable the logger so we can see what's going on.
analytix.enable_logging()


client = Client("client_secret_898467674662-a1b5vidubbadgt1om1cic23mho33ngok.apps.googleusercontent.com.json")
with Client("client_secret_898467674662-a1b5vidubbadgt1om1cic23mho33ngok.apps.googleusercontent.com.json") as client:
    report = client.retrieve_report(
        dimensions=("video", "day"),
        max_results=200,
        sort_options=("-views",),
        metrics=("views", "likes", "comments"),
    )
    
# report = client.retrieve_report(
#     dimensions=("day",),
#     filters={"country": "US"},
#     metrics=("views", "l ikes", "comments"),
# ) 
report.to_csv("./analytics.csv")


# if __name__ == "__main__":
#     with Client("client_secret_898467674662-a1b5vidubbadgt1om1cic23mho33ngok.apps.googleusercontent.com.json") as client:
#         report = client.retrieve_report(
#             dimensions=("video",),
#             metrics=("estimatedMinutesWatched", "views", "likes", "subscribersGained"),
#             max_results=10,
#             sort_options=("-estimatedMinutesWatched",),
#         )
#         # report.to_csv("top_10_watched_videos.csv")