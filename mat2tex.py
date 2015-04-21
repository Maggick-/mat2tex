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
