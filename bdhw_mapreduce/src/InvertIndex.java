/**
 * Created by lwz on 2017/11/18.
 */
//package hdfs;
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

public class InvertIndex {
    public static class InvertedIndexMapper
            extends Mapper<Object,Text,Text,Text>{
        private Text keyInfo = new Text();//存储单词
        private Text valueInfo = new Text();//存储词频
        //private final static IntWritable one = new IntWritable(1);
        private FileSplit split;//存储Split对象
        //@Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            //split = (FileSplit)context.getInputSplit();
            /*String str = value.toString();
            for( String line: str.split("\n")){
                if(line.contains("myurl"))
                    continue;
                else{
                    StringTokenizer itr = new StringTokenizer(line,",");
                    while(itr.hasMoreElements()){
                        keyInfo.set(itr.nextToken()+":");
                        context.write(keyInfo, one);
                    }
                }
            }*/
            split = (FileSplit) context.getInputSplit();
            StringTokenizer itr = new StringTokenizer(value.toString(), ",");
            while(itr.hasMoreTokens()){
                keyInfo.set(itr.nextToken()+":"+split.getPath().toString());
                valueInfo.set("1");
                context.write(keyInfo, valueInfo);//输出：<key,value>---<"MapReduce:1.txt",1>
            }
        }
    }

    public static class InvertedIndexCombiner
            extends Reducer<Text, Text/*IntWritable*/, Text, Text>{
        Text info = new Text();
        //@Override
        public void reduce(Text key, Iterable<Text> values,Context context)
                throws IOException, InterruptedException {
            //输入：<key,value>---<"MapReduce:1.txt",list(1,1,1,1)>
            //key="MapReduce:1.txt",value=list(1,1,1,1);
            Integer sum = 0;
            //int sum = 0;
            for(Text value : values){
                //sum += value.get();
                sum += Integer.parseInt(value.toString());
            }
            int splitIndex = key.toString().indexOf(":");
            info.set(key.toString().substring(splitIndex+1)+":"+sum.toString());
            key.set(key.toString().substring(0,splitIndex));
            context.write(key, info);//输出:<key,value>----<"Mapreduce","0.txt:2">
        }

    }

    public static class InvertedIndexReducer
            extends Reducer<Text, Text, Text, Text>{

        Text result = new Text();
        //@Override
        protected void reduce(Text key, Iterable<Text> values,Context context)
                throws IOException, InterruptedException {
            //输入：<"MapReduce",list("0.txt:1","1.txt:1","2.txt:1")>
            //输出：<"MapReduce","0.txt:1,1.txt:1,2.txt:1">
            String fileList = new String();
            for(Text value : values){//value="0.txt:1"
                fileList += value.toString()+";";
            }
            result.set(fileList);
            context.write(key, result);//输出：<"MapReduce","0.txt:1,1.txt:1,2.txt:1">

        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        //String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
        /*if (otherArgs.length != 2) {
            System.err.println("Usage: InvertedIndex <in> <out>");
            System.exit(2);
        }*/
        //Job job = new Job(conf, "InvertedIndex");
        Job job = Job.getInstance(conf, "InvertedIndex");
        job.setJarByClass(InvertIndex.class);
        //使用InvertedIndexMapper类完成Map过程；
        job.setMapperClass(InvertedIndexMapper.class);
        //使用InvertedIndexCombiner类完成Combiner过程；
        job.setCombinerClass(InvertedIndexCombiner.class);
        //使用InvertedIndexReducer类完成Reducer过程；
        job.setReducerClass(InvertedIndexReducer.class);
        //设置了Map过程和Reduce过程的输出类型，其中设置key的输出类型为Text；
        job.setOutputKeyClass(Text.class);
        //设置了Map过程和Reduce过程的输出类型，其中设置value的输出类型为Text；
        job.setOutputValueClass(Text.class);
        //设置任务数据的输入路径；
        FileInputFormat.addInputPath(job, new Path(args[0]));
        //设置任务输出数据的保存路径；
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        //调用job.waitForCompletion(true) 执行任务，执行成功后退出；
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }


}
