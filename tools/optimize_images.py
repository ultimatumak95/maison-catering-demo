from pathlib import Path
from PIL import Image, ImageOps


# =========================
# PATHS
# =========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_DIR = (
    PROJECT_ROOT
    / "source-assets"
    / "freepik-originals"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "assets"
    / "images"
)


SUPPORTED_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
]


# =========================
# IMAGE CONFIGURATION
# =========================

IMAGES = {

    # HERO
    "hero-catering": {
        "ratio": (16, 9),
        "sizes": [
            (640, 360),
            (960, 540),
            (1440, 810),
        ],
    },


    # SERVICES
    "service-wedding": {
        "ratio": (4, 3),
        "sizes": [
            (480, 360),
            (768, 576),
            (1200, 900),
        ],
    },

    "service-corporate": {
        "ratio": (4, 3),
        "sizes": [
            (480, 360),
            (768, 576),
            (1200, 900),
        ],
    },

    "service-private-event": {
        "ratio": (4, 3),
        "sizes": [
            (480, 360),
            (768, 576),
            (1200, 900),
        ],
    },


    # ABOUT
    "about-chef": {
        "ratio": (4, 5),
        "sizes": [
            (480, 600),
            (768, 960),
            (1200, 1500),
        ],
    },


    # GALLERY FOOD
    "gallery-food-01": {
        "ratio": (3, 2),
        "sizes": [
            (480, 320),
            (768, 512),
            (1200, 800),
        ],
    },

    "gallery-food-02": {
        "ratio": (3, 2),
        "sizes": [
            (480, 320),
            (768, 512),
            (1200, 800),
        ],
    },

    "gallery-food-03": {
        "ratio": (3, 2),
        "sizes": [
            (480, 320),
            (768, 512),
            (1200, 800),
        ],
    },


    # GALLERY EVENT
    "gallery-event-01": {
        "ratio": (4, 5),
        "sizes": [
            (480, 600),
            (768, 960),
            (960, 1200),
        ],
    },

    "gallery-event-02": {
        "ratio": (4, 5),
        "sizes": [
            (480, 600),
            (768, 960),
            (960, 1200),
        ],
    },

    "gallery-event-03": {
        "ratio": (4, 5),
        "sizes": [
            (480, 600),
            (768, 960),
            (960, 1200),
        ],
    },
}


# =========================
# FIND SOURCE IMAGE
# =========================

def find_source_image(name):

    for extension in SUPPORTED_EXTENSIONS:

        image_path = (
            SOURCE_DIR
            / f"{name}{extension}"
        )

        if image_path.exists():
            return image_path

    return None


# =========================
# PROCESS IMAGE
# =========================

def process_image(
    source_path,
    output_path,
    output_size
):

    with Image.open(source_path) as image:

        image = ImageOps.exif_transpose(image)

        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGB")

        image = ImageOps.fit(
            image,
            output_size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )

        image.save(
            output_path,
            "WEBP",
            quality=80,
            method=6,
        )


# =========================
# MAIN
# =========================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print()
    print("Generating responsive images...")
    print()


    for name, config in IMAGES.items():

        source_path = find_source_image(name)

        if source_path is None:

            print(
                f"[MISSING] {name}"
            )

            continue


        for width, height in config["sizes"]:

            output_name = (
                f"{name}-{width}.webp"
            )

            output_path = (
                OUTPUT_DIR
                / output_name
            )

            process_image(
                source_path,
                output_path,
                (width, height),
            )

            size_kb = (
                output_path.stat().st_size
                / 1024
            )

            print(
                f"[OK] "
                f"{output_name} "
                f"{width}x{height} "
                f"{size_kb:.0f} KB"
            )


    print()
    print("Finished.")
    print()


if __name__ == "__main__":
    main()