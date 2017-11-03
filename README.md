## a transfer learning with inception v3
### 1. scraping image urls from walmart search result page

```bash
# the url lists will be saved as *.txt files in the directory "./imageUrl"
python get_image_batch_urls.py
```
### 2. download images with the url lists

```bash
# the images will be download into the directory "./imageDownload"
python3 download_image.py -n 1000 -s 450
```

### 3. train the model 

```bash
python ./image_retraining/retrain.py \
--image_dir=./imageDownload/ \
--output_graph=./TF/output_graph.pb \
--output_labels=./TF/output_labels.txt \
--summaries_dir=./TF/retrain_logs \
--how_many_training_steps=4000 \
--model_dir=./TF/imagenet \
--bottleneck_dir=./TF/bottleneck
```

### 4. test a image

```bash
python ./image_retraining/label_image.py \
--graph=./TF/output_graph.pb --labels=./TF/output_labels.txt \
--output_layer=final_result:0 \
--image=./test.jpeg
```

### 5. notes
the "image_retaining" directory is from the original tensorflow repository "tensorflow/examples/image_retraining".<br />
the "draft_test_code" directory contains the draft codes for web scraping.

