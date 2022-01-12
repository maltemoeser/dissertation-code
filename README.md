
This repository contains notebooks with code from my dissertation *Cryptocurrency Privacy in Practice*.

A modified version of BlockSci is needed to reproduce these analysis, which can be found [here](https://github.com/maltemoeser/BlockSci/tree/thesis)

### Address clustering - Analyses

- These analyses were run a r5.4xlarge EC2 instance
- The ground truth data set is available for download [here](https://github.com/maltemoeser/address-clustering-data)
- EC2 Notebooks 12e) and after require results from ML notebooks (see below)


### Address clustering - ML

- The machine learning code was run on a machine with 64 cores and 500GB of memory (Princeton CS Cycles cluster)


### Taint tracking

- These analyses were run a r5.4xlarge EC2 instance (though a smaller one might suffice)

### Monero traceability

- The source code can be found [here](https://github.com/maltemoeser/moneropaper)
