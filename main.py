import json 
import pandas as pd

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

all_chunks=[]
for chunk in chunks:
     parse_chunks=parse_chunk(chunk)
     if parse_chunks:
         all_chunks.append(parse_chunks)

#print(all_chunks[1])

# 🛟Yahe ak csv File ko save krega 
df=pd.DataFrame(all_chunks)
print(df.head())
save_csv=df.to_csv("Instagram_following.csv",index=False,encoding="utf-8")
print(save_csv)

# Ye ak json file ko save krega 
with open ("Instagarm_following.jaon","w",encoding="utf-8")as f:
    data=json.dump(all_chunks,f,ensure_ascii=False,indent=4)
    print(f"json file successfully run-->{data}")


#Who Has The minimum Post
for chunk in all_chunks:
    if chunk["Number_of_post"]==min(c["Number_of_post"] for c in all_chunks):
        print(f"The Minimum post is-->{chunk}")

print()

#Who Has The Maximum post
for chunks in all_chunks:
    if chunks["Number_of_post"]==max(c["Number_of_post"] for c in all_chunks):
        print(f"The Maximum post is-->{chunks}")

#Who Has The Minimum Follower
for chunks in all_chunks:
    if chunks["Number_of_follower"]==min(c["Number_of_follower"] for c in all_chunks):
        print(f"The Minimum follower is-->{chunks}")

print()

#Who Has The Maximum Follower
for chunks in all_chunks:
    if chunks["Number_of_follower"]==max(c["Number_of_follower"] for c in all_chunks):
        print(f"Maximum follower is -->{chunks}")
print()

#Who Has The Minimum Following
for chunks in all_chunks:
    if chunks["Number_of_following"]==min(c["Number_of_following"] for c in all_chunks):
        print(f"Minimum Number is-->{chunks}")
print()

#Who Has The Maximum Following
for chunk in all_chunks:
    if chunk["Number_of_following"]==max(c["Number_of_following"] for c in all_chunks):
        print(f"Maximum Following is-->{chunk}")


categury=set()
for chunk in all_chunks:
    categury.add(chunk["Type_of_page"])
print(categury,len(categury))