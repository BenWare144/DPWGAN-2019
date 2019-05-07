# DPWGAN
Original network based on an implementation by [adler-j](https://github.com/adler-j/minimal_wgan) who states:<br>
> The implementation follows [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028), using the network from [the accompanying code](https://github.com/igul222/improved_wgan_training).
This code incorporates [Weka](https://www.cs.waikato.ac.nz/ml/weka/).

### Data Preprocessing Preprocess_Data.ipynb
1. Set up directory structure with<br>
`mkdir -p DATA/{PREPROCESSED/TEST,PREPROCESSED/TRAIN,ORIGINAL/.tmp,GENERATED}`

1. Then download the data sets from here:<br>
[KCCFD](https://www.kaggle.com/mlg-ulb/creditcardfraud#creditcard.csv)<br>
[KCCR](https://www.kaggle.com/loveall/cervical-cancer-risk-classification)
1. Place them in data `DATA/ORIGINAL`
1. Rename the Kaggle Credit Card Fraud Detection data to KCCFD.csv
1. Rename the Kaggle Cervical Cancer Risk data to KCCR.csv
1. Run the cell in Preprocess_Data.ipynb
  1. Saves files in both `.arff` (required for Weka) and `.csv`

### Generating synthetic datasets: DPWGAN.ipynb
1. A synthetic dataset using the examples in the second cell
1. Run the first cell to define all the required functions and classes
1. The second cell contains examples on how to use the code
    1. To train the non-DP WGAN on all three datasets, run:<br>
    `train_WGAN(name="my_data")`<br>
    1. To train the DPWGAN on all three datasets with privacy budjet ϵ, run:<br>
    `train_DPWGAN(name="my_data",epsilon=1)`<br>
    1. To train the DPWGAN on all three datasets for $ϵ ∈ [0.01, 0.05, 0.1, 0.5, 1, 5, 10, inf]$, run:<br>
    `train_all_DPWGANs()`<br>
    1. The data will be stored in the GENERATED folder with a descriptive name. For example:<br>
    `DATA/GENERATED/DPWGAN_MNIST_my_data_GENERATED_for_DPWGAN.csv`


### Evaluating the synthetic data: Evaluating_Datasets.ipynb

1. In the first cell, set the weka_path variable to the path to your weka.jar file.
1. Then other classifiers are desired, specify the model as it would be used if one were using Weka from the command line.
    1. These classifiers can be located in the Weka documentation, or copied directly from the Weka explorer.
    1. Remember to escape quotes.
1. Then run use:<br>
`runlists = generate_run_lists()`<br>
to create a list of every combination of defined dataset with every defined model type.<br>
I.e. if only models trained on the MNIST dataset are desired but not with SGD, simply include:<br>
`runlists=lists_with(runlists,"MNIST")`<br>
`runlists=lists_without(runlists,"SGD")`
1. Finally use to parse this information and train, evaluate, and retrieve and append the AUROC, run:<br>
`results = run_models(runlists)`<br>
Which will train the models on the generated sets, test them on the corresponding test sets, and return AUROC appended onto the list.

### Analysis: Analysis.ipynb
1. An example of how this data can be visualized is shown in the Analysis.ipynb notebook.
1. It shows how I generated my figures and table.
