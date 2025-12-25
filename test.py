from app import sum, multy

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    print("All tests passed!")

def test_multy():
    assert multy(2, 4) == 10
    
if __name__ == "__main__":
    main()
    
