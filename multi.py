import time
import os
import multiprocessing


#Create variable to store the prime numbers and a counter
def pro(start_number, end_number):
    start = time.time()
    primes = []
    noPrimes = 0
#Loop through each number, then through the factors to identify prime numbers
    for candidate_number in range(start_number, end_number, 1):
        found_prime = True
        for div_number in range(2, candidate_number):
            if candidate_number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(candidate_number)
            noPrimes += 1
#Once all numbers have been searched, stop the timer
    end = round(time.time() - start, 2)
#Display the results, uncomment the last to list the prime numbers found
    print(' Find all primes up to: ' + str(end_number),'Time elasped: ' + str(end) + ' seconds','Number of primes found ' + str(noPrimes))

if __name__ == '__main__':
    core = multiprocessing.cpu_count()
    main_start = time.time()
    for i in range(core):
        my_process = multiprocessing.Process(target=pro, args=(1,200000))
        my_process.start()

    for i in range(core):
        my_process.join()

    main_end = round(time.time() - main_start, 2)
    print('Time elasped: ' + str(main_end) + ' seconds')
    print('-------------------------------------------')
