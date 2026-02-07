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

    if not dst.exists():
        dst.mkdir(parents=True, exist_ok=True)
    else:
        if not dst.is_dir():
            raise NotADirectoryError(dst)
        shutil.rmtree(dst)

    c = list(src.iterdir())
    
    for cc in c:
        if cc.is_file():
            shutil.copy2(cc, dst)
        if cc.is_dir():
            tdir = (dst / cc.name)
            copy_all_from_source_to_target(cc, tdir)
