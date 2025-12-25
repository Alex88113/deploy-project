from app import sum

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_sum()
