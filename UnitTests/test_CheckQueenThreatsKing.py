import CheckQueenThreatsKing


# Unit Test that were created during cause-effect graphing
def test_horizontalThreat():
    assert CheckQueenThreatsKing.check_threat(1,1,2,1) == True

def test_verticalThreat():
    assert CheckQueenThreatsKing.check_threat(1,1,1,2) == True

def test_diagonalThreat():
    assert CheckQueenThreatsKing.check_threat(1,1,2,2) == True

def test_noThreat():
    assert CheckQueenThreatsKing.check_threat(1,1,3,2) == False

# Notice: Return value for no threat and invalid inputs are identical
def test_noKingInteger():
    assert CheckQueenThreatsKing.check_threat(1.5,1.5,2,2) == False

def test_KingNotOnBoard():
    assert CheckQueenThreatsKing.check_threat(0,0,2,2) == False

def test_noQueenInteger():
    assert CheckQueenThreatsKing.check_threat(1,1,2.5,2.5) == False

def test_QueenNotOnBoard():
    assert CheckQueenThreatsKing.check_threat(1,1,0,0) == False


# Unit Test that were created during boundary value analysis
def test_edgeKingCoords1():
    assert CheckQueenThreatsKing.check_threat(1,1,2,2) == True

def test_edgeKingCoords8():
    assert CheckQueenThreatsKing.check_threat(8,8,2,2) == True

def test_outOfBoundsKingCoords0():
    assert CheckQueenThreatsKing.check_threat(0,0,2,2) == False

def test_outOfBoundsKingCoords9():
    assert CheckQueenThreatsKing.check_threat(9,9,2,2) == False

def test_edgeQueenCoords1():
    assert CheckQueenThreatsKing.check_threat(2,2,1,1) == True

def test_edgeQueenCoords8():
    assert CheckQueenThreatsKing.check_threat(2,2,8,8) == True

def test_outOfBoundsQueenCoords0():
    assert CheckQueenThreatsKing.check_threat(2,2,0,0) == False

def test_outOfBoundsQueenCoords9():
    assert CheckQueenThreatsKing.check_threat(2,2,9,9) == False


# No (new) Unit Tests were found during the generation of the equivalence classes
# Unit Test that were created during error-guessing technique
def test_identicalValidCoords():
    assert CheckQueenThreatsKing.check_threat(1,1,1,1) == False
    # Current Implementation fails this unit test

def test_identicalInvalidCoords():
    assert CheckQueenThreatsKing.check_threat(0,0,0,0) == False


# No (new) Unit Tests were found during logic coverage
# No (new) Unit Tests were found during condition coverage 
