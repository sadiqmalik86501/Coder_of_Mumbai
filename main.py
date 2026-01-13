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

        number_of_post=int(
                            sep_chunk[2].
                            split(" posts")[0]
                            .replace(",","")
                          )

        number_of_follower=float(
                                   sep_chunk[3].
                                   split(" followers")[0].
                                   replace(",","").
                                   replace("K","").
                                   replace("M","")
                                )
        
        if "K" in sep_chunk[3]:
            number_of_follower=int(number_of_follower*1000)

        elif "M" in sep_chunk[3]:
            number_of_follower=int(number_of_follower*1000000)

        else:
            number_of_follower=int(number_of_follower)
        number_of_following=float(
                                    sep_chunk[4].
                                    split(" following")[0].
                                    replace(",","").
                                    replace("K","").
                                    replace("M","")
                                 )
        
        if "K" in sep_chunk[4]:
            number_of_following=int(number_of_following*1000)

        elif "M" in sep_chunk[4]:
            number_of_following=int(number_of_following*1000000)

        else:
            number_of_following=int(number_of_following)

        if len(sep_chunk)>=6:
            type_of_page=sep_chunk[5]
            bio="\n".join(sep_chunk[6:])

        else:
            type_of_page="Unknown"
            bio=""

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
#print(parse_data[0])