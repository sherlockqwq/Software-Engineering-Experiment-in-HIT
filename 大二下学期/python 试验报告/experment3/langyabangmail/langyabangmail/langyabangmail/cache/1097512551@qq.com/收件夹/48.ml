Received: from hust.edu.cn (unknown [202.114.0.240])
	by newmx115.qq.com (NewMx) with SMTP id
	for <1097512551@qq.com>; Fri, 05 Jan 2018 13:57:41 +0800
X-QQ-FEAT: +K0KBi/SMxnbQA0R4AK5jD49AG2F5S1sVPN9uGe8Lz4SdcKCNLhLtTYVDol0I
	mT3QJK+6By+KOgWejJAP/nfa8+wkQ4/2aD3rl3tKNDoQL9rtrOyewoVqtkJRStsMZ21T1+w
	tPFxUeUsaMkgDT/JTUyydEDFBI5hAhar0zNpWyBpZYh8bHpiUtE9hNIBxhM0xCQfEmPjA4n
	sDPjDaYSEgD77zR+iGLVHMuCHgoM3vXenzIMcwg1qFe8ZoQZSeySEvvQWXLr9Pkk=
X-QQ-MAILINFO: MHG2h55yn1llGeHhBnikmK7jjRsDFtItYeFZEyhZmwaTK4NncOL2xg+tU
	j0XXyvxjCc7CSrN8cHJPAa5prd+1tezIPw7xAOFXoI3JHXC5U6tAW/buejyAIfaTIgS7Uyy
	bk1nXxQUOs3cBjvCvPTngSbkUv7snAct0w==
X-QQ-mid: mx115t1515131862tejbiwihy
X-QQ-ORGSender: chensf@hust.edu.cn
Received: from Thinking (unknown [10.10.198.57])
	by app1 (Coremail) with SMTP id FgEQrAD3CBHNE09aqScfAg--.9989S2;
	Fri, 05 Jan 2018 13:57:33 +0800 (CST)
Date: Fri, 5 Jan 2018 13:57:33 +0800 (CST)
From: <chensf@hust.edu.cn>
To: <1097512551@qq.com>
Message-ID: <981808167.2.1515131853521@Thinking>
Subject: 
MIME-Version: 1.0
Content-Type: multipart/mixed;
	boundary="----=_Part_1_722783749.1515131853462"
X-CM-TRANSID: FgEQrAD3CBHNE09aqScfAg--.9989S2
X-Coremail-Antispam: 1UD129KBjDUn29KB7ZKAUJUUUUU529EdanIXcx71UUUUU7v73
	VFW2AGmfu7bjvjm3AaLaJ3UjIYCTnIWjp_UUUOx7k0a2IF6F4UM7kC6x804xWl1xkIjI8I
	6I8E6xAIw20EY4v20xvaj40_Wr0E3s1l1IIY67AEw4v_Jr0_Jr4l8cAvFVAK0II2c7xJM2
	8CjxkF64kEwVA0rcxSw2x7M28EF7xvwVC0I7IYx2IY67AKxVW7JVWDJwA2z4x0Y4vE2Ix0
	cI8IcVCY1x0267AKxVW8Jr0_Cr1UM28EF7xvwVC2z280aVAFwI0_GcCE3s1l84ACjcxK6I
	8E87Iv6xkF7I0E14v26rxl6s0DM2AIxVAIcxkEcVAq07x20xvEncxIr21le4C267I2x7xF
	54xIwI1l5I8CrVACY4xI64kE6c02F40Ex7xfMc02F40E4c8EcI0Er2xKeI8DMcIj6xIIjx
	v20xvE14v26r1Y6r17McIj6I8E87Iv67AKxVW8JVWxJwAm72CE4IkC6x0Yz7v_Jr0_Gr1l
	F7xvr2IY64vIr41lFcxC0VAqx4xG64AKrs4lw4CE7480Y4vE14AKx2xKxVC2ax8xM4kE6x
	kIj40Ew7xC0wCF04k20xvY0x0EwIxGrwCF04k20xvE74AGY7Cv6cx26r43Zr1UJr1l4I8I
	3I0E4IkC6x0Yz7v_Jr0_Gr1lx2IqxVAqx4xG67AKxVWUGVWUWwC20s026x8GjcxK67AKxV
	WUJVWUGwC2zVAF1VAY17CE14v26r1j6r15MIIYrxkI7VAKI48JMIIF0xvE2Ix0cI8IcVAF
	wI0_Jr0_JF4lIxAIcVC0I7IYx2IY6xkF7I0E14v26r1j6r4UMIIF0xvE42xK8VAvwI8IcI
	k0rVWrJr0_WFyUJwCI42IY6I8E87Iv67AKxVW8JVWxJwCI42IY6I8E87Iv6xkF7I0E14v2
	6r4j6r4UJbIYCTnIWIevJa73UjIFyTuYvjxUIVyxDUUUU
X-CM-SenderInfo: zxsqikarttllo6kx23oohg3hdfq/

------=_Part_1_722783749.1515131853462
Content-Type: text/html;charset=UTF-8
Content-Transfer-Encoding: 7bit

fdksaklf
------=_Part_1_722783749.1515131853462
Content-Type: application/octet-stream; name=eval.py
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename=eval.py

#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers
import word2vec_helpers
from text_cnn import TextCNN
import csv

# Parameters
# ==================================================

# Data Parameters
tf.flags.DEFINE_string("input_text_file", "./test1", "Test text data source to evaluate.")
tf.flags.DEFINE_string("input_label_file", "", "Label file for test text data source.")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./1514720888/checkpoints", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", True, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")

# validate
# ==================================================

# validate checkout point file
checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
if checkpoint_file is None:
    print("Cannot find a valid checkpoint file!")
    exit(0)
print("Using checkpoint file : {}".format(checkpoint_file))

# validate word2vec model file
trained_word2vec_model_file = os.path.join(FLAGS.checkpoint_dir, "..", "trained_word2vec.model")
if not os.path.exists(trained_word2vec_model_file):
    print("Word2vec model file \'{}\' doesn't exist!".format(trained_word2vec_model_file))
print("Using word2vec model file : {}".format(trained_word2vec_model_file))

# validate training params file
training_params_file = os.path.join(FLAGS.checkpoint_dir, "..", "training_params.pickle")
if not os.path.exists(training_params_file):
    print("Training params file \'{}\' is missing!".format(training_params_file))
print("Using training params file : {}".format(training_params_file))

# Load params
params = data_helpers.loadDict(training_params_file)
num_labels = int(params['num_labels'])
max_document_length = int(params['max_document_length'])

# Load data
if FLAGS.eval_train:
    x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.input_text_file, FLAGS.input_label_file, num_labels)
else:
    x_raw = ["a masterpiece four years in the making", "everything is off."]
    y_test = [1, 0]

# Get Embedding vector x_test
sentences, max_document_length = data_helpers.padding_sentences(x_raw, '<PADDING>', padding_sentence_length = max_document_length)
x_test = np.array(word2vec_helpers.embedding_sentences(sentences, file_to_load = trained_word2vec_model_file))
print("x_test.shape = {}".format(x_test.shape))


# Evaluation
# ==================================================
print("\nEvaluating...\n")
checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
graph = tf.Graph()
with graph.as_default():
    session_conf = tf.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # Load the saved meta graph and restore variables
        saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        # input_y = graph.get_operation_by_name("input_y").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

        # Tensors we want to evaluate
        predictions = graph.get_operation_by_name("output/predictions").outputs[0]

        # Generate batches for one epoch
        batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

        # Collect the predictions here
        all_predictions = []

        for x_test_batch in batches:
            batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            all_predictions = np.concatenate([all_predictions, batch_predictions])
        print(all_predictions)

# Print accuracy if y_test is defined
if y_test is not None:
    correct_predictions = float(sum(all_predictions == y_test))
    print("Total number of test examples: {}".format(len(y_test)))
    print("Accuracy: {:g}".format(correct_predictions/float(len(y_test))))

# Save the evaluation to a csv
predictions_human_readable = np.column_stack((np.array([text.encode('utf-8') for text in x_raw]), all_predictions))
out_path = os.path.join(FLAGS.checkpoint_dir, "..", "prediction.csv")
print("Saving evaluation to {0}".format(out_path))
with open(out_path, 'w') as f:
    csv.writer(f).writerows(predictions_human_readable)

------=_Part_1_722783749.1515131853462--

