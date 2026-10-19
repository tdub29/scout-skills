"""Strip openpyxl's empty cached <v></v> after <f> so Excel stops dropping formulas (the "Removed Records: Formula" repair defect in openpyxl 3.1.5)."""

import os
import shutil
import sys
import zipfile


def finalize_xlsx(path):
    """Remove empty cached formula values from every worksheet XML in the xlsx, rewriting in place.

    openpyxl 3.1.5 emits "</f><v></v>" (or "</f><v/>") after each formula cell. Excel
    reads the empty cached value, reports "Removed Records: Formula", and strips the
    formulas on open. Removing the empty <v> lets Excel recalculate the cell on open.
    """
    tmp = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                name = item.filename.replace("\\", "/")
                if name.startswith("xl/worksheets/") and name.endswith(".xml"):
                    text = data.decode("utf-8")
                    text = text.replace("</f><v></v>", "</f>")
                    text = text.replace("</f><v/>", "</f>")
                    data = text.encode("utf-8")
                zout.writestr(item, data)
    os.replace(tmp, path)
    return path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python finalize_xlsx.py <path-to-xlsx>")
        sys.exit(1)
    out = finalize_xlsx(sys.argv[1])
    print("finalized: " + out)
