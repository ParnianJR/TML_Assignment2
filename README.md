# Stolen Model Detection

This repository contains the code used for Trustworthy Machine Learning Course , Assignment 2: **Stolen Model Detection**.

## Files

- `TML_VFinal.ipynb`: final notebook used to generate the leaderboard submission.
- `train_main_idx.json`: target-model training indices provided with the assignment.
- `features_v12.csv`: cached feature table for the best run.
- `submission.csv`: final prediction file submitted to the leaderboard. It contains one row per suspect model, with columns `id` and `score`; higher scores indicate higher confidence that the model was stolen.
- `submit.py`: optional submission helper. You should add your own API key locally.

Large model checkpoints, CIFAR-100 data, Hugging Face caches, and generated runtime folders are not included.

## Recreating the Best Result

Run `TML_VFinal.ipynb` in a GPU notebook environment such as Kaggle (we used Kaggle).

The notebook downloads the assignment assets from:

```text
SprintML/tml26_task2
```

It also downloads CIFAR-100 through `torchvision.datasets.CIFAR100`.

The notebook compares the target model with the 360 suspect models using batch-normalization statistics, output-distribution similarities, representation similarities, augmentation-response probes, boundary probes, and input-gradient similarity. The final submission is generated from the `max` score variant.

To reproduce the submitted result:

1. Open `TML_VFinal.ipynb`.
2. Use a GPU runtime.
3. Run the notebook from top to bottom.
4. The final file is saved as:

```text
submission.csv
```

If using the cached features instead of recomputing all suspect-model features, place `features_v12.csv` at the notebook's runtime feature path before running the scoring cells:

```text
Kaggle: /kaggle/working/tml_12/features_v12.csv
Colab:  /content/tml_v12/features_v12.csv
Local:  ./tml_v12/features_v12.csv
```

The leaderboard score obtained with this version was `0.74` on the public leaderboard.
