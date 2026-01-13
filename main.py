with open("data.txt","r",encoding="utf-8") as f:
    data=f.read()
    #print(data)

chunks=data.split("\n\n")
chunks=[c for c in chunks if len(c)>6]
#print(chunks)

def parse_chunk(chunk):
    try:
        chunk=chunk.strip()
        sep_chunk=chunk.split("\n")
        username=sep_chunk[0]
        name=sep_chunk[1]
        number_of_post=sep_chunk[2]
        number_of_follower=sep_chunk[3]
        number_of_following=sep_chunk[4]
        type_of_page=sep_chunk[5]
        bio="\n".join(sep_chunk[6:])

        return {
                "Number_of_post":number_of_post,
                "Number_of_follower":number_of_follower,
                "Number_of_following":number_of_following,
                "Type_of_page":type_of_page,
                "Bio":bio
        }
    except Exception as e:
        print(chunk,e)
        return None

parse_data=[parse_chunk(c) for c in chunks]
print(parse_data)