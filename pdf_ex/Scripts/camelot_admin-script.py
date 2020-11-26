#!e:\gst_files\varasity_exe\pdf_ex\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Camelot==12.6.29','console_scripts','camelot_admin'
__requires__ = 'Camelot==12.6.29'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Camelot==12.6.29', 'console_scripts', 'camelot_admin')()
    )
