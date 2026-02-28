from src.hybrid_simulator import run_leo_simulation

def test_reliability_above_90():
    rel = run_leo_simulation(1000)
    assert rel > 90, f"Expected >90%, got {rel:.1f}%"
    print("✅ Unit test passed — Reliability above 90%")
