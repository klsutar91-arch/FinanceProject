df=spark.read.csv("c://file.txt")
df.show()
df1=spark.sql("select * from employee")
df1.show()