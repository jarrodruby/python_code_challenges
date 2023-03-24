from rock_paper_scissors.program import run_strategy

fixture1 = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

def test_main():
    assert run_strategy(fixture1) == 15