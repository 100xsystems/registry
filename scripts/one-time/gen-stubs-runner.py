#!/usr/bin/env python3
"""Generate complete 21-lesson courses for all stub languages.

Run from anywhere inside the registry repo:

    python3 scripts/one-time/gen-stubs-runner.py

Writes lesson .md files + index.json lessons arrays for every language in
gen_stub_data_*.py, replacing the old 2-lesson templates.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_stub_lib import run_all  # noqa: E402
from gen_stub_data_shell import SPECS as SPECS_A  # noqa: E402
from gen_stub_data_b import SPECS as SPECS_B  # noqa: E402
from gen_stub_data_c import SPECS as SPECS_C  # noqa: E402
from gen_stub_data_d import SPECS as SPECS_D  # noqa: E402
from gen_stub_data_e import SPECS as SPECS_E  # noqa: E402
from gen_stub_data_f import SPECS as SPECS_F  # noqa: E402
from gen_stub_data_g import SPECS as SPECS_G  # noqa: E402

ALL = SPECS_A + SPECS_B + SPECS_C + SPECS_D + SPECS_E + SPECS_F + SPECS_G

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'static-data', 'knowledge', 'languages',
)

if __name__ == '__main__':
    print(f'Generating {len(ALL)} languages...')
    run_all(ALL, BASE)
    print('Done.')
