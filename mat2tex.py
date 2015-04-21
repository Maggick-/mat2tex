# MAT2TEX is a function to print out a Python Numpy [Mat]rix to La[TeX]
#
# ABOUT:
#
# PUBLIC REPOSITORY:
#   - https://github.com/Maggick-/mat2tex
#
# HISTORY:
#   2014-04-21: Nick Maggio (nickmaggio [at] ymail [dot] com)
#   - Intial version
#
# TODO:
#   - Fix error handling
#   - Tidy up code
#   - Format output of different types
#   - Add function comments
#
# LICENSE:
#   The MIT License (MIT)
#
#   Copyright 2014 Nick Maggio
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to 
#   deal in the Software without restriction, including without limitation the 
#   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
#   sell copies of the Software, and to permit persons to whom the Software is 
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in 
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
#   IN THE SOFTWARE.
#
# REFERENCES:
#
#

__author__ = "Nick Maggio"
__copyright__ = "Copyright 2014, Maggick"
__credits__ = ["Nick Maggio"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Nick Maggio"
__email__ = "nickmaggio@ymail.com"
__status__ = "Production"

import numpy as np

def mat2tex(mat,x_title=[],y_title=[],align=[],hline=True,vline=True):

    # Check type
    if type(mat).__module__ != np.__name__:
        pass

    # Check length
    if len(mat.shape) is 1:
        [row, col] = mat.shape+(1,)
    elif len(mat.shape) is 2:
        [row, col] = mat.shape
    else:
        row = mat.shape[0]
        col = mat.shape[1]

    if align == []:
        if vline:
            align = '|'
        else:
            align = ''

        for idx in range(col):
            if vline:
                align += 'c|'
            else:
                align += 'c'

    strRow = ''

    print 
    print '\\begin{tabular}{%s}' % (align)
    if hline:
        print '\\hline'
    if x_title != []:
        if len(x_title) == col:
            for idn in range(col):
                strRow += str(x_title[idn])
                if idn+1 != col:
                    strRow +='&'
            if hline:
                strRow += '\\\\ \\hline'
            else:
                strRow += '\\\\'
        print strRow

    for idx in range(row):
        strRow = ''
        for idn in range(col):
            strRow += str(mat[idx,idn])
            if idn+1 != col:
                strRow +='&'
        if hline:
            strRow += '\\\\ \\hline'
        else:
            strRow += '\\\\'
        print strRow
    print '\\end{tabular}'
    print

if __name__ == "__main__":

    x_title = ['5','5','e','3','4']

    v = np.random.randn(5,5)

    mat2tex(v,x_title)
