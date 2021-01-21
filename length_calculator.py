import numpy as np

def longer_than_standard(piece, length, offcuts):
        count = int(piece // length)
        remain = piece % length
        if remain > 0:
                count += 1
                offcut = length - remain
                offcuts = np.append(offcuts, offcut)
        number_of_length.append(count)
        return offcuts

def shorter_than_standard(pieces, length, offcuts, count=0):
        #print(pieces, length, offcuts)
        if len(pieces) > 0:
                count += 1
                offcut = length - pieces[0]
                pieces = np.delete(pieces, 0)
                #print(pieces)
                if offcut > 0:
                        offcuts = np.append(offcuts, offcut)
                number_of_length.append(count)
                #print('wee')
        return pieces, offcuts
        
                
def offcut_check(offcuts, pieces):
        for i in set(offcuts) & set(pieces): 
                pieces = np.delete(pieces, np.argwhere(pieces == i)[0])
                offcuts = np.delete(offcuts, np.argwhere(offcuts == i)[0])

        offcuts = np.sort(offcuts)[::-1]
        pieces = np.sort(pieces)[::-1]
        #print('initial pieces', pieces)
        try:
                while offcuts[0] > pieces[0]:
                        offcut = offcuts[0] - pieces[0]
                        #print(f'{offcuts[0]} - {pieces[0]} = {offcut}')
                        first_piece = pieces[0]
                        #print('first piece', first_piece)
                        first_offcut = offcuts[0]
                        offcuts = np.append(offcuts, offcut)
                        offcuts = np.sort(offcuts)[::-1]
                        offcuts = np.delete(offcuts, np.argwhere(offcuts == first_offcut)[0])
                        #print('offcut', offcuts)
                        pieces  = np.delete(pieces, np.argwhere(pieces == first_piece)[0])
                        #print('pieces', pieces)
        except IndexError:
                pass
       # print('I reach here. Their father')
        return pieces, offcuts

def lengths(pieces, market_standard):
        global offcuts, number_of_length
        number_of_length = []
        offcuts = np.array([])
        pieces = np.array(pieces)
        pieces = np.sort(pieces)[::-1]
        shorter_pieces = pieces[pieces < market_standard]
        longer_pieces = pieces[pieces >= market_standard]

        if len(longer_pieces) > 0:
                for piece in longer_pieces:
                        offcuts = longer_than_standard(piece, market_standard, offcuts)
                #print('initial offcuts', np.sort(offcuts)[::-1])
        if len(shorter_pieces) > 0:
                while len(shorter_pieces) > 0:
                        shorter_pieces = np.sort(shorter_pieces)[::-1]
                        shorter_pieces, offcuts = offcut_check(offcuts, shorter_pieces)
                        shorter_pieces, offcuts = shorter_than_standard(shorter_pieces, market_standard, offcuts)
                        #print('we here')
                        #print(sum(number_of_length))

        offcuts = np.round_(offcuts, decimals=3)
        offcuts = np.delete(offcuts, np.argwhere(offcuts == 0))
        OFfcuts, COunts = np.unique(offcuts, return_counts=True)
        OFFCUTS = {}
        for i in tuple(zip(COunts, OFfcuts)):
                OFFCUTS.update({i[0]:i[1]})
                    

        return sum(number_of_length), OFFCUTS
                        
                                
                        
                        
