

id_counter: int = 0

def gen_id() -> str:
    global id_counter
    r = id_counter
    id_counter = id_counter + 1
    return "GEN_{}".format(r)