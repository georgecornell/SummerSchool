python -m timeit -n 1000 'import computeCollatz;computeCollatz.collatz(837799,open("c.tmp", "w"))'
python -m cProfile -o collatz.profile computeCollatz.py 837799 c.tmp;python -m pstats collatz.profile



