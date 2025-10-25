import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

r.set("name", "Ani")  # string
r.hset("user:1", mapping={"age": 33, "role": "MLE"})  # hash
r.lpush("jobs", "train", "deploy")  # list
r.sadd("skills", "ML", "Docker", "FastAPI")  # set
r.zadd("leaderboard", {"ani": 120, "mesh": 150})  # zset


print(r.get("name"))  # string
print(r.hgetall("user:1"))  # hash
print(r.lrange("jobs", 0, -1))  # list
print(r.smembers("skills"))  # set
print(r.zrange("leaderboard", 0, -1, withscores=True))  # zset