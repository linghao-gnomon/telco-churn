from pathlib import Path
import hashlib

source = Path("data/raw/telco.csv")  # Your input path.
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()

print(f"SHA256 hash of {source}: {source_hash}")