from main import Bank

bankObj = Bank()

def test_getAmount():
    assert bankObj.getAmount() == 0

def test_deposit():
    bankObj.deposit(500)
    assert bankObj.getAmount() == 500

def test_withDraw():
    bankObj.withDraw(500)
    assert bankObj.getAmount() == 0