from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

print(BASE_DIR)
print(os.path.join(BASE_DIR, 'Fronted\\front\\dist'))