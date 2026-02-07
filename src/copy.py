import shutil

from pathlib import Path


def copy_all_from_source_to_target(source_path, target_path):
    root = Path(__file__).resolve().parents[1]

    src = Path(source_path)
    if not src.is_absolute():
        src = root / src
    src = src.resolve()

    if not src.exists():
        raise FileNotFoundError(src)
    if not src.is_dir():
        raise NotADirectoryError(src)

    dst = Path(target_path)
    if not dst.is_absolute():
        dst = root / dst
    dst = dst.resolve()

    if not dst.is_dir():
        raise NotADirectoryError(dst)

    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)

    c = list(src.iterdir())
    
    for cc in c:
        if cc.is_file():
            shutil.copy2(f, dst)
        if cc.is_dir():
            tdir = (dst / d.name)
            copy_all_from_source_to_target(d, tdir)
