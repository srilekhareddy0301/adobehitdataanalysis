import sys
import boto3
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from awsglue import DynamicFrame
from datetime import datetime

class adobdeData:

    # define view on the dynamic frames
    def sparkSqlQuery(glueContext, query, mapping, transformation_ctx,spark) -> DynamicFrame:
        for alias, frame in mapping.items():
            frame.toDF().createOrReplaceTempView(alias)
        result = spark.sql(query)
        return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

    #define spark
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)
    #defining needed args
    cdate=datetime.today().strftime('%Y-%m-%d')
    args = getResolvedOptions(sys.argv, ["JOB_NAME","filepath"])
    job.init(args["JOB_NAME"], args)
    filepath=args["filepath"]
    bucket = filepath.split('/')[2]
    outputpath=f"s3://{bucket}/output"

    # Script for reading data into dynamicframe
    AmazonS3_node1681225203068 = glueContext.create_dynamic_frame.from_options(
        format_options={
            "quoteChar": '"',
            "withHeader": True,
            "separator": "\t",
            "optimizePerformance": False,
        },
        connection_type="s3",
        format="csv",
        connection_options={
            "paths": [filepath],
            "recurse": True,
        },
        transformation_ctx="AmazonS3_node1681225203068",
    )

    # Script for generating the Raw data view
    SqlQuery0="""
	SELECT 
	ip,
	from_unixtime(hit_time_gmt) as unix_time,
	date(from_unixtime(hit_time_gmt)) as unix_date,
	product_list,
	case WHEN size(split(product_list,';')) > 3 and trim(split(product_list,';')[3]) <> '' then cast(split(product_list,';')[3] as int) else 0 end as revenue,
	referrer,
	CASE WHEN lower(referrer) like '%mozilla%' THEN replace(lower(REGEXP_EXTRACT(referrer, '^(?:(?:(?:https?|ftp):)?\/\/).+&q=(.*?)(?:&.*?$|$)')),'+',' ') 
	ELSE replace(lower(REGEXP_EXTRACT(referrer, '^(?:(?:(?:https?|ftp):)?\/\/).+?[a-zA-Z]=(.*?)(?:&.*?$|$)')),'+',' ') END as keyword,
	lower(split(referrer,'\\\\.')[1]) as search_engine,
	row_number() over(partition by ip order by from_unixtime(hit_time_gmt) asc) as unique_user_id
	FROM myDataSource order by ip,"date_time";
		"""

    Adobe_gen_data = sparkSqlQuery(
        glueContext,
        query=SqlQuery0,
        mapping={"myDataSource": AmazonS3_node1681225203068},
        transformation_ctx="Adobe_gen_data",
        spark=spark,
    )

    # Script for final Query
    SqlQuery1 = """
	select raw_se.search_engine,raw_se.keyword,sum(raw.revenue) as revenue  from Adobe_gen_data raw left join (select ip,unix_date,search_engine,keyword from Adobe_gen_data where unique_user_id=1 ) raw_se on raw_se.unix_date=raw.unix_date and raw_se.ip=raw.ip
	group by 1,2 order by 3 desc 
		"""
    hit_revenue = sparkSqlQuery(
        glueContext,
        query=SqlQuery1,
        mapping={"Adobe_gen_data": Adobe_gen_data},
        transformation_ctx="hit_revenue",
        spark=spark,
    )

    #convert DynamicFrame to Dataframe
    df=hit_revenue.toDF()
    df=df.coalesce(1)

    # write the data to the output path
    df.write.option("sep","\t").option("header","true").csv(f"{outputpath}/temp")

    res=[]
    # S3 Resources
    s3 = boto3.resource('s3')
    client = boto3.client('s3')
    my_bucket = s3.Bucket(bucket)

    # Get output path Object details
    for object_summary in my_bucket.objects.filter(Prefix="output/temp"):
        res.append(object_summary.key)
        print(res[0])

    # define new & old prefixes
    new_prefix=f'output/{cdate}_SearchKeywordPerformance.tab'
    old_prefix='output/temp'

    # move the files from output temp path to the final path
    copy_source = {
        'Bucket': bucket,
        'Key': res[0]
    }
    s3.meta.client.copy(copy_source, bucket, new_prefix)
    my_bucket.object_versions.filter(Prefix=old_prefix).delete()

    job.commit()
