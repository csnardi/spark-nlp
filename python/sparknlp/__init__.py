import sys
from pyspark.sql import SparkSession
from sparknlp import annotator
from sparknlp.base import DocumentAssembler, Finisher, TokenAssembler, Chunk2Doc, Doc2Chunk

sys.modules['com.johnsnowlabs.nlp.annotators'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.tokenizer'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.tokenizer.wordpiece'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.ner'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.ner.regex'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.ner.crf'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.ner.dl'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.pos'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.pos.perceptron'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sbd'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sbd.pragmatic'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sbd.deep'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sda'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sda.pragmatic'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.sda.vivekn'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.spell'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.spell.norvig'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.spell.context'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.spell.symmetric'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.parser'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.parser.dep'] = annotator
sys.modules['com.johnsnowlabs.nlp.annotators.parser.typdep'] = annotator
sys.modules['com.johnsnowlabs.nlp.embeddings'] = annotator

annotators = annotator
embeddings = annotator


def start(include_ocr=False):
    builder = SparkSession.builder \
        .appName("Spark NLP") \
        .master("local[*]") \
        .config("spark.driver.memory", "6G") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

    if include_ocr:
        builder \
            .config("spark.jars.packages", "JohnSnowLabs:spark-nlp:2.0.8,com.johnsnowlabs.nlp:spark-nlp-ocr_2.11:2.0.8,javax.media.jai:com.springsource.javax.media.jai.core:1.1.3") \
            .config("spark.jars.repositories", "http://repo.spring.io/plugins-release")

    else:
        builder.config("spark.jars.packages", "JohnSnowLabs:spark-nlp:2.0.8") \

    return builder.getOrCreate()


def version():
    print('2.0.8')
