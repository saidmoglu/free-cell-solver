import cProfile
import pstats
from pstats import SortKey
import io
from freeCellSolver import run_test_cases

profiler = cProfile.Profile()

profiler.enable()

run_test_cases(
    start_index=0,
    end_index=1,
    step_by_step_solution=False,
    print_solution=False,
    max_states=50000,
    heuristic_power_factor=1.5,
    num_threads=1,  # Use single thread for accurate profiling
)

profiler.disable()

s = io.StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats(SortKey.CUMULATIVE)
ps.print_stats(30)
print(s.getvalue())

with open("profile_results.txt", "w") as f:
    ps = pstats.Stats(profiler, stream=f).sort_stats(SortKey.CUMULATIVE)
    ps.print_stats()

    print("\n\nDetailed analysis of key functions:", file=f)
    for func_name in [
        "__hash__",
        "normalized_tableau",
        "valid_moves",
        "apply_move",
        "heuristic",
    ]:
        print(f"\n\nFunction: {func_name}", file=f)
        ps.print_callers(func_name)
        ps.print_callees(func_name)
