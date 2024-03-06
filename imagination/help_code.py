import shelve


def count_(string, id):
    all_ = []
    k = 0
    for i in string:
        part0 = i.split("(==)")[0]
        part1 = i.split("(==)")[1]
        part2 = i.split("(==)")[2]
        if part1 == id:
            all_.add(0)
            if part2 > k:
                k = part2
    return (all_, k)

def get_actual_path(user_id):
    data = shelve.open("image_actual")
    abs_path = data[f"actual{user_id}"]
    return abs_path




