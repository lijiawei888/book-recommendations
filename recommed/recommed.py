from pyspark import SparkContext
from pyspark.mllib.recommendation import MatrixFactorizationModel
from pprint import pprint
import redis
pool=redis.ConnectionPool(host='192.168.10.10',port=6379)
redis_client=redis.Redis(connection_pool=pool)

# def redisOp():
#     redis_client.set(1,'bob')
#     print(redis_client.get(1))

def getRecommendByUserID(userid,rec_num):
    sc=SparkContext(master='local[*]',appName='book_recommend')
    try:
        model=MatrixFactorizationModel.load(sc,'file:///root/recommendModel_1')
        result=model.recommendProducts(userid,rec_num)
        temp=''
        for r in result:
            temp+=str(r[0])+','+str(r[1])+','+str(r[2])+'|'
            redis_client.set(userid,temp)
            print('load model success')
        # pprint(result)
    except Exception as e:
        print('load model failed' +str(e))
    sc.stop()
# if __name__ == '__main__':
#     # redisOp()
#      getRecommendByUserid(189,4)
from pyspark import SparkContext
from pyspark.mllib.recommendation import MatrixFactorizationModel
import redis
from pprint import pprint
pool=redis.ConnectionPool(host='192.168.10.10',port=6379)
redis_client= redis.Redis(connection_pool=pool)

# def redisOp():
#     redis_client.set(1,'bob')
#     print(redis_client.get(1))

def getRecommendByUserID(userid,rec_num):
    sc=SparkContext(master="local[*]",appName='book_recommend')
    try:
        model = MatrixFactorizationModel.load(sc,"file:///root/aa")
        result=model.recommendProducts(userid,rec_num)
        pprint(result)
        temp=''
        for r in result:
             temp +=str(r[0])+','+str(r[1])+','+str(r[2])+'|'
        redis_client.set(userid,temp)
        # print(temp)
        print("load model success!!!")
    except Exception as e:
        print("load model failed"+str(e))
    sc.stop()
