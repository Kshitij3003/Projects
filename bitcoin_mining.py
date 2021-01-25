from hashlib import new, sha256

def sh256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number,transactions,previous_hash,prefix_zeros):
    nounce=1
    Max_num=100000000000
    while True:
        text=str(block_number)+transactions+previous_hash+str(nounce)
        new_hash=sh256(text)
        zeros='0'*prefix_zeros
        if(new_hash.startswith(zeros)):
            return new_hash
        else:
            nounce=+1
    raise BaseException(f"couldn't find correct hash after trying {max_nounce} times")

if __name__=='__main__':
    transactions='''
    Kshitij->Tansihq->20,
    Ram->Shyam->40,
    King->Queen->50
    '''
    difficulty=4
    import time
    start=time.time()
    new_hash=mine(2,transactions,'831a73a68b11ec563ed784643d022a9f3cf6ca0ff7b8589ff50622c7d3cfeee0',difficulty)
    total_time=str((time.time()-start))
    print("Time Taken to mine is:{}".format(total_time))
    print(new_hash)