from secrets import token_bytes

def proof_of_work(function):
    while True:
        random_message = token_bytes(32)
        hash = function(bytearray(random_message))
        if hash[:3] == '0'*3:
            print("Hash: " + hash)
            break


if __name__ == '__main__':
    import time
    from hash_functions.sha256 import sha256

    for i in range(3):
        start = time.time()
        proof_of_work(sha256)
        stop = time.time()
        print(stop-start)