import os, io
from pathlib import Path
import requests
from PIL import Image

OUT = Path('assets/img/projects')
OUT.mkdir(parents=True, exist_ok=True)

# Curated direct URLs (royalty-free). If any fail, they will be skipped.
URLS = [
  # Industrial shed / factory interior (generic industrial)
  'https://images.pexels.com/photos/532791/pexels-photo-532791.jpeg',
  # Roof waterproofing / construction roof
  'https://images.pexels.com/photos/159306/construction-build-concrete-architecture-159306.jpeg',
  # Fireproofing / steel structure representative
  'https://images.pexels.com/photos/2760241/pexels-photo-2760241.jpeg',
  # Basement waterproofing / basement construction
  'https://images.pexels.com/photos/584399/pexels-photo-584399.jpeg',
  # Retrofit / concrete repair (site work)
  'https://images.pexels.com/photos/2219024/pexels-photo-2219024.jpeg',
  # Firestopping / services (cables/pipes in construction)
  'https://images.pexels.com/photos/239380/pexels-photo-239380.jpeg',
  # Road & boundary works (road construction)
  'https://images.pexels.com/photos/3856252/pexels-photo-3856252.jpeg',
  # Academic campus / modern building
  'https://images.pexels.com/photos/373912/pexels-photo-373912.jpeg',
]

saved = []
for i, url in enumerate(URLS, start=1):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        img = Image.open(io.BytesIO(r.content)).convert('RGB')
        out_path = OUT / f'project{i:02d}.webp'
        img.save(out_path, 'WEBP', quality=80, method=6)
        saved.append(str(out_path))
        print(f'SAVED {out_path}')
    except Exception as e:
        print(f'FAILED {url}: {e}')

print('DONE', len(saved))
