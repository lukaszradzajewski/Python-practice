"""
Question: Write a function that will keep trying to check a status of a process by calling the function "is_status_success()" until the function returns True.

Retry for 20 seconds while sleeping 3 seconds between each retry. After the 20 seconds raise an exception if the success check is not True.
Make the max retry length and the sleep time keyword parameters to the function with default values.

The function to call to check the status is written below. The function will randomly return True or False.
Call the function in the loop as a way of checking success status of a process.

Requirements:
- use while loop
- use timer
- raise an exception
- keyword parameter for max retry and sleep time

Hint:
 To set a timer you can import time and to set a timeout you can do
    > time.time() + 20 # this will set a timeout 20 seconds from now. time.time() is now.
"""

import random
import time


def is_status_success():
    print("Checking the status of the process.")
    list_to_chose_from = [True, True, False, False, False, False, False]

    bool_to_return = random.choice(list_to_chose_from)

    return bool_to_return


def wait_and_retry_until_status_is_success(max_wait=20, sleep_per_retry=3):
    timeout = time.time() + max_wait
    while time.time() <= timeout:

        status = is_status_success()
        print(f"Status is success: {status}")

        if status:
            print("Success. No retry")
            break
        else:
            print(f"Not success, sleeping for {sleep_per_retry} seconds.")
            time.sleep(sleep_per_retry)
    else:
        raise Exception(f"The status did not succeed after waiting for {max_wait}")


wait_and_retry_until_status_is_success()
