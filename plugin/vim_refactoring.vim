let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python', 'src'))
sys.path.insert(0, python_root_dir)
import convert_buffer
import json_refactoring
import vim_refactoring
EOF

function! RefactorJson()
    python3 vim_refactoring.refactor_json()
endfunction

command! -nargs=0 PrintCountry call PrintCountry()
command! -nargs=0 RefactorJson call RefactorJson()