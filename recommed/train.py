from pyspark.mllib.recommendation import ALS
from pyspark.sql import SparkSession
from pyspark.sql import Row

if __name__ == '__main__':
    spark=SparkSession.builder.getOrCreate()
    sc=spark.sparkContext
    # 读取数据
    rdd1=sc.textFile("hdfs://mycluster/book/hits.txt")
    ratingRDD=rdd1.map(lambda x:x.split('\t'))
    print(ratingRDD.take(3))
    user_row=ratingRDD.map(lambda x:Row(userid=int(x[0]),bookid=int(x[1]),hitnum=int(x[2])))

    # 将rdd转为spark的df
    user_df=spark.createDataFrame(user_row)
    user_df.printSchema()
    # user_df.show()

    # 将df创建为临时表
    user_df.createOrReplaceTempView('test')

    datatable=spark.sql("""
    select userid,bookid,sum(hitnum) as hitnum from test group by userid,bookid
    """)
    # datatable.show()

    bookrdd=datatable.rdd.map(lambda x:(x.userid,x.bookid,x.hitnum))
    # print(bookrdd.take(3))
    #
    # 使用ASL：训练的数据集，特征集数据,迭代次数，正则因子
    model=ALS.trainImplicit(bookrdd,10,10,0.01)
      # print(model)

    # 测试
    # model.recommendProducts(169,5)

    # 保存model
    import os
    import  shutil
    # 用来删除已经存在的目录
    if os.path.exists('/root/recommendModel_1'):
        shutil.rmtree('/root/recommendModel_1')
    model.save(sc,'file:///root/recommendModel_1')
    print("训练完成")