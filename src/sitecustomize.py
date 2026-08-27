"""Let CuPy find a CUDA runtime on Windows without a full CUDA Toolkit install.

Python 3.8+ ignores ``PATH`` when resolving the DLL dependencies of extension
modules, so exporting ``PATH`` does not help CuPy locate ``cudart64_12.dll`` and
``spacy.require_gpu()`` fails with "CuPy is not installed" even though CuPy is
installed and ``torch.cuda.is_available()`` is True.

The PyTorch CUDA wheel already ships the runtime CuPy needs (``cudart64_12.dll``,
``cublas64_12.dll``, ``nvrtc64_120_0.dll``) inside ``torch/lib``, so register that
directory explicitly instead of installing a second copy of the CUDA toolkit.

``site`` imports this module automatically at interpreter startup as long as its
directory is on ``PYTHONPATH``. The notebooks put this ``src/`` directory there so
that ``spacy train`` **subprocesses** inherit the fix as well - ``add_dll_directory``
applies only to the calling process and does not propagate to children.
"""

import os
import sys
import warnings
from pathlib import Path

if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
    _torch_lib = Path(sys.prefix) / "Lib" / "site-packages" / "torch" / "lib"
    if _torch_lib.is_dir():
        try:
            os.add_dll_directory(str(_torch_lib))
        except OSError as exc:
            warnings.warn(
                f"could not register {_torch_lib} for DLL lookup ({exc}); "
                "CuPy may fail to import and spaCy will fall back to CPU",
                RuntimeWarning,
            )
