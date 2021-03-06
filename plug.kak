# kak-plug: Kakoune plugin manager
# ===============================
#
#   git clone https://github.com/kdheepak/kak-plug.git ~/.config/kak/autoload/kak-plug/
#
#
# MIT License
#
# Copyright (c) 2018 Dheepak Krishnamurthy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

declare-option str-list plugin_list

declare-option -docstring "Folder where kak-plug is installed" str kak_plug_dir %sh{ echo "$HOME/.config/kak/autoload/kak-plug" }

define-command plug -params 1.. %{
    set -add current plugin_list %arg{@}
    nop %sh{
        (
            python $kak_opt_kak_plug_dir/kak_plug/kak_plug.py install ${@}
        ) >/dev/null 2>&1 </dev/null &
   }
}

define-command plugUpdate %{
    nop %sh{
        (
            echo $kak_opt_plugin_list
            python $kak_opt_kak_plug_dir/kak_plug/kak_plug.py update $kak_opt_plugin_list
        ) >/dev/null 2>&1 </dev/null &
   }

}

