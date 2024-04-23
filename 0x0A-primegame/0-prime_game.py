#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'










{
    "transaction_timestamp": "2024-02-15T12:25:08+00:00", //yyyy-MM-ddTHH:mm:ssz
    "shipped_from_site_code": "6299999999981",
    "shipped_to_site_code": "6299999999998",
    "biz_transactions": { // for available keyss, see section 7.3.3 in https://www.gs1.org/sites/default/files/docs/epc/CBV-Standard-1-2-2-r-2017-10-12.pdf
        "desadv": "6299999999981", // despatch advice | delivery number
        "po": "0081030898", // purchase order
        "inv": "656846513" // invoice
    },
    "items": [
        {
            // unit item information (GTIN, batch, exp, mfg, serial)
            "barcode": "136R49H6GHGE3A",
            "GTIN": "03664798022643",
            "batch_number": "X3C131V",
            "expiry": "2025-09-30",
            "manufacturing_date": "2023-03-20",
            // aggregation hierarchy (up to 7 parnets, typically 3 in most cases)
            "parent1": "136600530023657654",
            "parent2": "236600530023657654",
            "parent3": "336600530023657654",
            "parent4": "436600530023657654"
        },
        {
            "GTIN": "03664798022643",
            "batch_number": "X3C131V",
            "expiry": "2025-09-30",
            "manufacturing_date": "2023-03-20",
            "barcode": "136R49H6GHHK27",
            "parent1": "936600530023657654",
            "parent2": "836600530066857069"
        }
        // add all the items in same manner
    ],
    "external_values": {
        // Any other value
    }
}








