import gazu
import pandas as pd
from pathlib import Path
from typing import List, Dict

def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def parse_artists(df: pd.DataFrame) -> List[Dict]:
    """
    Expected columns:
        - email
        - first_name
        - last_name
        - role
    """
    return df.to_dict(orient="records")

def upload_artists(artists: List[Dict]):
    """
    Create artists if they do not already exist.
    """
    existing_users = {
        user["email"]: user
        for user in gazu.person.all_persons()
    }

    for artist in artists:
        if artist["email"] in existing_users:
            print(f"Artist exists: {artist['email']}")
            continue

        gazu.person.new_person(
            artist["first_name"],
            artist["last_name"],
            artist["email"],
        )
        print(f"Created artist: {artist['email']}")

if __name__ == "__main__":
    gazu.set_host("http://localhost/api")
    user = gazu.log_in("admin@example.com", "mysecretpassword")

    artists_df = load_csv(Path("artists.csv"))

    artists = parse_artists(artists_df)

    upload_artists(artists)
