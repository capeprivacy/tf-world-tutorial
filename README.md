# TensorFlow World: Privacy-Preserving Machine Learning with TensorFlow

**Disclaimer: please note that the installation instructions will be updated until October 22nd and the tutorial until October 28th.**

In this tutorial, you will learn how to build and deploy privacy-preserving machine learning models using [TF Encrypted](https://github.com/tf-encrypted/tf-encrypted), [PySyft-TensorFlow](https://github.com/OpenMined/PySyft-TensorFlow), and the [TensorFlow](https://www.tensorflow.org/) ecosystem.

This tutorial was created for the [TensorFlow World conference](https://conferences.oreilly.com/tensorflow/tf-ca/public/schedule/detail/78557) on Tuesday, October the 29th 2019 at 1:30pm PST.

Please join the [TF Encrypted Slack](https://join.slack.com/t/tf-encrypted/shared_invite/enQtNjI5NjY5NTc0NjczLWM4MTVjOGVmNGFkMWU2MGEzM2Q5ZWFjMTdmZjdmMTM2ZTU4YjJmNTVjYmE1NDAwMDIzMjllZjJjMWNiMTlmZTQ). We will be answering questions in the `tf-world-2019` channel!

## Description

Today, we’re trying to take advantage of machine learning across many facets of modern life. However, many of our most impactful uses of machine learning in health care, transportation, and finance are blocked as they require access to sensitive data. In this tutorial, attendees will learn how to use [TF Encrypted](https://github.com/tf-encrypted/tf-encrypted) and [PySyft](https://github.com/OpenMined/PySyft-TensorFlow) to train and deploy machine learning models using remote execution, secure federated learning, and encrypted predictions in the cloud while preserving the privacy of both the model and the end user’s input data.

[TF Encrypted](https://github.com/tf-encrypted/tf-encrypted) and [PySyft](https://github.com/OpenMined/PySyft-TensorFlow) are complementary open-source libraries for designing and building privacy-preserving machine learning workflows.  They both extend TensorFlow and aim to make privacy-preserving machine learning easy without needing to understand the complexities of cryptography, distributed systems, or high-performance computing.

Attendees will use [TF Encrypted](https://github.com/tf-encrypted/tf-encrypted), [PySyft](https://github.com/OpenMined/PySyft-TensorFlow) and TensorFlow to train and deploy machine learning models to the cloud while preserving the privacy of both the model and the end user’s input data. After an introduction to the landscape of privacy-preserving machine learning, we'll dive into a series of hands-on exercises for building models with [TF Encrypted](https://github.com/tf-encrypted/tf-encrypted)’s secure primitives and [PySyft-TensorFlow](https://github.com/OpenMined/PySyft-TensorFlow).  Attendees will take away the skills needed to identify use cases requiring heightened privacy and security, as well as learn how to design, prototype, and deploy private machine learning.

## Installation

To run these notebooks you will need to install:
- UNIX-based OS (e.g. Ubuntu or MacOS)
- Python 3.6+
- [TF Encrypted](https://github.com/tf-encrypted/tf-encrypted)
- [PySyft TensorFlow](https://github.com/OpenMined/PySyft-TensorFlow)
- [TensorFlow 2.0](https://www.tensorflow.org/api_docs/python/tf)
- [NumPy](https://numpy.org/)
- [Jupyter Notebook](https://jupyter.org/)

To install all these dependencies you can simply run: `pip3 install -r requirements.txt`.

To manage dependencies, you can use a virtual environment like `venv` or a package manager like `conda`.  Here's an example using `conda`:

```
conda create -n ppml python=3.7
conda activate ppml
pip install -r requirements.txt
```

### Google Cloud Installation

If you want to run this tutorial with [Google Cloud Platform](https://cloud.google.com/), you will need a [GCP account](https://cloud.google.com/) and install [Google SDK](https://cloud.google.com/sdk/install). See below for a quick reference to the installation procedure.

Run the following commands based on your OS to install gcloud tool.

**MacOS**

```shell
brew cask install google-cloud-sdk
```

**Debian/Ubuntu**

```shell
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get install apt-transport-https ca-certificates curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

**Initialize gcloud (Any OS)**

Run the following command to initialize your Google Cloud configuration. You will have to complete the following:

- Log into the account created above.
- Set your default project to use, it will prompt you to create one if you haven't already made one.
- Set your default zone and region to use.

```
gcloud init
```
