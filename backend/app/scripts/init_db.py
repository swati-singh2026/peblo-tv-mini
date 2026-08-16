import json

from app.db.session import SessionLocal
from app.models.show import Show
from app.models.season import Season
from app.models.episode import Episode

db = SessionLocal()

with open("app/data/seed_shows.json", "r", encoding="utf-8") as f:
    data = json.load(f)

shows = {}
seasons = {}

for item in data:

    # ----------------------------
    # Show
    # ----------------------------
    slug = item["slug"]

    if slug not in shows:

        show = Show(
            title=item["show_title"],
            slug=slug,
            synopsis=item["synopsis"],
            category=", ".join(item["categories"]),
            section=item["section"],
            published=item["status"] == "published",
        )

        db.add(show)
        db.flush()

        shows[slug] = show

    show = shows[slug]

    # ----------------------------
    # Season
    # ----------------------------
    season_key = (show.id, item["season_number"])

    if season_key not in seasons:

        season = Season(
            show_id=show.id,
            season_number=item["season_number"],
            title=f"Season {item['season_number']}",
        )

        db.add(season)
        db.flush()

        seasons[season_key] = season

    season = seasons[season_key]

    # ----------------------------
    # Episode
    # ----------------------------
    episode = Episode(
        season_id=season.id,
        episode_number=item["episode_number"],
        title=item["episode_title"],
        duration_seconds=item["duration_seconds"],
        language=item["language"],
        content_group=item["content_group"],
        artwork=len(item["artwork_available"]) > 0,
        published=item["status"] == "published",
    )

    db.add(episode)

db.commit()

print("✅ Seed data imported successfully!")
print(f"Shows: {len(shows)}")
print(f"Seasons: {len(seasons)}")
print(f"Episodes: {len(data)}")

db.close()